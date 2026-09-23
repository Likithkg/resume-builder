"""
Renderer entrypoint for the SDE resume builder.

Main.py is the DETERMINISTIC renderer. It takes a Content Manifest (the JSON produced by the
multi-model pipeline) and writes the PDF + DOCX artifacts. It does NOT spawn sub-agents or call
the Anthropic API — that orchestration is driven by the Claude Code main agent per SKILL.md,
which uses the model you selected in the terminal for every stage.

  python main.py --json <content_manifest.json> [--out ./output]

Artifacts: output/<name>_Resume.pdf and output/<name>_Resume.docx

The Content Manifest schema matches what the renderer expects:
  {
    "header": {"name","email","phone","location","github","linkedin","summary", ...},
    "education": [{"institution","start_date","end_date","degree","location", ...}],
    "experience": [{"company","start_date","end_date","role","location","bullet_points":[...]}, ...],
    "skills": { "Category": ["s", ...], ... },
    "projects": [{"name","technologies":["..."],"bullet_points":[...]}, ...],
    "awards": [{"title","issuer", ...}, ...]
  }

`objective` from the content stage maps to header.summary; `achievement` maps to awards.
"""
import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_PARENT = os.path.dirname(_HERE)          # skill root (contains docs/, data/, renderer/)
_RENDERER = os.path.join(_PARENT, "renderer")
# Scanned format folders live in the project-root references/ (three levels up:
# engine -> skill root -> .claude/skills -> project root).
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_REFERENCES = os.path.join(_PROJECT_ROOT, "references")
for _p in (_PARENT, _RENDERER):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from jinja2 import Template  # noqa: E402
import render_pdf  # noqa: E402
import validate  # noqa: E402


def _load_json(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def _render_html(data: dict, template_path: str, css_path: str) -> str:
    with open(template_path, "r") as f:
        template = Template(f.read())
    css = open(css_path, "r").read()
    return render_pdf.inject_css(template.render(data), css)


def resolve_format(fmt: str | None) -> dict | None:
    """Locate a scanned format folder and return its template/css paths, or None.

    `fmt` matches the folder under `references/` created by tools/scan.py
    (the format name, e.g. the reference PDF's stem). Falls back gracefully:
    the PDF renders directly from the format's template.html + styles.css,
    while DOCX uses the canonical renderer (DOCX section order is fixed and
    is not scanned per-reference).
    """
    if not fmt:
        return None
    folder = os.path.join(_REFERENCES, fmt)
    if not os.path.isdir(folder):
        available = sorted(
            d for d in os.listdir(_REFERENCES)
            if os.path.isdir(os.path.join(_REFERENCES, d))
        )
        raise FileNotFoundError(
            f"Format {fmt!r} not found under references/. Available: {available}"
        )
    template_path = os.path.join(folder, "template.html")
    if not os.path.isfile(template_path):
        raise FileNotFoundError(f"template.html missing in format {fmt!r}: {folder}")
    css_path = os.path.join(folder, "styles.css")
    if not os.path.isfile(css_path):
        raise FileNotFoundError(f"styles.css missing in format {fmt!r}: {folder}")
    return {"folder": folder, "template": template_path, "css": css_path, "format": fmt}


def render_artifacts(manifest: dict, out_dir: str, out_prefix="Resume",
                     fmt: str | None = None) -> dict:
    """Validate then render PDF (per-format) + DOCX (canonical) for a manifest.

    Args:
        manifest: validated content manifest.
        out_dir: output directory.
        out_prefix: filename prefix for artifacts.
        fmt: optional scanned format name (folder under references/). When set,
             the PDF renders with the format's own template.html + styles.css;
             the DOCX always uses the canonical renderer.
    """
    ok, errors = validate.validate_resume_data(manifest)
    if not ok:
        raise ValueError("Content manifest failed validation: " + "; ".join(errors))

    name = (manifest.get("header", {}).get("name") or "Candidate").replace(" ", "_")
    os.makedirs(out_dir, exist_ok=True)
    pdf = os.path.join(out_dir, f"{name}_{out_prefix}.pdf")
    docx = os.path.join(out_dir, f"{name}_{out_prefix}.docx")

    resolved = resolve_format(fmt)
    if resolved:
        # PDF: per-format template + CSS.
        html = _render_html(manifest, resolved["template"], resolved["css"])
        render_pdf.render_to_pdf(html, pdf)
        # DOCX: canonical single writer (fixed section order).
        render_pdf.render_to_docx(manifest, docx)
        source = f"{resolved['format']}"
    else:
        # PDF: default locked template.
        html = _render_html(manifest,
                            os.path.join(_RENDERER, "template.html"),
                            os.path.join(_RENDERER, "styles.css"))
        render_pdf.render_to_pdf(html, pdf)
        render_pdf.render_to_docx(manifest, docx)
        source = "default"

    return {"pdf": pdf, "docx": docx, "format": source}


def main():
    ap = argparse.ArgumentParser(description="SDE resume builder: deterministic renderer")
    ap.add_argument("--json", required=True, help="Content Manifest JSON to render")
    ap.add_argument("--out", default="./output", help="Output directory (default ./output)")
    ap.add_argument("--format", default=None,
                    help="Scanned format folder under references/ to render the PDF with.")
    args = ap.parse_args()

    manifest = _load_json(args.json)
    out = render_artifacts(manifest, args.out, fmt=args.format)
    print("Rendered:")
    for kind, path in out.items():
        print(f"  {kind}: {path}")


if __name__ == "__main__":
    main()
