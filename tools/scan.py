#!/usr/bin/env python3
"""
Standalone reference-PDF scanner for the SDE resume builder.

Scans a reference resume PDF *word by word* via PyMuPDF (`fitz`) — using
`page.get_text("dict")`, which yields every text run with its bbox, font,
size, colour and position — then infers the visual structure of the resume:

  * page geometry (A4 vs US Letter) from the media box
  * top/left/right/bottom margins (from the text bounding box)
  * the font stack, point sizes used, and dominant body/name/section sizes
  * colour palette (foreground + any non-black accent)
  * section order (by vertical position, with kind classification)
  * bullet character(s) used inside list items
  * column layout (single vs. multi-column)

For every scanned PDF it writes a **format folder** containing the artefacts
needed to reproduce that layout in a new resume:

    references/<name>/
      spec.md          human-readable visual spec (structure only — no candidate data)
      spec.json        machine-readable extracted reference (validation source)
      template.html    Jinja2 skeleton in the detected section order
      styles.css       detected fonts / sizes / colours / margins / page size
      index.html       self-contained interactive preview page
      preview.js       preview behaviour (live placeholder edit + re-render)

### Security contract
This tool is READ-ONLY of the reference and OUTPUTS ONLY VISUAL STRUCTURE.
It NEVER emits the text content of the reference (no names, dates, projects,
contact info, or any candidate fact) — visual structure only, in `spec.json`
and the template. Candidate facts come solely from `docs/candidate-profile.md`.

    python3 tools/scan.py <path/to/reference.pdf> [--out DIR] [--name FORMAT_NAME]
    python3 tools/scan.py --dir references --out references            # scan all
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict

# --- PyMuPDF import (fitz is the stable alias; `pymupdf` triggers deprecation warn) ---
try:
    import fitz  # type: ignore
    FROM = "fitz"
except ImportError:  # pragma: no cover
    try:
        import pymupdf as fitz  # type: ignore
        FROM = "pymupdf"
    except ImportError as e:  # pragma: no cover
        sys.stderr.write(
            "PyMuPDF is required. Install with: pip install pymupdf\n"
        )
        raise SystemExit(1) from e

PAGE_SIZES = {
    "612x792": "US Letter",
    "595.28x841.89": "ISO A4",
    "595x842": "ISO A4",
    "612x792.01": "US Letter",
}

# Known embedded font sub-names -> a CSS-accessible family fallback.
_CMAP = {
    "CMR": "Times New Roman", "CMBX": "Times New Roman", "CMTI": "Times New Roman",
    "CMSY": "Times New Roman", "CMEX": "Times New Roman", "CMMI": "Times New Roman",
    "CMTT": "Courier New", "CMBI": "Times New Roman",
    "Cambria": "Cambria", "Georgia": "Georgia", "Arial": "Arial",
    "Times": "Times New Roman", "Calibri": "Calibri", "Helvetica": "Helvetica",
}


# --------------------------------------------------------------------------- #
# Low-level colour / font helpers
# --------------------------------------------------------------------------- #
def argb_to_hex(argb: float) -> str:
    """Convert a fitz ARGB float (0 == black) to a #RRGGBB hex string."""
    raw = int(round(argb))
    if raw < 0:
        raw += 1 << 32
    r = (raw >> 16) & 0xFF
    g = (raw >> 8) & 0xFF
    b = raw & 0xFF
    # fitz treats 0 as "black", not transparent; keep it simple.
    return f"#{r:02x}{g:02x}{b:02x}"


def font_family(raw: str) -> str:
    """Map an embedded font sub-name to a clean CSS family name."""
    if not raw:
        return ""
    for key, fam in _CMAP.items():
        if raw.startswith(key):
            return fam
    # Strip weight/style suffixes: "Cambria-Bold" -> "Cambria",
    # "TimesNewRomanPS-BoldMT" -> "Times New Roman".
    cleaned = re.sub(r"[-_].*$", "", raw)
    cleaned = re.sub(r"([a-z])([A-Z])", r"\1 \2", cleaned)
    return cleaned or raw


