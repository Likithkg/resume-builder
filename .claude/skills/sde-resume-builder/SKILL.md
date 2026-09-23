---
name: sde-resume-builder
description: Generate truthful, ATS-friendly SDE resumes tailored to a target job description using a provided candidate profile and a fixed reference-resume format. Multi-model: each pipeline stage runs under a dedicated sub-agent.
---

# SDE Resume Builder (General)

## 0. Directory layout

The skill is organized in three layers. You run from the skill root
(`.claude/skills/sde-resume-builder/`) and refer to files by their new location.

```
.
├── SKILL.md                     # this entrypoint
├── USER_GUIDE.md
├── engine/                      # main agent + orchestrator logic (no model calls)
│   ├── main.py                  # deterministic renderer entrypoint
│   ├── model_router.py          # stage list, effort, model resolver, prompt loader
│   ├── auth_manifest.py         # read-only sub-agent contract
│   └── pipeline_prompts.py      # per-stage system prompts
├── renderer/                    # deterministic rendering (no model calls)
│   ├── render_pdf.py            # PDF + DOCX writers (single canonical writer)
│   ├── template.html            # locked visual authority
│   ├── styles.css               # locked visual authority
│   └── validate.py              # artifact QA
├── docs/                        # read-only source of truth (never edit)
│   ├── candidate-profile.md     # AUTHORITATIVE facts
│   ├── career-positioning.md    # positioning / emphasis
│   ├── resume-guidelines.md     # writing & ATS rules
│   └── resume-template.md       # one-page / visual template contract
├── data/                        # input data / test manifests
│   ├── candidate-schema.json
│   └── test_manifest.json
└── references/                  # reference resumes (visual reference only)
    └── *.pdf
```

## 1. Who you are (the orchestrator)

You are the **orchestrator** of a resume-generation pipeline. You do **not** do the heavy
reasoning yourself. You **delegate each pipeline stage to a separate sub-agent** via the
`Agent` tool and you **control the flow**: run stages in order, let the ATS reviewer feed back
into the content stage, and re-run until the resume passes.

Control flow is yours. Sub-agents only think and return structured JSON; they never render
artifacts. Rendering is deterministic Python, done once at the end.

### Delegation contract (every sub-agent)

For **each** stage below, call `Agent` with these inputs:

- `system`: the exact stage prompt from `pipeline_prompts.py` — read the prompt the stage needs
  with `model_router.prompt_for("<stage>")`.
- `effort`: `model_router.effort_for("<stage>")`.
- instruct the sub-agent to **return ONLY JSON**, to be **read-only** (no file writes), and to
  **never invent facts**.

The model that runs each sub-agent is whatever you (the user) selected in the terminal — this
skill does **not** force or pin a model. To pin a single model for a run, set the
`SDE_RESUME_MODEL` env var; otherwise the session model is used for every stage.

```python
import model_router
prompt = model_router.prompt_for("analysis")
out = Agent(system=prompt, effort=model_router.effort_for("analysis"))
```

### Sources of truth (read-only inputs)

- `docs/candidate-profile.md` — **authoritative facts**. Never rewrite, never infer.
- `docs/career-positioning.md` — positioning / emphasis strategy.
- `docs/resume-guidelines.md` — writing & ATS rules.
- `docs/resume-template.md` — one-page / visual template contract.

No stage may edit these files.

---

## 2. Inputs

- **Candidate Profile** — JSON object or file path with the candidate's full history.
- **Job Description (JD)** — text of the target role.

---

## 3. Reference format selection

Before running the pipeline you must pick the **reference format** the final resume will be
rendered in. The format is a per-reference "template" captured under
`references/<name>/`:

```
references/<name>/
├── spec.md          # human-readable visual spec (structure only, no candidate data)
├── spec.json        # machine-readable spec (validation source)
├── template.html    # Jinja2 section skeleton
├── styles.css       # page size, margins, fonts, sizes, colours
├── index.html       # interactive preview
└── preview.js       # preview behaviour
```

