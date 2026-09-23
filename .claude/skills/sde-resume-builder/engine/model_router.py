"""
Model + effort router for the multi-model SDE resume pipeline.

IMPORTANT: this router does NOT assign a Claude model to each stage. The pipeline runs through
your Claude Code terminal, which already has a model loaded — that model runs every stage. We
intentionally avoid hardcoding per-stage models, because:

  * The pipeline is orchestrated by the Claude Code main agent (see SKILL.md), not by this Python
    module. The main agent delegates each stage to a sub-agent that inherits the session's model.
  * Hardcoding e.g. "analysis -> opus" would (a) ignore the model you actually picked, and
    (b) fight the terminal's settings.

So this module provides only: the ordered stage list, each stage's role/focus (for SKILL.md),
optional per-stage *effort* defaults (overridable), and a model resolver that defaults to
"inherit the session model" (None) unless you pin one via SDE_RESUME_MODEL.
"""
from __future__ import annotations

import os
import sys

# Ordered pipeline. New stages (e.g. ats) are inserted in the correct dependency order here and
# get a matching prompt in pipeline_prompts.py.
STAGE_ORDER = ["analysis", "mapping", "content", "ats", "compress"]

# Role of each sub-agent (what the main agent tells it to do). Non-model configuration only.
STAGE_FOCUS: dict[str, str] = {
    "analysis": "Parse the JD -> Requirement Matrix (A/B/C/D).",
    "mapping": "Map A/B/C requirements to the strongest verified profile evidence (A > B > C).",
    "content": "Build the Content Manifest (objective/education/experience/skills/projects/achievement).",
    "ats": "Score the manifest against the JD; return hit/miss + suggestions.",
    "compress": "Fit the manifest to exactly one page without touching the template.",
}

# Per-stage effort defaults. These are the ONLY non-model tuning knobs, and they are overridable
# (see resolve_model / effort_for). Effort is not "the model", so it is safe to default here.
EFFORT_DEFAULTS: dict[str, str] = {
    "analysis": "high",
    "mapping": "high",
    "content": "high",
    "ats": "high",
    "compress": "medium",
}

# Model resolution: the model the pipeline runs on.
# Default = None (inherit the Claude Code session's model = whatever you picked in the terminal).
# Override with SDE_RESUME_MODEL to pin a single model for the whole run (NOT per-stage).
MODEL_ENV_VAR = "SDE_RESUME_MODEL"


def resolve_model(stage: str | None = None, override: str | None = None) -> str | None:
    """Return the model id to pass to the Agent tool, or None to inherit the session model.

    Precedence: explicit `override` arg > $SDE_RESUME_MODEL > None (inherit). Stage is accepted for
    API symmetry but never changes the model — there is no per-stage model here.
    """
    if override:
        return override
    env = os.environ.get(MODEL_ENV_VAR)
    if env:
        return env
    return None


def effort_for(stage: str) -> str:
    """Per-stage effort default; overridable by the caller."""
    if stage not in EFFORT_DEFAULTS:
        raise KeyError(f"unknown stage '{stage}'")
    return EFFORT_DEFAULTS[stage]


def stages() -> list[str]:
    return list(STAGE_ORDER)


def _ensure_here_on_path() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    if here not in sys.path:
        sys.path.insert(0, here)


def prompt_for(stage: str) -> str:
    """The system prompt for a given stage (imported lazily to avoid import churn)."""
    _ensure_here_on_path()
    from pipeline_prompts import STAGE_PROMPTS  # noqa: WPS433

    if stage not in STAGE_PROMPTS:
        raise KeyError(f"no prompt for stage '{stage}'")
    return STAGE_PROMPTS[stage]
