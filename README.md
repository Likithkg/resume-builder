# SDE Resume Builder

A truthful, ATS-friendly resume builder for Software Development Engineers. It turns a **candidate profile** and a **target job description** into a single, one-page PDF and DOCX that matches a locked LaTeX-style reference template — without inventing any facts.

The system is split into two halves:

- **A multi-model reasoning pipeline** (runs inside the Claude Code terminal). The main agent orchestrates four specialist sub-agents — analysis, mapping, content, and an ATS reviewer — each of which can think under a different Claude model and give feedback to the others.
- **A deterministic renderer** (plain Python). Once the reasoning is done, a single writer converts the resulting Content Manifest into the PDF and DOCX artifacts. No model, no guessing, no font drift.

---

## Architecture

```
┌───────────────────────────────────────────────────────────────────────┐
│  Claude Code main agent (SKILL.md)  — orchestrates the pipeline         │
│                                                                        │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│   │  analysis│─▶│  mapping │─▶│  content │─▶│    ats   │  feedback     │
│   │  (A/B/C/D)│  │  A>B>C   │  │  manifest │  │  review  │◀── loops back │
│   └──────────┘  └──────────┘  └──────────┘  └──────────┘   to content  │
│                    ▲                                   │                │
│                    └───────────  content re-run ────────┘                │
│                                                                        │
│   ┌───────────────┐   ┌───────────────────────────────────────────┐    │
│   │  compress     │──▶│  renderer/  (main.py → render_pdf.py)       │    │
│   │  (one page)   │   │   validate.py → output/*.pdf  + *.docx      │    │
│   └───────────────┘   └───────────────────────────────────────────┘    │
└───────────────────────────────────────────────────────────────────────┘
```

**Why sub-agents per stage?** Each stage has a different kind of thinking. Analysis (classifying requirements), mapping (matching evidence with an A > B > C priority), and content (writing truthful bullets) are judgment-heavy and want a strong model. The ATS reviewer is a check-and-feedback loop. The renderer is pure Python and never needs a model at all. The main agent picks the model per stage from whatever you set in the terminal.

**Why a separate renderer?** Presentation must be 100% reproducible. The model produces *content only*; the renderer owns the visual template, page geometry, and fonts. If the model hallucinates a font change, it never reaches the PDF.

---

## The pipeline

The main agent runs five stages in order, with one feedback loop:

| Stage | Sub-agent | Does | Output |
|------|-----------|------|--------|
| 1 | **analysis** | Parses the JD, classifies each requirement A (strong match) / B (adjacent) / C (project-only) / D (missing) | Requirement Matrix |
| 2 | **mapping** | Maps A/B/C requirements to the strongest verified profile evidence | Evidence Map |
| 3 | **content** | Builds the Content Manifest (objective, education, experience, skills, projects, achievement) | Content Manifest |
| 4 | **ATS review** | Scores the manifest against the JD and feeds suggestions back | Hit / miss + score |
| 5 | **compress** | Fits the manifest to exactly one page without touching the template | Compressed Manifest |

The **ATS review** stage is a reviewer, not a gate — if it rejects (JD-only violation, score < 60, or drift in positioning), the main agent re-runs *content* (then the ATS review again) before compressing.

---

## How to use it

There are two ways to run this. Both produce the same `output/<name>_Resume.pdf` and `output/<name>_Resume.docx`.

### 1. Inside the Claude Code terminal (recommended)

Invoke the skill with a candidate profile and a job description:

```
/sde-resume-builder "Profile: [path/to/profile.json], JD: [paste the JD text here]"
```

The main agent orchestrates the sub-agents, runs the ATS feedback loop, and finally calls the renderer to produce the artifacts. It reports the absolute output paths when done.

- The model each stage runs under is **whatever you selected in the terminal**. To pin a single model for a run, export `SDE_RESUME_MODEL` before invoking.
- Every sub-agent is **read-only** — it returns structured JSON, writes nothing. Only the renderer writes files.

### 2. Standalone, with the renderer directly

If you already have a Content Manifest (or want to render a test one), run the deterministic renderer:

```bash
pip install weasyprint python-docx jinja2
python3 .claude/skills/sde-resume-builder/engine/main.py \
    --json .claude/skills/sde-resume-builder/data/test_manifest.json \
    --out output
```

Artifacts land in `output/`. The manifest schema is:

```json
{
  "header":        { "name", "email", "phone", "location", "github", "linkedin", "summary", ... },
  "education":     [{ "institution", "start_date", "end_date", "degree", "location", ... }],
  "experience":    [{ "company", "start_date", "end_date", "role", "location", "bullet_points": [...] }],
  "skills":        { "Languages": [...], "Backend": [...], ... },
  "projects":      [{ "name", "technologies": [...], "bullet_points": [...] }],
  "awards":        [{ "title", "issuer", ... }]
}
```

The `summary` field becomes the resume's OBJECTIVE; `awards` becomes the ACHIEVEMENT section.

---

## Reference formats (the template you render in)

Each reference PDF maps to a **format** — its own visual template under `references/<name>/`.
You pick which format to render in when the skill starts:

