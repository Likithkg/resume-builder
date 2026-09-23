# resume-guidelines.md

> ⚠️ **DE-IDENTIFIED TEMPLATE.** Reusable resume-writing rules only. No candidate
> specifics. Keep the rules; the bullets themselves come from the candidate's
> verified profile (`candidate-profile.md`) and the target role.

# SDE Resume Writing & ATS Guidelines

## 1. Purpose

This document controls **how the resume is written**. It does not define candidate facts.

Source hierarchy — use in this order:

1. `candidate-profile.md` — factual source of truth
2. `career-positioning.md` — positioning and prioritization
3. Target job description — relevance and keyword emphasis only
4. `resume-template.md` — visual structure (immutable)
5. Reference resume / format — visual/template source only

Never use the target role to create candidate experience. Never use the reference to create candidate facts.

---

## 2. Objective / Summary

Concise. Target 2–3 lines. Communicates software-engineering identity, experience level, and strengths.

Do not fill with a long list of technologies. Avoid generic phrases:

* Passionate developer
* Results-driven professional
* Highly motivated individual
* Team player
* Hard-working engineer

Prefer evidence-based positioning.

---

## 3. Experience Structure

Represent each real employer as **one employment entry**. Do not create separate fake
entries or fake job titles for assignments/workstreams. Represent multiple workstreams
through bullet grouping or concise contextual labels if the template permits.

Example:

```
[Employer]
[Title] | [Start] – [Present] | [Location]
```

Omit non-substantive assignments (e.g. onboarding with no real work) rather than padding the resume.

---

## 4. Experience Bullet Formula

Structure:

**Action + Engineering Work + Technology/Context + Verified Result/Constraint**

A strong bullet answers, as naturally as possible:

* What did the candidate build/change?
* What technical problem was involved?
* How was it implemented?
* What technology was used?
* What verified result or constraint demonstrates significance?

Avoid bullets that only describe participation.

### Quality hierarchy

1. Engineering decision + verified outcome
2. Engineering implementation
3. Technology/task statement

Prefer higher levels; use lower levels only where that is all the verified evidence supports.

### Length

1–2 lines in the final template. Normally one major contribution per bullet.

Do not combine unrelated achievements into one oversized bullet merely to save space.

### Number

Target approximately **4–6 strong bullets** for the primary experience, adapting to the
template's available space and the role. Use fewer bullets if each is substantially stronger.
Do not fill space with weak bullets.

---

## 5. Strong Action Verbs

Prefer: Built, Developed, Implemented, Designed, Redesigned, Engineered, Optimized,
Automated, Integrated, Processed, Transformed, Deployed, Containerized, Tested,
Refined, Orchestrated.

Match the verb to the candidate's actual ownership. If the candidate used an existing
endpoint, **Queried / Integrated with** is preferable to **Built / Developed**.
Do not use stronger verbs merely for impact.

## Ownership Accuracy

Supported when verified: Built, Implemented, Developed, Proposed and implemented,
Designed workflow logic, Integrated, Queried, Used.

Avoid (unless explicitly verified at that level): Architected, Led, Owned, Spearheaded,
Directed, Managed.

## Data / Backend / API wording

Describe backend and API work no broader than the candidate's actual contribution.

Safe wording: Built REST APIs, Exposed data through APIs, Queried an endpoint,
Integrated with an existing endpoint.

Do not imply the candidate built or owned an external platform merely because they
interacted with its API. State only that they used/queryed an endpoint.

## AI / LLM / automation experience

Present as engineering. The work may include tool-oriented workflows, incident investigation,
structured output, SOP decomposition, tool/input/output identification, incident-based
testing, and iterative refinement.

Avoid reducing the work to **Prompt Engineering** alone when it involves workflow design.

## Metrics

Use only verified metrics. Never estimate a metric or infer a percentage from a qualitative
statement. Prefer a verified engineering constraint over an invented percentage.

---

## 6. Technical Skills

Compact, ATS-readable, logically grouped, based on verified (or appropriately qualified) skills, and relevant to the role.

Recommended categories (adapt to the candidate and role):

* Languages
* Backend / Frameworks
* Data / Processing
* Databases / Search
* AI / LLM
* Containers / Infrastructure

### Skill ordering

1. Most relevant verified skills first.
2. Stronger evidence before weaker exposure.
3. Match the role's terminology where truthful.
4. Avoid adding technologies merely to increase keyword count.

The skills list may be shortened or reordered depending on the role.

## Skills anti-drift rule

The skills section is not a free-form summary of every technology found in the source files.
Each listed item must have explicit evidence and context. Prefer verified professional skills;
include project technologies only when clearly project-supported; remove lower-value items
before adding any role-only keyword.

---

## 7. ATS Keyword Strategy

Achieve ATS optimization through **natural, evidence-backed keyword placement**:

* Summary/objective where relevant
* Experience bullets
* Skills section
* Projects where genuinely applicable

Do not repeat keywords unnaturally. Do not create a keyword-only skills dump.