1. **Ask which reference format** to render in. Present the available formats by listing
   `references/` and showing each folder's `spec.md` header (page size, page-size name,
   section order) so the user can choose. The `<name>` is the folder name (it may contain
   spaces or parentheses, e.g. `Likith_SDE_Resume (2)`).
2. **Reuse if present.** If `references/<name>/spec.md` exists, the format is ready —
   proceed to the pipeline. Pass `--format "<name>"` to `engine/main.py` at render time.
3. **Build if missing.** If `spec.md` is absent, generate the format folder first:

   ```bash
   python3 tools/scan.py --dir references --out references
   ```

   `scan.py` scans the reference PDF word-by-word via PyMuPDF and emits
   `references/<name>/{spec.md, spec.json, template.html, styles.css, index.html, preview.js}`
   — visual structure only. It never emits candidate data (no names, dates, projects, or
   contact info). Candidate facts come solely from `docs/candidate-profile.md`.

   > The reference PDFs under `references/` are **visual guidance only**. `scan.py` extracts
   > layout only — it must not copy any text content from a reference into a resume.

4. **Rebuild (optional).** Re-running `scan.py` overwrites the format folder. Only do this
   if you intentionally change a reference; otherwise reuse the existing `spec.md`.

Pick the format, then continue to **§4 The Pipeline**. The chosen format name is used only at
render time (`engine/main.py --format "<name>"`); the thinking pipeline does not need to know it.

---

## 4. The Pipeline

Run the four thinking stages. The `ats` stage is a **reviewer** that can send feedback back to the
`content` stage — that is the "all agents communicate" loop.

### Stage 1 — Analysis  → `analysis`
Read the JD, classify each requirement A/B/C/D → **Requirement Matrix**. `D` classes must never
appear in later output.

### Stage 2 — Mapping  → `mapping`
Map A/B/C terms to the strongest verified evidence; drop unsupported claims.

### Stage 3 — Content  → `content`
Produce the **Content Manifest** (objective/education/experience/skills/projects/achievement).
Truthful, ownership-calibrated verbs, JD-relevant emphasis, no invented facts.

### Stage 4 — ATS review  → `ats`
Score the manifest against the JD and return hit/miss + suggestions. This is a **feedback** step:
the main agent reads its verdict and, if it rejects, re-runs `content` (then `ats` again) before
compressing. Reject if: any `jd_only_violation`, score < 60, or `positioning_ok=false`.

```
content → ats → (reject) → content → ats → (pass)
```

### Stage 5 — Compress  → `compress`
If the manifest would overflow one page, compress by removing/shortening content **only** — never
by touching fonts, margins, or section order.

### Stage 6 — Validate  → `qa`
Run `renderer/validate.py`. The skill is NOT complete until QA passes.

---

## 5. Per-stage prompts

The exact system prompt for each sub-agent lives in `pipeline_prompts.py` (`STAGE_PROMPTS[stage]`).
`model_router.prompt_for(stage)` returns it. The prompts embed the source hierarchy, the JD
firewall, the one-page compression order, and the QA rejection rules so each sub-agent stays
scoped and read-only.

---

## 6. Core constraints

### Truthfulness & authority
- **Candidate Profile** is the absolute factual authority.
- **JD Firewall**: the JD controls relevance/emphasis, NEVER facts. A JD technology is not
  evidence the candidate has it.
- No hallucinations: never infer production scale, leadership, ownership, or unverified tech.
- `NEEDS VERIFICATION` items are **not** resume content unless the candidate later verifies them.

### Visual fidelity & one-page limit
- **Hard template**: `docs/resume-template.md`. Do not redesign.
- The final output must be exactly **one** US Letter page.
- If content overflows, compress in order: (1) remove redundant wording, (2) shorten bullets,
  (3) remove lower-priority projects/skills, (4) omit nonessential achievements.
  *Never* solve overflow by changing fonts, margins, spacing, or adding a second page.