# --------------------------------------------------------------------------- #
# Scanning
# --------------------------------------------------------------------------- #
def scan_pdf(pdf_path: str) -> dict:
    """Scan one reference PDF and return the extracted visual spec."""
    doc = fitz.open(pdf_path)
    page = doc[0]  # one-page resumes; the canonical template is single-page

    mediabox = page.mediabox
    width_pt = round(mediabox.x1, 2)
    height_pt = round(mediabox.y1, 2)
    size_key = f"{int(round(width_pt))}x{int(round(height_pt))}"
    page_size_name = PAGE_SIZES.get(size_key) or (
        "US Letter" if abs(width_pt - 612) < 1 else "A4"
    )

    text_dict = page.get_text("dict")
    blocks = text_dict.get("blocks", [])
    spans = []
    for block in blocks:
        for line in block.get("lines", []):
            spans.extend(line.get("spans", []))

    # Collect per-span geometry + attributes. y=0 is the page bottom.
    records = []
    font_counts = Counter()
    size_counts = Counter()
    color_counts = Counter()
    min_x = min_x_edge = float("inf")
    max_x = max_x_edge = -float("inf")
    top_y1 = -float("inf")  # largest y1 (top edge)
    bottom_y0 = float("inf")  # smallest y0 (bottom edge)
    for sp in spans:
        text = sp.get("text", "")
        if not text.strip():
            continue
        bbox = sp["bbox"]
        x0, y0, x1, y1 = bbox
        x_center = (x0 + x1) / 2
        y_center = (y0 + y1) / 2
        records.append(
            {
                "text": text,
                "x0": x0, "y0": y0, "x1": x1, "y1": y1,
                "x_center": x_center, "y_center": y_center,
                "font": font_family(sp.get("font", "")),
                "size": round(float(sp["size"]), 2),
                "color_hex": argb_to_hex(sp.get("color", 0.0)),
                "flags": sp.get("flags", 0),
            }
        )
        font_counts[sp.get("font", "")] += 1
        size_counts[round(float(sp["size"]), 2)] += 1
        color_counts[argb_to_hex(sp.get("color", 0.0))] += 1
        min_x = min(min_x, x0)  # leftmost text
        max_x = max(max_x, x1)  # rightmost text
        top_y1 = max(top_y1, y1)  # y1 is the TOP edge (origin at bottom-left)
        bottom_y0 = min(bottom_y0, y0)  # y0 is the BOTTOM edge

    # Margins (pt). mediabox.x0/y0 is usually 0; subtract to be exact.
    mx0 = mediabox.x0
    my0 = mediabox.y0
    left_margin = round(min_x - mx0, 2)
    right_margin = round(width_pt - (max_x - mx0), 2)
    top_margin = round(height_pt - (top_y1 - my0), 2)
    bottom_margin = round(bottom_y0 - my0, 2)

    # Text-area width vs page width -> rough column inference.
    text_area_width = max_x - min_x
    usable_width = width_pt - left_margin - right_margin

    # Fonts / sizes.
    dominant_font = font_counts.most_common(1)[0][0] if font_counts else ""
    body_size = _mode(size_counts)
    sizes_used = sorted(size_counts)

    # Colour palette: black dominant; capture any strong non-black accent.
    black_hex = "#000000"
    accent_colors = [c for c, n in color_counts.items()
                     if c.lower() not in ("#000000", "#ffffff", "#fff") and c != black_hex]
    accent_counts = Counter(accent_colors)
    accent_hex = accent_counts.most_common(1)[0][0] if accent_counts else None

    # Section-title detection: short bold lines near the left margin.
    sections = _detect_sections(records)

    # Bullet character detection: scan line-initial glyph of list items.
    bullet_char = _detect_bullets(records)

    # Column layout: detected by horizontal glyph-density profile. We score the
    # page at many x positions (2pt bins) and ask whether content exists in
    # BOTH the left and right halves. A single-column resume has most of its
    # glyphs in the left ~2/3 and nothing past the gutter.
    columns = _detect_columns(records, width_pt)

    doc.close()

    return {
        "source_file": os.path.basename(pdf_path),
        "page": {
            "width_pt": width_pt,
            "height_pt": height_pt,
            "size_key": size_key,
            "page_size_name": page_size_name,
            "margins_pt": {
                "top": top_margin,
                "bottom": bottom_margin,
                "left": left_margin,
                "right": right_margin,
            },
            "text_area_width_pt": round(text_area_width, 2),
            "usable_width_pt": round(usable_width, 2),
        },
        "typography": {
            "dominant_font": dominant_font,
            "font_families": {font_family(f): n for f, n in
                              font_counts.most_common()},
            "sizes_used_pt": sizes_used,
            "body_size_pt": body_size,
        },
        "colors": {
            "foreground": black_hex,
            "accent": accent_hex,
        },
        "layout": {
            "columns": columns,
            "sections": sections,
            "bullet_char": bullet_char,
        },
        "_report": {  # human-readable diagnostics; trimmed in spec.json
            "raw_font_counts": dict(font_counts.most_common()),
            "raw_size_counts": dict(size_counts.most_common()),
            "raw_color_counts": dict(color_counts.most_common()),
        },
    }


