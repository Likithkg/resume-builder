"""
PDF + DOCX renderers.

The PDF path populates the locked template.html/styles.css. The DOCX path mirrors the
verified output/Likith_Resume.docx layout (⋄ contacts, · bullets, 5-section loop).
This module is the single canonical writer for both artifacts.
"""
import logging
from typing import Any, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from weasyprint import HTML
    WEASYPRINT_AVAILABLE = True
except ImportError:
    WEASYPRINT_AVAILABLE = False

try:
    from docx import Document
    from docx.shared import Pt
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False


def inject_css(html_content: str, css_content: str) -> str:
    """Inject <style> into <head> (WeasyPrint needs the CSS inline)."""
    if "</head>" in html_content:
        return html_content.replace("</head>", f"<style>{css_content}</style></head>")
    return f"<style>{css_content}</style>" + html_content


def render_to_pdf(html_content: str, output_path: str):
    """Render HTML content to a PDF using WeasyPrint."""
    if not WEASYPRINT_AVAILABLE:
        logger.error("WeasyPrint is not installed. Install via 'pip install weasyprint'.")
        raise ImportError("WeasyPrint dependency missing. PDF rendering cannot proceed.")
    try:
        HTML(string=html_content).write_pdf(output_path)
        logger.info(f"Successfully rendered PDF to {output_path}")
    except Exception as e:
        logger.error(f"Failed to render PDF: {e}")
        raise


# --- DOCX ------------------------------------------------------------------

# DOCX section order: (display title, json key). Mirrors the proven reference layout.
_SECTIONS = [
    ("EDUCATION", "education"),
    ("EXPERIENCE", "experience"),
    ("SKILLS / TOOLS", "skills"),
    ("PROJECTS", "projects"),
    ("ACHIEVEMENT", "awards"),
]
_FONT = 10.9
_LINE_HEIGHT = 13.5  # Locked line height from resume-template.md. Compact spacing keeps the DOCX
                     # dense enough to match the PDF's single-page layout.
_CONTACT_SEP = " ⋄ "


def _compact(doc, para):
    """Collapse paragraph spacing and pin line height to the locked 13.5pt (template-faithful)."""
    para.paragraph_format.space_before = Pt(0)
    para.paragraph_format.space_after = Pt(0)
    # Pin line height to the locked 13.5pt template value (13.5 / _FONT as an em multiple,
    # since python-docx treats a float line_spacing as a multiple of the font height).
    para.paragraph_format.line_spacing = _LINE_HEIGHT / _FONT
    return para


def _docx_contacts(header, sep=_CONTACT_SEP):
    parts = []
    if header.get("location"):
        parts.append(header["location"])
    if header.get("phone"):
        parts.append(header["phone"])
    if header.get("email"):
        parts.append(header["email"])
    if header.get("github"):
        parts.append("GitHub")
    if header.get("linkedin"):
        parts.append("LinkedIn")
    return sep.join(parts)


def _docx_entry_header(doc, left, right):
    p = doc.add_paragraph()
    run = p.add_run(left)
    run.bold = True
    run.font.size = Pt(_FONT)
    if right:
        sep = p.add_run("\t" * 10)
        sep.font.size = Pt(_FONT)
        p.add_run(right)
    return p


def _docx_bullet(doc, text):
    bp = doc.add_paragraph(f"· {text}", style="List Bullet")
    bp.paragraph_format.space_after = Pt(0)
    bp.paragraph_format.space_before = Pt(0)
    bp.runs[0].font.size = Pt(_FONT)


def render_to_docx(data: Dict[str, Any], output_path: str):
    """Render structured resume data to a DOCX, matching the verified reference layout."""
    if not DOCX_AVAILABLE:
        logger.error("python-docx is not installed. Install via 'pip install python-docx'.")
        raise ImportError("python-docx dependency missing. DOCX rendering cannot proceed.")

    doc = Document()
    # Match the locked template's margins (28.8pt all around); the PDF writer uses the same
    # value via @page in styles.css. A larger bottom margin (e.g. 36pt) forces the trailing
    # ACHIEVEMENT onto a second page.
    for section in doc.sections:
        section.top_margin = Pt(28.8)
        section.bottom_margin = Pt(28.8)
        section.left_margin = Pt(28.8)
        section.right_margin = Pt(28.8)

    header = data["header"]

    name_p = doc.add_paragraph()
    _compact(doc, name_p)
    name_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = name_p.add_run(header.get("name", "Your Name"))
    run.bold = True
    run.font.size = Pt(20.7)

    contact_p = doc.add_paragraph(_docx_contacts(header))
    _compact(doc, contact_p)
    contact_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    contact_p.runs[0].font.size = Pt(_FONT)

    summary = header.get("summary")
    if summary:
        sp = doc.add_paragraph(summary)
        _compact(doc, sp)
        sp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        sp.runs[0].font.size = Pt(_FONT)

    for title, key in _SECTIONS:
        h = doc.add_paragraph()
        _compact(doc, h)
        r = h.add_run(title)
        r.bold = True
        r.font.size = Pt(_FONT)
        rule = doc.add_paragraph("_" * 80)
        _compact(doc, rule)

        items = data.get(key, [])
        if key == "education":
            for edu in items:
                eh = _docx_entry_header(doc, edu.get("institution", ""),
                                   f"{edu.get('start_date', '')} - {edu.get('end_date', '')}")
                _compact(doc, eh)
                sub = doc.add_paragraph(f"{edu.get('degree', '')} | {edu.get('location', '')}")
                _compact(doc, sub)
                sub.runs[0].font.italic = True
                sub.runs[0].font.size = Pt(_FONT)
        elif key == "experience":
            for exp in items:
                _docx_entry_header(doc, exp.get("company", ""),
                                   f"{exp.get('start_date', '')} - {exp.get('end_date', '')}")
                role = doc.add_paragraph(f"{exp.get('role', '')} | {exp.get('location', '')}")
                _compact(doc, role)
                role.runs[0].font.italic = True
                role.runs[0].font.size = Pt(_FONT)
                for bullet in exp.get("bullet_points", []):
                    _docx_bullet(doc, bullet)
        elif key == "skills":
            for category, skill_list in items.items():
                p = doc.add_paragraph()
                _compact(doc, p)
                c = p.add_run(f"{category}: ")
                c.bold = True
                c.font.size = Pt(_FONT)
                p.add_run(", ".join(skill_list))
                p.runs[-1].font.size = Pt(_FONT)
        elif key == "projects":
            for proj in items:
                doc.add_paragraph()
                p = doc.add_paragraph()
                _compact(doc, p)
                pt = p.add_run(proj.get("name", ""))
                pt.bold = True
                tech = proj.get("technologies", [])
                if tech:
                    meta = doc.add_paragraph(f"  ({', '.join(tech)})")
                    _compact(doc, meta)
                    meta.runs[0].font.italic = True
                    meta.runs[0].font.size = Pt(_FONT)
                for bullet in proj.get("bullet_points", []):
                    _docx_bullet(doc, bullet)
        elif key == "awards":
            for award in items:
                p = doc.add_paragraph(f"{award.get('title', '')} - {award.get('issuer', '')}")
                _compact(doc, p)
                p.runs[0].font.size = Pt(_FONT)

    doc.save(output_path)
    logger.info(f"Successfully rendered DOCX to {output_path}")
