"""
Auth guide for the multi-model resume pipeline.

Sub-agents act inside the orchestrator's (main agent's) context, so a sub-agent can perform
actions the user would otherwise have to approve. The safest design is a sub-agent that cannot
write anything: it only reads source data and returns a structured result. This module records
that contract so the main agent and any reviewer can audit what each sub-agent may do.

Rules (also enforced by settings.local.json via Read-only permissions):
  * Each stage sub-agent is READ-ONLY: no file creation/deletion, no side-effecting commands.
    It returns structured results only.
  * The main agent (the orchestrator) is the only component that writes files, and only by
    invoking the deterministic renderer (main.py -> render_pdf.py). Sub-agents never render.
  * No sub-agent may fabricate candidate facts. Unsupported claims are rejected by the QA gate.

The per-stage MODEL is intentionally NOT here: the pipeline runs through your Claude Code
terminal, so the model that runs every stage is whatever you selected in the terminal. See
model_router.py (the router does not hardcode a model per stage).

The pipeline runs in dependency order, and the main agent may re-run earlier stages when the
ATS reviewer feeds back into the content stage:

    analysis -> mapping -> content -> ats -> compress
                                  ^_________|
        (ats rejects)  ->  re-run content, then ats again

Stage roles (non-model; per-stage effort lives in model_router.py):
"""
from __future__ import annotations

STAGE_SCOPE = {
    "analysis": "Read the target JD only. Emit the A/B/C/D Requirement Matrix. No file writes.",
    "mapping": "Read the JD matrix + candidate-profile.md. Emit the verified evidence map. No file writes.",
    "content": "Read verified evidence + positioning rules. Emit the Content Manifest. No file writes.",
    "ats": "Read the manifest + JD. Score it and return hit/miss + suggestions. No file writes.",
    "compress": "Read the manifest + template compression rules. Emit a one-page-compressed manifest. No file writes.",
}

AUTH_MANIFEST = {
    "subject": "SDE resume builder multi-model pipeline",
    "permission_model": "Every stage sub-agent is READ-ONLY. Only the orchestrator writes files (rendering).",
    "read_only": {stage: True for stage in STAGE_SCOPE},
    "stage_scope": STAGE_SCOPE,
    "model_policy": "The model is whatever the Claude Code terminal is set to; no per-stage hardcoding.",
    "feedback_flow": "ats may reject and send feedback back to content, which then re-runs before compress.",
    "hard_rules": [
        "No stage may fabricate candidate facts, dates, titles, metrics, or technologies.",
        "A technology in the JD is never evidence of candidate experience.",
        "Unsupported claims are rejected by the QA gate and cause that stage to re-run.",
        "Only the orchestrator renders artifacts; sub-agents never write files.",
        "ATS review is a feedback loop, not a hard gate the model cannot see.",
    ],
}
