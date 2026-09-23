# Candidate Profile

> ⚠️ **DE-IDENTIFIED TEMPLATE — fill in your own verified facts.**
> This file ships with **no real personal data**. Copy this file over a real
> `personal/candidate-profile.md` (which is gitignored) or edit this one in place
> and replace every `[placeholder]` below with your own verified facts. Never
> commit real PII (name, phone, email, LinkedIn/GitHub URLs, real employers).

## 1. Source-of-Truth Policy

This document is the authoritative factual source for resume generation. It is
read-only during resume generation. No stage is permitted to edit it or to
augment its contents.

### Source priority

1. Direct information explicitly provided by the candidate during the project
2. Candidate's current resume for personal details, education, personal projects, achievement, links, and skills
3. Reference resume / reference format only for visual/template requirements — never for candidate facts

### Rules

* Never invent technologies, responsibilities, metrics, dates, titles, ownership, deployment, adoption, or business impact.
* Do not upgrade exposure into expertise.
* Do not claim a technology simply because it appears in a job description.
* When a fact is uncertain, mark it as `NEEDS VERIFICATION`.
* Resume wording may be stronger than the source wording, but the underlying factual claim must remain unchanged.
* Metrics may only be used when explicitly verified by the candidate.

---

## 2. Candidate Identity

| Field            | Value                     | Status              |
| ---------------- | ------------------------- | ------------------- |
| Name             | [Your Full Name]          | [Verified / etc.]   |
| Phone            | [Your Phone Number]       | [Status]            |
| Email            | [your.email@example.com]  | [Status]            |
| Location         | [City, Country]           | [Status]            |
| Target Role      | [Target Role, e.g. SDE]   | [Verified]          |
| Current Employer | [Current Employer]        | [Verified]          |
| Current Title    | [Current Title]           | [Status]            |
| Start Date       | [Start Date]              | [Status]            |
| GitHub           | [GitHub URL or `NEEDS VERIFICATION`] | [Status] |
| LinkedIn         | [LinkedIn URL or `NEEDS VERIFICATION`] | [Status] |

---

## 3. Target Professional Positioning

## Primary Position

[Target role, e.g. **Software Development Engineer (SDE)**]

## Core Positioning