```
references/<name>/
├── spec.md          # human-readable visual spec (structure only — no candidate data)
├── spec.json        # machine-readable spec (validation source)
├── template.html    # Jinja2 section skeleton
├── styles.css       # page size, margins, fonts, sizes, colours
├── index.html       # interactive preview
└── preview.js       # preview behaviour
```

1. **Choose** a format (list `references/` and read each `spec.md` header — page size, section
   order — so you can pick).
2. **Reuse if present.** If `references/<name>/spec.md` exists, the format is ready — proceed.
3. **Build if missing.** If `spec.md` is absent, generate the format folder first:

   ```bash
   python3 tools/scan.py --dir references --out references
   ```

   `tools/scan.py` scans the reference PDF **word by word** (via PyMuPDF) and emits only the
   *visual* structure — page geometry, margins, fonts, sizes, colours, section order, bullets.
   It **never** copies any text content (names, dates, projects, contact info) from a reference.
   Candidate facts come solely from `docs/candidate-profile.md`.

The chosen format name is used only at render time: `engine/main.py --format "<name>"`.

> The reference PDFs under `references/` are **visual guidance only**. Their content is never
> transferred into a resume.

---

## What you need

- **Python 3.10+**
- **Python packages:** `weasyprint`, `python-docx`, `jinja2`, `pymupdf`
  ```bash
  pip install -r requirements.txt
  ```
- **Computer Modern fonts** (optional but recommended) — install the `cm-super` / `texlive-fonts-recommended` package family so the PDF uses the reference font family instead of a Times New Roman fallback.

### Inputs

- **Candidate Profile** — JSON (or a path to one) with the candidate's full history. Schema in `data/candidate-schema.json`.
- **Job Description** — the text of the target role you are tailoring for.

---

## The source of truth

The pipeline reads four **read-only** documents from `docs/`. No stage is permitted to edit them; they are inputs, not a drafting canvas.

| File | Role |
|------|------|
| `docs/candidate-profile.md` | **Authoritative candidate facts.** The only source for who the candidate is. |
| `docs/career-positioning.md` | How to position and emphasize the candidate's story. |
| `docs/resume-guidelines.md` | Writing & ATS rules (bullet formula, verbs, missing-skill handling). |
| `docs/resume-template.md` | The locked one-page visual template contract. |

`references/` holds reference resumes for **visual guidance only** — their names, dates, and projects are never transferred.

---

## Hard constraints

The builder is constrained by design, not by preference:

- **Truthfulness is non-negotiable.** A JD is *relevance*, never *facts*. A technology listed in a JD is not evidence the candidate has it. Unsupported claims are dropped, never invented.
- **Exactly one page**, US Letter (612 × 792 pt). If content overflows, the *content* is compressed — the template is never reshaped.
- **Locked layout.** One section order (OBJECTIVE → EDUCATION → EXPERIENCE → SKILLS → PROJECTS → ACHIEVEMENT), Computer Modern typography, monochrome, no colors, icons, or columns.
- **SDE-first positioning.** The candidate is read as a software engineer — not an ML/Data/DevOps/Cloud title — even when the JD pulls the other way.

`renderer/validate.py` enforces these automatically on every run.

---

## Project layout

```
resume-builder/
├── README.md
├── requirements.txt                 # Python dependencies
├── references/                      # reference resumes (visual guidance only; *.pdf kept as source)
├── tools/                           # reference scanner (tools/scan.py → generates formats/)
├── output/                          # generated artifacts (PDF + DOCX)
├── .trash/                          # removed files (safe to delete)
└── .claude/skills/sde-resume-builder/
    ├── SKILL.md                     # main-agent orchestration (entrypoint)
    ├── USER_GUIDE.md                # how a user provides inputs
    ├── engine/                      # orchestrator logic (no model calls)
    │   ├── main.py                  # renderer entrypoint
    │   ├── model_router.py          # stage list, effort, model resolver, prompt loader
    │   ├── auth_manifest.py         # read-only sub-agent contract
    │   └── pipeline_prompts.py      # per-stage system prompts
    ├── renderer/                    # deterministic rendering (no model calls)
    │   ├── render_pdf.py            # PDF + DOCX writers (single canonical writer)
    │   ├── template.html            # locked visual authority
    │   ├── styles.css               # locked visual authority
    │   └── validate.py              # artifact QA
    ├── docs/                        # read-only source of truth
    │   ├── candidate-profile.md
    │   ├── career-positioning.md
    │   ├── resume-guidelines.md
    │   └── resume-template.md
    └── data/                        # input data / test manifest
        ├── candidate-schema.json
        └── test_manifest.json
```

> The generated folders under `references/<name>/` (spec.json, template.html, styles.css, …) are
> build outputs of `tools/scan.py` and are git-ignored. The `references/*.pdf` remain the source
> of truth. Run `python3 tools/scan.py --dir references --out references` to regenerate them.

---

## Quick start

```bash
# Install dependencies
pip install weasyprint python-docx jinja2

# Render the bundled test manifest
python3 .claude/skills/sde-resume-builder/engine/main.py \
    --json .claude/skills/sde-resume-builder/data/test_manifest.json \
    --out output

# Open the results
xdg-open output/Likith_K_G_Resume.pdf
```