### Experience coverage
Professional experience takes priority over projects when allocating the single page. This is a
**coverage** rule, not a stylistic preference.

- Give **professional experience** priority over projects for page space.
- For ~**2+ years** of professional experience, do **not** aggressively compress the Experience
  section merely to make room for projects.
- When enough verified evidence exists, target ~**4–5 strong experience bullets**.
- Select bullets by **relevance to the target JD**, not by brevity alone.
- **Preserve distinct engineering dimensions** when the verified evidence supports each one:
  - backend / microservices development
  - data processing and ingestion
  - concrete performance / workflow optimization
  - processing state / deduplication / reliability
  - incident investigation / automation
  - LLM / AI skill or workflow engineering
- **Do not** merge several distinct engineering contributions into one vague bullet just to cut the
  bullet count. Each separate evidence area stays a separate bullet when relevant to the target JD.

#### One-page compression order (experience-first)
When the manifest overflows one page, compress in this priority:

**FIRST (preserve):**
- preserve professional-experience bullets
- preserve concrete engineering evidence
- preserve quantified, verified technical constraints/results

**THEN (compress):**
- compress objective wording
- compress skill descriptions
- reduce lower-priority project bullets
- reduce secondary project content
- compress achievements

*Never* remove a meaningful professional-experience bullet simply to preserve a project bullet.

#### Current candidate — verified experience evidence (for reference)
These verified areas should generally remain **separate bullets** when relevant to the target JD:
- Python/Flask and Node.js microservices processing Avro/Parquet data
- PyArrow/fastavro chunked & asynchronous processing and batch ingestion for the 2–3 GB workflow
- persisted processing state across overlapping polling windows
- incident-investigation workflows using tools, endpoint queries, LLM agents, and structured TSV normalization
- converting infrastructure troubleshooting SOPs into structured AI skill instructions, tested/refined against incidents

> These are reminders of **verified** evidence only — do not invent additional metrics, ownership,
> technologies, deployment scope, business impact, or responsibilities. Unsupported facts stay out.

---

## 7. Rendering (deterministic, by you)

The renderer lives in `renderer/`:
- `template.html` & `styles.css` — locked visual authority.
- `render_pdf.py` — PDF + DOCX writers (single canonical writer).
- `validate.py` — artifact QA (one page, no placeholders, section order).

Rendering is **not** a stage; it is a separate deterministic step you perform once QA passes.

### Run it
The Content Manifest is Stage 5 output (JSON). Render the artifacts:

```bash
python3 main.py --json <content_manifest.json> --out ./output
```

Artifacts are written to `output/<name>_Resume.pdf` and `output/<name>_Resume.docx`.

> If you are running this outside a Claude Code terminal, pass the manifest you produced. Inside
> the terminal, the main agent produces the manifest by orchestrating the sub-agents in §2, then
> invokes `main.py` to render it.

### Execution rule
The skill is complete **only when the PDF and DOCX are generated and verified**. You must provide
the absolute output paths. Printing text is not sufficient.

---

## 8. Reference documents
- Writing & ATS rules: `docs/resume-guidelines.md`
- Visual specification: `docs/resume-template.md`
- Positioning framework: `docs/career-positioning.md`
- Candidate facts: `docs/candidate-profile.md`

---

## 9. Auth guide for sub-agents
Sub-agents run inside your context, so keep each sub-agent **read-only** and return JSON only
(see `auth_manifest.py`: every stage is read-only; only you, the orchestrator, render artifacts).

The pipeline runs in dependency order, and the main agent may re-run earlier stages when the ATS
reviewer feeds back into the content stage:

```
analysis → mapping → content → ats → compress
                        ^_________|
            (ats rejects) → re-run content, then ats again
```