def _mode(counter: Counter):
    return counter.most_common(1)[0][0] if counter else None


# --------------------------------------------------------------------------- #
# Heuristics
# --------------------------------------------------------------------------- #
def _lines_of(records):
    """Group records into horizontal lines (same integer y-centre band)."""
    bands = defaultdict(list)
    for r in records:
        band = round(r["y_center"])
        bands[band].append(r)
    # Merge adjacent 1-px bands.
    ordered = sorted(bands)
    merged = []
    for band in ordered:
        rows = sorted(bands[band], key=lambda r: r["x0"])
        # join if gap to previous < ~4pt
        grouped = []
        cur = []
        for r in rows:
            if cur and r["x0"] - cur[-1]["x1"] < 4:
                cur.append(r)
            else:
                if cur:
                    grouped.append(cur)
                cur = [r]
        if cur:
            grouped.append(cur)
        merged.append((band, grouped))
    return merged


def _is_title_like(recs_first, margin_x0: float, min_size: float = 10.5) -> bool:
    """Heuristic: a line that looks like a section header.

    Section headers are bold, >= 10.5pt, short (< 30 chars), and flush to the
    left margin — regardless of the case convention (ALL CAPS vs Title Case).
    The largest bold title on the page (the candidate name, e.g. 20-25pt) is
    excluded by the caller via the relative-size cap, not here.
    """
    r = recs_first
    flags = r.get("flags", 0)
    is_bold = bool(flags & 1 << 4)  # bit 4 == bold in fitz char_flags
    return (
        is_bold
        and r["size"] >= min_size
        and r["x0"] <= margin_x0 + 8  # flush-left, not indented like an entry
        and len(r["text"].strip()) < 30
    )