[One-paragraph story that ties the candidate's experience together, e.g. "Software engineering spanning backend services, data processing, microservices, and AI/LLM workflows."]

## Supporting Areas

* [Supporting theme 1]
* [Supporting theme 2]
* [Supporting theme 3]

## Positions to Avoid as Primary Identity

Unless future evidence supports them, the candidate should NOT be positioned primarily as:

* [Role A — e.g. ML Engineer]
* [Role B — e.g. Data Scientist]
* [Role C — e.g. DevOps Engineer]

---

## 4. Professional Experience

> Add one entry per real employer. Repeat this block as needed.

## [Employer Name]

**[Current Title]**
**[Start Date] – [End Date or Present]**
**[Location]**

[1–2 sentences of context: the kind of work, team, or business. Omit roles or assignments that were not substantive, e.g. onboarding without work.]

### Verified Experience

* [Verifiable accomplishment 1 — action + engineering work + technology + verified result]
* [Verifiable accomplishment 2]
* [Verifiable accomplishment 3]
* [Verifiable accomplishment 4]

### Technologies Used

* [Technology 1]
* [Technology 2]
* [Technology 3]

### Resume Treatment

[Note what should or should NOT be presented. E.g. which assignments, metrics, or technologies are unverified or should be omitted to keep the resume truthful and truthful to the target role.]

---

## 5. Personal Projects

> Optional. Add one entry per real project. Omit if none are worth including.

## [Project Name]

**Technologies:** [Tech 1, Tech 2, Tech 3]

### Verified resume-derived details

* [What was actually built — verifiable]
* [How it was built — verifiable]
* [Outcome or role you played — verifiable]

### Resume Boundary

[What NOT to add: production deployment, user count, scale, business impact, performance metrics, etc. — unless verified separately.]

---

## 6. Technical Skills

## Languages

* [Verified language 1]
* [Verified language 2]

## [Backend / Frameworks]

* [Verified skill 1]
* [Verified skill 2]

## [Data / Processing]

* [Verified skill 1]
* [Verified skill 2]

## [Databases / Search]

* [Verified skill 1]
* [Verified skill 2]

## [Containers / Infrastructure]

* [Verified skill 1]

## [AI / LLM]

* [Verified skill 1]
* [Verified skill 2]

### Skills Requiring Verification Before Professional-Experience Claims

[These may appear only after their level/context is established; do not present as professional experience yet.]

* [Skill 1]
* [Skill 2]

---

## 7. Education

**[Institution Name]**
**[Degree] in [Major]**
**[Start–End or Graduation Year]**
[Location]

Additional academic details:

`[NEEDS VERIFICATION or —]`

---

## 8. Achievement

**[Achievement Title]**

Additional information such as year, team size, participant count, topic, or prize:

`[NEEDS VERIFICATION or —]`

---

## 9. Links

* GitHub: `[URL — NEEDS VERIFICATION]`
* LinkedIn: `[URL — NEEDS VERIFICATION]`

Never reconstruct or invent URLs.

---

## 10. Verified Metrics

| Metric                        | Status       | Usage   |
| ----------------------------- | ------------ | ------- |
| [Verified metric 1]           | [Verified]   | [Use]   |
| [Verified metric 2]           | [Verified]   | [Use]   |
| [Unverified metric 1]         | [Unverified] | [Do not use] |

Metrics may only be used when explicitly verified. Never estimate a metric or infer a percentage.

---

## 11. Explicitly Unsupported Claims

Unless independently verified later, do not claim:

* [Unsupported claim 1]
* [Unsupported claim 2]
* [Unsupported claim 3]

---

## 12. Resume Generation Rule

> Present the strongest relevant evidence for the target role **without changing the underlying facts**.

The job description determines **which verified evidence receives emphasis**.
It does not determine what experience the candidate has.

---

## 13. IMMUTABLE FACTUAL SOURCE CONTRACT — DO NOT OVERRIDE

This file is the **authoritative candidate-fact database**. A resume generator MUST treat it as read-only source data.

### Absolute rules

1. Never invent, infer, embellish, reconcile, or "improve" a candidate fact.
2. Never replace a candidate fact with a more impressive equivalent.
3. `NEEDS VERIFICATION` means **DO NOT USE AS VERIFIED RESUME CONTENT**.
4. An item marked unverified may only be used after the candidate explicitly verifies it.
5. The target JD can request emphasis, but it can never upgrade an item from unverified to verified.
6. The reference resume can provide visual information only; it can never provide candidate facts.
7. If another source conflicts with this file, this file wins unless the candidate explicitly provides a newer correction.
8. If a fact is missing, the generator must omit it rather than guess.

### Context boundaries

A technology listed under a personal project is not automatically professional experience.

A technology listed in the general skills inventory is not automatically evidence of professional use.

An endpoint used by the candidate does not mean the candidate built or administered the underlying platform.

A workload size does not imply production scale.

A successful technical outcome does not imply business impact, user adoption, or percentage improvement.

---

## 14. READ-ONLY SOURCE LOCK

This file is input data, not a drafting canvas. During resume generation, the model MUST read it as authoritative, MUST NOT edit or reinterpret it, and MUST NOT use outside knowledge to fill missing fields.

## ABSOLUTE FACT LOCK — FAIL CLOSED

These facts are authoritative. Do not add, infer, upgrade, normalize, or substitute candidate facts. JD technologies are never evidence of candidate experience. Exposure is not expertise; usage is not ownership; querying is not building/administering. Metrics, scale, performance, deployment, adoption, impact, leadership, dates, titles, and responsibilities require explicit support.

If a requested claim is unsupported, OMIT IT. If sources conflict, STOP and flag the conflict rather than silently reconciling it. Reject any output containing unsupported technology, metric, responsibility, ownership, production/deployment/adoption claim, leadership claim, or upgraded factual meaning.

---

*This is a template. Replace every `[placeholder]` with verified facts from the candidate's own resume, or copy this into a gitignored `personal/candidate-profile.md` and fill it in from there.*