## Exact role wording

When the candidate has verified experience, use the role's terminology when it accurately
describes verified experience. Do not replace a precise term with a vague one unnecessarily.

## Missing-technology rule

If the role contains a technology the candidate does not have, **do not add it.**
Emphasize verified adjacent engineering experience instead. The unmet technology itself must not appear unless later verified.

## Adjacent-skill strategy

When a required skill is missing, use truthful adjacent experience (e.g. verified
pipelines/polling/asynchronous processing for a message-queue request). The missing skill
itself must not be claimed.

## Objective rule (role-specific emphasis)

The objective must reflect the role using only verified professional evidence. When space
is limited, prefer verified backend/API/database evidence over AI/LLM terminology.

## Bullet selection rule (role-specific)

Prefer bullets demonstrating backend implementation, API/service development, database
integration, data-processing engineering, asynchronous/chunked/batch processing, and
defect investigation/troubleshooting. AI/LLM bullets are secondary.

## Unsupported requirement handling

If the role requests a capability the candidate lacks, do not create a substitute claim.
Emphasize the strongest verified adjacent evidence instead.

---

## 8. Project Selection

Projects should reinforce the target narrative. Project bullets focus on:

**What was built + how it was built + relevant technical design.**

Do not add (unless verified):

* Users
* Production deployment
* Scale
* Business impact
* Performance metrics

One project should not dominate the resume. Keep it a supporting entry, not the basis for an off-role identity.

---

## 9. Education

Keep concise. Use verified information.

Do not add GPA, coursework, awards, rankings, or academic achievements unless verified.

## Achievement

Verified achievements only. Additional details (year, team size, participant count, prize, topic)
should only be added after verification. Do not invent them.

## Links

Use GitHub and LinkedIn only when the actual URLs are verified. Never reconstruct URLs from
profile names. If URLs are unavailable, do not invent them.

---

## 10. Formatting & Visual Constraints

Content must adapt to `resume-template.md`. Do **not** redesign the resume to fit content.

If content is too long, compress in this order:

1. Remove low-value content.
2. Shorten wording.
3. Remove redundant skills.
4. Weaker project detail.
5. Omit nonessential sections where the template allows.

Never change font family, font size, margins, bullet indentation, section spacing, page
size, section order, or visual hierarchy to accommodate content. Formatting belongs to
`resume-template.md`.

### Density

Information-dense but readable. Avoid large empty spaces, dense walls of text, long
paragraphs, excessive or redundant bullets, and repeating the same technology in every bullet.

### Redundancy check

Before finalizing, merge or replace bullets that communicate essentially the same information.

### Truthfulness gate — every final bullet must pass:

* **Fact check** — supported by `candidate-profile.md`?
* **Ownership check** — wording reflects actual responsibility?
* **Technology check** — did the candidate actually use it?
* **Metric check** — is every number verified?
* **Scope check** — does it avoid implying broader ownership than held?
* **Deployment check** — does it avoid unsupported production/deployment claims?

If any answer is no, rewrite or remove the bullet.

### Hallucination prevention

Never infer: a technology from another technology, production usage from project usage,
leadership from participation, architecture ownership from implementation, scale from
workload, business impact from technical completion, expertise from exposure, or automation
platform ownership from workflow usage. The resume must remain defensible in an interview.

---

## 11. Role-Tailoring Workflow

For each role:

1. **Parse** — identify required languages, backend tech, databases, cloud/infra,
   distributed-system, AI/LLM, and architecture requirements.
2. **Map to evidence** — classify each requirement: **A** strong verified match, **B**
   relevant adjacent, **C** project-only, **D** unverified/missing.
3. **Prioritize** — A > B > C. Do not claim D-level items.
4. **Rewrite emphasis** — reorder/rewrite verified evidence to match the role's priorities.
5. **Truthfulness gate** — verify every claim again.
6. **ATS check** — confirm important verified terms appear naturally.
7. **Visual check** — confirm the tailored content still fits the template.

---

## 12. Immutability & Enforcement

Allowed transformations:

- rewrite verified facts for clarity
- shorten verified facts
- combine non-conflicting verified facts
- select the most relevant verified facts for the role
- reorder bullets within an existing section
- reorder skills within existing categories when relevant
- use exact role terminology when it accurately describes verified experience

Forbidden transformations:

- add a technology because it appears in the role
- add a responsibility because it is common for the role
- add a metric because it would strengthen a bullet
- infer production deployment / ownership / leadership / scale / architecture expertise
- create a new section, rename a required section, or reorder required sections
- change the visual template or create a new resume style

**When a better-looking or more ATS-friendly alternative conflicts with a documented rule, the rule wins.**

These rules are mandatory constraints, not optional advice. Do not replace them with
personal resume-writing preferences. If a requested wording change would require an
unsupported factual claim or a forbidden formatting change, reject it and retain the
compliant version.

---

*This is a reusable ruleset. Keep the rules; replace all candidate-specific examples with the actual candidate's verified facts when generating a resume.*