def _detect_sections(records):
    """Detect section-title lines and classify each into the renderer's kinds."""
    lines = _lines_of(records)
    if not records:
        return []
    margin_x0 = min(r["x0"] for r in records)
    candidates = []
    for band, rows in lines:
        all_spans = [r for row in rows for r in row]
        text = " ".join(r["text"].strip() for r in all_spans).strip()
        if not text or len(text) > 40 or all(ch.isspace() for ch in text):
            continue
        if not _is_title_like(all_spans[0], margin_x0):
            continue
        candidates.append({"text": text, "y": band, "first": all_spans[0]})

    if not candidates:
        return []

    # The candidate name (e.g. 20-25pt) is far larger than any header. Reject
    # anything more than 1.6x the median header size.
    sizes = [c["first"]["size"] for c in candidates]
    median_size = sorted(sizes)[len(sizes) // 2]
    cap = median_size * 1.6
    candidates = [c for c in candidates if c["first"]["size"] <= cap]
    if not candidates:
        candidates = [max(candidates, key=lambda c: c["first"]["size"])]

    kinds = {
        "OBJECTIVE": "summary", "SUMMARY": "summary", "PROFILE": "summary",
        "EDUCATION": "education",
        "EXPERIENCE": "experience", "WORK": "experience", "WORK EXPERIENCE": "experience",
        "SKILLS": "skills", "SKILLS / TOOLS": "skills", "SKILLS/TOOLS": "skills",
        "TECHNOLOGIES": "skills", "TECHNICAL SKILLS": "skills",
        "TECHNICAL SKILL": "skills", "PERSONAL SKILLS": "skills",
        "TOOLS USED": "skills", "TOOLS": "skills",
        "PROJECTS": "projects", "MAJOR PROJECT": "projects", "MINI PROJECT": "projects",
        "PERSONAL PROJECT": "projects",
        "ACHIEVEMENT": "awards", "AWARDS": "awards", "ACHIEVEMENTS": "awards",
        "COURSES": "education",
    }
    sections = []
    # Top -> down: higher y = closer to top.
    for c in sorted(candidates, key=lambda d: -d["y"]):
        key = c["text"].strip().upper()
        kind = kinds.get(key)
        sections.append({"name": c["text"], "order": len(sections), "kind": kind})
    return sections


def _detect_columns(records, width_pt: float) -> int:
    """Detect single- vs multi-column layout via horizontal glyph density.

    Scores the page at 2pt bins. If both the left half and the right half each
    contain a meaningful share of glyphs (roughly), it's two columns; otherwise
    it's one column. Tolerates asymmetric single-column layouts (e.g. name
    centered, contacts left) by requiring both halves to be substantive.
    """
    if not records:
        return 1
    mid = width_pt / 2
    left = sum(1 for r in records if r["x_center"] < mid)
    right = sum(1 for r in records if r["x_center"] >= mid)
    total = left + right or 1
    left_frac, right_frac = left / total, right / total
    # Two columns: both halves have a solid share of content.
    if left_frac >= 0.32 and right_frac >= 0.32:
        return 2
    # Three/four columns are rare for these resumes; keep it binary here.
    return 1


def _detect_bullets(records):
    """Detect the bullet glyph used to mark list items."""
    lines = _lines_of(records)
    bullets = Counter()
    for _, rows in lines:
        for row in rows:
            r = row[0]
            t = r["text"].lstrip()
            # a line starting with a bullet-like glyph and having body text after
            if not t:
                continue
            first = t[0]
            if first in "•·▪●◦-–":
                bullets[first] += 1
    if not bullets:
        # Fallback to common unicode bullet.
        return "•"
    return bullets.most_common(1)[0][0]


# --------------------------------------------------------------------------- #
# Template + CSS generation
# --------------------------------------------------------------------------- #
def _kind_to_section(kind: str | None) -> str | None:
    """Map a detected section kind to the renderer's template block (or None)."""
    return {"summary": "OBJECTIVE", "education": "EDUCATION",
            "experience": "EXPERIENCE", "skills": "SKILLS / TOOLS",
            "projects": "PROJECTS", "awards": "ACHIEVEMENT"}.get(kind)


def render_template_html(spec: dict) -> str:
    """Emit a Jinja2 skeleton in the detected section order, placeholder content only."""
    order = [s for s in spec["layout"]["sections"] if s["kind"]]
    kinds = [s["kind"] for s in order]
    blocks = {
        "summary": _BLOCKS["summary"],
        "education": _BLOCKS["education"],
        "experience": _BLOCKS["experience"],
        "skills": _BLOCKS["skills"],
        "projects": _BLOCKS["projects"],
        "awards": _BLOCKS["awards"],
    }
    out = _TEMPLATE_HEAD
    for k in kinds:
        if k in blocks:
            out += "\n" + blocks[k]
    out += "\n" + _TEMPLATE_TAIL
    return out


def render_styles_css(spec: dict) -> str:
    """Emit a CSS file capturing the detected page size, margins, fonts, sizes, colours."""
    pg = spec["page"]
    fonts = spec["typography"]
    colors = spec["colors"]
    fam = fonts["font_families"]
    primary_fam = list(fam)[0] if fam else "Times New Roman"
    size = _mode(Counter(spec["typography"]["sizes_used_pt"])) or fonts["body_size_pt"] or 10.9
    fg = colors["foreground"]
    accent = colors["accent"] or fg
    lines = []
    lines.append("/* AUTO-GENERATED by tools/scan.py — visual reference only. */")
    lines.append("@page {")
    lines.append(f"    size: {pg['width_pt']}pt {pg['height_pt']}pt;")
    lines.append(f"    margin: {pg['margins_pt']['top']}pt {pg['margins_pt']['right']}pt "
                 f"{pg['margins_pt']['bottom']}pt {pg['margins_pt']['left']}pt;")
    lines.append("}")
    lines.append("")
    lines.append("body {")
    lines.append(f"    font-family: '{primary_fam}', Georgia, serif;")
    lines.append(f"    font-size: {size}pt;")
    lines.append(f"    color: {fg};")
    lines.append("    margin: 0; padding: 0;")
    lines.append("}")
    lines.append("")
    if accent and accent.lower() not in (fg, "#fff", "#ffffff"):
        lines.append("")
        lines.append(f"/* accent color {accent} */")
        lines.append(".accent {")
        lines.append(f"    color: {accent};")
        lines.append("}")
    return "\n".join(lines)


# Inline template blocks (placeholder text only — never reference-scoped text).
_BLOCKS = {
    "summary": (
        '        <section class="section">\n'
        '            <div class="section-title">OBJECTIVE</div>\n'
        '            <div class="summary-text">Your professional summary goes here.</div>\n'
        '        </section>'
    ),
    "education": (
        '        <section class="section">\n'
        '            <div class="section-title">EDUCATION</div>\n'
        '            <div class="entry">\n'
        '                <div class="entry-header">\n'
        '                    <span class="institution">Institution Name</span>\n'
        '                    <span class="date">YYYY &ndash; YYYY</span>\n'
        '                </div>\n'
        '                <div class="entry-sub-header">\n'
        '                    <span class="degree">Degree</span>\n'
        '                </div>\n'
        '            </div>\n'
        '        </section>'
    ),
    "experience": (
        '        <section class="section">\n'
        '            <div class="section-title">EXPERIENCE</div>\n'
        '            <div class="entry">\n'
        '                <div class="entry-header">\n'
        '                    <span class="company">Company</span>\n'
        '                    <span class="date">YYYY &ndash; Present</span>\n'
        '                </div>\n'
        '                <div class="entry-sub-header">\n'
        '                    <span class="role">Role</span>\n'
        '                </div>\n'
        '                <ul class="bullet-points">\n'
        '                    <li>Verified accomplishment.</li>\n'
        '                    <li>Verified accomplishment.</li>\n'
        '                </ul>\n'
        '            </div>\n'
        '        </section>'
    ),
    "skills": (
        '        <section class="section">\n'
        '            <div class="section-title">SKILLS / TOOLS</div>\n'
        '            <div class="skills-grid">\n'
        '                <div class="skill-category"><strong>Category:</strong> skill, skill</div>\n'
        '            </div>\n'
        '        </section>'
    ),
    "projects": (
        '        <section class="section">\n'
        '            <div class="section-title">PROJECTS</div>\n'
        '            <div class="entry">\n'
        '                <div class="entry-header"><span class="project-title">Project</span></div>\n'
        '                <div class="entry-sub-header"><span class="project-meta">Tech</span></div>\n'
        '                <ul class="bullet-points"><li>Verified project detail.</li></ul>\n'
        '            </div>\n'
        '        </section>'
    ),
    "awards": (
        '        <section class="section">\n'
        '            <div class="section-title">ACHIEVEMENT</div>\n'
        '            <div class="achievement-text">Award &ndash; Issuer</div>\n'
        '        </section>'
    ),
}
_TEMPLATE_HEAD = '''<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Resume Template</title></head>
<body>
<div class="resume-container">
    <header>
        <div class="name">Your Name</div>
        <div class="contact-info">Location &middot; email@x.com &middot; GitHub</div>
    </header>
'''
_TEMPLATE_TAIL = '''    </div>
</body>
</html>
'''


# --------------------------------------------------------------------------- #
# Interactive preview (index.html + preview.js)
# --------------------------------------------------------------------------- #
def render_preview(spec: dict) -> tuple[str, str]:
    """Return (index.html, preview.js) for a self-contained editable preview."""
    pg = spec["page"]
    preview_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Preview: {spec['source_file']}</title>
<style>
  body {{ font-family: system-ui, sans-serif; margin: 24px; background: #fafafa; color: #222; }}
  .toolbar {{ margin-bottom: 16px; }}
  .toolbar button {{ padding: 6px 12px; margin-right: 8px; cursor: pointer; }}
  .stage {{ background: #fff; box-shadow: 0 1px 6px rgba(0,0,0,.15); margin: 0 auto; }}
  #page {{
    width: {pg['width_pt']}pt; height: {pg['height_pt']}pt;
    padding: {pg['margins_pt']['top']}pt {pg['margins_pt']['right']}pt
             {pg['margins_pt']['bottom']}pt {pg['margins_pt']['left']}pt;
    box-sizing: border-box;
  }}
  pre {{ background: #1e1e1e; color: #d6d6d6; padding: 12px; font-size: 11px; }}
</style>
</head>
<body>
<div class="toolbar">
  <button onclick="loadPlaceholder()">Reset to placeholder</button>
  <button onclick="render()">Re-render</button>
  <span style="color:#666">Page: {pg['page_size_name']} ({pg['width_pt']}x{pg['height_pt']}pt)
    · sections: {_section_labels(spec)}</span>
</div>
<div class="stage">
  <div id="page">{render_template_html(spec)}</div>
</div>
<h3>Source HTML (template.html)</h3>
<pre id="src"></pre>
<script>
{preview_js}
</script>
</body>
</html>
"""
    return preview_html, preview_js


preview_js = """
const PAGE = document.getElementById('page');
const SRC = document.getElementById('src');

function render() {
  SRC.textContent = PAGE.innerHTML;
}

function loadPlaceholder() {
  location.reload();
}

document.addEventListener('DOMContentLoaded', render);
render();
"""


# --------------------------------------------------------------------------- #
# Orchestration
# --------------------------------------------------------------------------- #
def _render_spec_md(spec: dict) -> str:
    """Render a human-readable spec.md for a format. Structure only.

    This describes the *visual* layout of a reference (page size, margins,
    fonts, sizes, colours, section order, bullets, columns). It NEVER contains
    any text from the reference resume — no names, dates, projects, contact
    info, or candidate facts. Candidate facts come solely from
    docs/candidate-profile.md.
    """
    pg = spec["page"]
    fonts = spec["typography"]
    colors = spec["colors"]
    layout = spec["layout"]
    line = []
    line.append(f"# Visual Spec — {spec['source_file']}")
    line.append("")
    line.append("> Auto-generated by tools/scan.py. Visual structure only — no candidate")
    line.append("> data. Facts come from docs/candidate-profile.md.")
    line.append("")
    line.append("## Page")
    line.append("")
    line.append(f"- Format: {spec['format_name']}")
    line.append(f"- Page size: {pg['page_size_name']} ({pg['width_pt']} x {pg['height_pt']} pt)")
    m = pg["margins_pt"]
    line.append(
        f"- Margins: top={m['top']}pt bottom={m['bottom']}pt "
        f"left={m['left']}pt right={m['right']}pt"
    )
    line.append(f"- Usable width: {pg['usable_width_pt']}pt")
    line.append("")
    line.append("## Typography")
    line.append("")
    line.append(f"- Dominant font: {fonts['dominant_font']}")
    line.append(f"- Body size: {fonts['body_size_pt']}pt")
    line.append(f"- Sizes used (pt): {', '.join(str(s) for s in fonts['sizes_used_pt'])}")
    fams = ", ".join(f"{name} (×{n})" for name, n in fonts["font_families"].items())
    line.append(f"- Fonts present: {fams}")
    line.append("")
    line.append("## Colour")
    line.append("")
    line.append(f"- Foreground: {colors['foreground']}")
    line.append(f"- Accent: {colors['accent'] or 'none (black only)'}")
    line.append("")
    line.append("## Layout")
    line.append("")
    line.append(f"- Columns: {layout['columns']}")
    line.append(f"- Bullet glyph: {layout['bullet_char']!r}")
    line.append("")
    line.append("### Sections (top → bottom)")
    line.append("")
    for s in layout["sections"]:
        kind = s.get("kind") or "unknown"
        line.append(f"{s['order']}. `{s['name']}` → {kind}")
    if not layout["sections"]:
        line.append("_no sections detected_")
    line.append("")
    line.append("### Renderer inputs")
    line.append("")
    line.append("Use these files to render a resume in this format:")
    line.append("")
    line.append("```")
    line.append("references/<name>/template.html   # Jinja2 section skeleton")
    line.append("references/<name>/styles.css      # page size, margins, fonts, sizes, colours")
    line.append("")
    line.append("Render with:")
    line.append('python3 engine/main.py --json <manifest.json> --format "<name>"')
    line.append("```")
    line.append("")
    return "\n".join(line)


def write_format_folder(spec: dict, out_dir: str) -> dict:
    """Write spec.json + template.html + styles.css + preview artifacts for one format."""
    folder = os.path.join(out_dir, spec["format_name"])
    os.makedirs(folder, exist_ok=True)

    # spec.json: machine-readable extracted reference (trim human diagnostics).
    clean = {k: v for k, v in spec.items() if k != "_report"}
    with open(os.path.join(folder, "spec.json"), "w") as f:
        json.dump(clean, f, indent=2)

    # spec.md: human-readable visual spec (structure only, no candidate data).
    with open(os.path.join(folder, "spec.md"), "w") as f:
        f.write(_render_spec_md(spec))

    with open(os.path.join(folder, "template.html"), "w") as f:
        f.write(render_template_html(spec))

    with open(os.path.join(folder, "styles.css"), "w") as f:
        f.write(render_styles_css(spec))

    index_html, preview_js = render_preview(spec)
    with open(os.path.join(folder, "index.html"), "w") as f:
        f.write(index_html)
    with open(os.path.join(folder, "preview.js"), "w") as f:
        f.write(preview_js)

    return {"folder": folder, "format_name": spec["format_name"]}


def scan_many(pdf_paths, out_dir: str):
    results = []
    for path in pdf_paths:
        fmt = os.path.splitext(os.path.basename(path))[0]
        spec = scan_pdf(path)
        spec["format_name"] = fmt
        print(f"\n=== {path} ===")
        _print_report(spec)
        res = write_format_folder(spec, out_dir)
        results.append(res)
        print(f"  -> {res['folder']}")
    return results


def _section_labels(spec: dict) -> str:
    secs = spec["layout"]["sections"]
    if not secs:
        return "(none)"
    return ", ".join(f"{s['name']}({s['kind']})" for s in secs)


def _print_report(spec: dict):
    pg = spec["page"]
    print(f"  Page size : {pg['page_size_name']}  ({pg['width_pt']} x {pg['height_pt']} pt)")
    m = pg["margins_pt"]
    print(f"  Margins   : top={m['top']} bottom={m['bottom']} left={m['left']} right={m['right']}")
    print(f"  Dominant  : {spec['typography']['dominant_font']}  (body ~{spec['typography']['body_size_pt']}pt)")
    print(f"  Colours   : fg={spec['colors']['foreground']}  accent={spec['colors']['accent']}")
    print(f"  Sections  : {_section_labels(spec)}")
    print(f"  Bullet    : {spec['layout']['bullet_char']!r}")
    print(f"  Columns   : {spec['layout']['columns']}")


def main():
    ap = argparse.ArgumentParser(description="Scan reference resume PDFs for visual structure")
    ap.add_argument("path", nargs="?", help="Path to a reference PDF.")
    ap.add_argument("--dir", help="Directory to scan for *.pdf (mutually exclusive with path).")
    ap.add_argument("--out", default="references", help="Output dir for format folders.")
    ap.add_argument("--name", help="Format name (default: PDF stem).")
    args = ap.parse_args()

    if not args.path and not args.dir:
        ap.error("Provide a PDF path or --dir.")

    if args.dir:
        pdfs = sorted(
            os.path.join(args.dir, f)
            for f in os.listdir(args.dir)
            if f.lower().endswith(".pdf")
        )
    else:
        pdfs = [args.path]

    if not pdfs:
        print("No PDFs found; nothing to scan.")
        return

    results = scan_many(pdfs, args.out)
    print(f"\nScanned {len(results)} reference PDF(s).")


if __name__ == "__main__":
    main()
