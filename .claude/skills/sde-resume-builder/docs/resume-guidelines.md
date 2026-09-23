# resume-guidelines.md

# SDE Resume Writing & ATS Guidelines

## 1. Purpose

This document defines the rules for converting the candidate's verified profile and a target Software Development Engineer (SDE) job description into a tailored resume.

It controls **how the resume is written**.

It does not define new candidate facts.

The factual source of truth is `candidate-profile.md`.

The positioning strategy is defined in `career-positioning.md`.

The visual structure is defined separately in `resume-template.md`.

---

# 2. Source Hierarchy

When generating a resume, use sources in this order:

1. `candidate-profile.md` — factual source of truth
2. `career-positioning.md` — positioning and prioritization
3. Target job description — determines relevance and keyword emphasis
4. `resume-template.md` — determines visual structure
5. Reference resume PDF — visual/template source only

Never use the target JD to create candidate experience.

Never use the reference resume to create candidate facts.

---

# 3. Core Resume Objective

The resume should communicate:

> **Software Development Engineer with hands-on backend, data-processing, and AI/LLM automation experience.**

The document should make the candidate's software-engineering identity immediately clear.

The resume should not read primarily as:

* ML Engineer
* Data Scientist
* Cloud Administrator
* DevOps Engineer
* Prompt Engineer

---

# 4. Recruiter 10-Second Test

A recruiter scanning the top portion of the resume should quickly understand:

1. The candidate is an SDE/software engineer.
2. The candidate has 2+ years of professional experience.
3. The candidate has backend engineering experience.
4. The candidate has meaningful data-processing experience.
5. The candidate has modern AI/LLM workflow experience.

If these points are not apparent quickly, revise the content hierarchy.

---

# 5. Resume Content Hierarchy

Prioritize content in approximately this order:

1. Professional identity / objective
2. TCS software-engineering experience
3. Backend/data-processing engineering evidence
4. AI/LLM automation evidence
5. Relevant technical skills
6. Strong supporting projects
7. Education
8. Achievement where space permits

The initial Cloud Administrator assignment should normally be omitted.

---

# 6. Professional Summary / Objective

The summary/objective should be concise.

Target:

**2–3 lines**

It should communicate:

* Software engineering identity
* Experience level
* Backend/data-processing strengths
* AI/LLM automation differentiation

Do not fill the summary with a long list of technologies.

Do not use generic phrases such as:

* Passionate developer
* Results-driven professional
* Highly motivated individual
* Team player
* Hard-working engineer

unless a specific JD requires such wording and it adds meaningful value.

Prefer evidence-based positioning.

---

# 7. Experience Structure

Represent TCS as one employment entry:

**Tata Consultancy Services (TCS)**
**Software Engineer | August 2024 – Present | Bengaluru, India**

Do not create separate fake employment entries for individual assignments.

Assignments/workstreams may be represented through bullet grouping or concise contextual labels if the template permits.

Do not invent assignment titles that were never official job titles.

---

# 8. Experience Bullet Formula

The preferred bullet structure is:

**Action + Engineering Work + Technology/Context + Result/Constraint**

A strong bullet should answer as many of these as naturally possible:

* What did the candidate build/change?
* What technical problem was involved?
* How was it implemented?
* What technology was used?
* What verified result or constraint demonstrates significance?

Avoid bullets that only describe participation.

---

# 9. Bullet Quality Hierarchy

Prefer bullets in this order:

### Level 1 — Engineering decision + verified outcome

Example structure:

> Redesigned a data-processing workflow to eliminate intermediate CSV disk I/O, using chunked/asynchronous processing and batch ingestion to process a 2–3 GB workload within the required ~2-minute window.

### Level 2 — Engineering implementation

> Built Python/Flask and Node.js services for processing Avro/Parquet data and loading transformed results into PostgreSQL and Elasticsearch.

### Level 3 — Technology/task statement

> Developed backend services using Python, Flask, and Node.js.

Level 1 and Level 2 bullets should receive priority.

---

# 10. Bullet Length

Target approximately:

**1–2 lines in the final resume template.**

Avoid unnecessarily long bullets.

A bullet should normally communicate one major engineering contribution.

Do not combine unrelated achievements into one oversized bullet merely to save space.

---

# 11. Number of Experience Bullets

For the primary TCS experience, target approximately:

**4–6 strong bullets**

The exact number depends on the reference template's available space and the target JD.

Use fewer bullets if each bullet is substantially stronger.

Do not fill space with weak bullets.

---

# 12. Strong Action Verbs

Prefer precise engineering verbs such as:

* Built
* Developed
* Implemented
* Designed
* Redesigned
* Engineered
* Optimized
* Automated
* Integrated
* Processed
* Transformed
* Deployed
* Containerized
* Implemented
* Tested
* Refined
* Orchestrated

Use the verb that accurately describes the candidate's actual level of ownership.

Do not use stronger verbs merely for impact.

For example:

If the candidate used an existing endpoint:

**Queried** or **integrated with**

is preferable to:

**Built** or **developed**

---

# 13. Ownership Accuracy

Ownership language must reflect actual responsibility.

Use:

* Built
* Implemented
* Developed
* Proposed and implemented
* Designed workflow logic
* Integrated
* Queried
* Used

when supported.

Avoid:

* Architected
* Led
* Owned
* Spearheaded
* Directed
* Managed

unless the candidate has explicitly verified that level of responsibility.

---

# 14. Data-Processing Experience

When relevant, prioritize the candidate's strongest data-processing story.

Include where appropriate:

* Avro
* Parquet
* PyArrow
* fastavro
* Chunked processing
* Asynchronous processing
* Batch ingestion
* PostgreSQL
* Elasticsearch
* Processing-state management

The strongest engineering story is:

> The candidate identified unnecessary intermediate CSV disk I/O and redesigned the processing path for direct/on-the-fly processing using chunked/asynchronous processing and batch ingestion.

Where appropriate, include the verified constraint:

**2–3 GB within approximately 2 minutes.**

Do not create an unsupported percentage improvement.

---

# 15. Backend Engineering

Backend experience should be clearly visible.

Relevant evidence includes:

* Python
* Flask
* Node.js
* Microservices
* REST APIs
* Data ingestion
* Data transformation
* PostgreSQL
* Elasticsearch
* Docker

Do not describe backend work more broadly than the candidate's actual contribution.

---

# 16. API Language

Use API terminology carefully.

Safe wording includes:

* Built REST APIs
* Exposed processed data through APIs
* Queried an endpoint
* Integrated with an existing endpoint

Do not imply that the candidate built or owned an external platform merely because they interacted with its API.

Specifically:

**Osprey was used through an available endpoint.**

Do not state that the candidate built or administered Osprey.

---

# 17. AI / LLM Experience

AI experience should be presented as engineering.

Strong concepts include:

* LLM agents
* Tool-oriented workflows
* Incident investigation
* Data collection
* Structured output
* TSV normalization
* Resource extraction
* Diagnostic workflow steps
* SOP decomposition
* AI skill engineering
* Tool/input/output identification
* Incident-based testing
* Iterative refinement

Avoid reducing the candidate's current work to:

**Prompt Engineering**

alone.

The work includes workflow design, procedure decomposition, tool identification, input/output specification, testing, and refinement.

---

# 18. IBM Bob Experience

Describe the current work as:

**AI skill/workflow engineering**

or equivalent.

Communicate that the candidate:

1. Understands infrastructure troubleshooting procedures.
2. Breaks procedures into executable steps.
3. Identifies required tools.
4. Identifies inputs and expected outputs.
5. Converts procedures into structured AI skill instructions.
6. Tests against incidents.
7. Refines the workflow based on failures.

Do not claim:

* Building IBM Bob
* Owning IBM Bob
* Public skill publication
* Production deployment
* Production adoption
* Number of users
* Business impact
* Quantified time savings

---

# 19. Incident Automation Experience

For incident-automation bullets, emphasize the engineering workflow.

Potential structure:

> Engineered incident-investigation workflows combining tools, Osprey endpoint queries, LLM agents, and structured TSV normalization to support data collection and diagnostic workflows.

Only use wording that remains consistent with the candidate profile.

Do not claim:

* ServiceNow-triggered workflows
* Autonomous remediation
* Fully autonomous incident resolution
* Quantified MTTR reduction

---

# 20. Technical Skills Section

The skills section should be:

* Compact
* ATS-readable
* Grouped logically
* Based on verified or appropriately qualified skills
* Relevant to the target JD

Recommended categories:

### Languages

Python, SQL

### Backend

Flask, FastAPI, Node.js, REST APIs, Microservices

### Data Processing

Avro, Parquet, PyArrow, fastavro, Chunked Processing, Asynchronous Processing, Batch Processing

### Databases / Search

PostgreSQL, Elasticsearch, MySQL

### AI / LLM

LLM Agents, LLM Integration, Agentic Workflows, AI Skill/Workflow Engineering, Prompt Engineering

### Containers / Infrastructure

Docker

The final skills list may be shortened or reordered depending on the target JD.

---

# 21. Skill Ordering

Within each category:

1. Put the most relevant verified skills first.
2. Put stronger evidence before weaker exposure.
3. Match the target JD's terminology where truthful.
4. Avoid unnecessary technologies merely to increase keyword count.

For a Python-heavy role:

**Python** should be prominent.

For a data-processing role:

**PyArrow, fastavro, Avro, Parquet, data processing** should become more prominent.

For an AI workflow role:

**LLM Agents, Agentic Workflows, AI Skill/Workflow Engineering** should receive more emphasis.

---

# 22. ATS Keyword Strategy

ATS optimization should be achieved through **natural, evidence-backed keyword placement**.

Use important verified JD terms in:

* Summary/objective where relevant
* Experience bullets
* Skills section
* Projects where genuinely applicable

Do not repeat a keyword unnaturally.

Do not create a keyword-only skills dump.

---

# 23. Exact JD Matching

When a JD uses a technology that the candidate genuinely has, use the JD's terminology when appropriate.

Example:

If the candidate has verified experience with:

**PostgreSQL**

and the JD says:

**PostgreSQL**

use **PostgreSQL**.

Do not replace it with a vague term such as:

**Relational database**

unless necessary.

---

# 24. Missing Technology Rule

If a JD contains a technology the candidate does not have:

**Do not add it.**

Example:

JD:

* Python
* Docker
* Kubernetes
* Kafka

Candidate:

* Python
* Docker
* No verified Kubernetes
* No verified Kafka

Resume:

* Python
* Docker

Do not add Kubernetes or Kafka.

Instead, emphasize verified adjacent engineering experience where relevant.

---

# 25. Adjacent-Skill Strategy

When a required JD skill is missing, use truthful adjacent experience.

For example:

JD:

**Kafka**

Relevant candidate evidence:

* Data pipelines
* Polling
* Asynchronous processing
* Batch ingestion
* Microservices
* Processing state

These can be emphasized as transferable data-processing experience.

Kafka itself must not appear unless later verified.

---

# 26. Metrics Rules

Use metrics only when verified.

Currently safe:

* 2+ years professional experience
* 2–3 GB data workload
* ~2-minute processing window

Currently prohibited unless verified:

* 100K+ events/day
* Sub-second PostgreSQL latency
* Sub-100ms ML inference
* MTTR reduction
* Manual-effort reduction
* Percentage performance improvement

Never estimate a metric.

Never infer a percentage improvement from a qualitative statement.

---

# 27. Project Selection

Projects should reinforce the target SDE narrative.

Primary project:

**Cloud Service Observability & Monitoring Platform**

Use it to demonstrate:

* Backend development
* FastAPI
* PostgreSQL
* Docker
* Event-driven architecture
* SSE
* JWT/RBAC
* Monitoring/observability

Secondary project:

**Heart Disease Prediction System — ML Backend**

Use it to demonstrate:

* Python
* Flask
* REST APIs
* Backend ML integration
* End-to-end ML pipeline

Do not allow the ML project to dominate the resume.

---

# 28. Project Bullet Rules

Project bullets should focus on:

**What was built + how it was built + relevant technical design.**

Do not add:

* Users
* Production deployment
* Scale
* Business impact
* Performance metrics

unless verified.

The sub-100ms ML inference claim remains excluded until verified.

---

# 29. Education

Keep education concise.

Use verified information:

**Shree Devi Institute of Technology**
**Bachelor of Engineering in Information Science and Engineering | 2020–2024**
Mangalore, Karnataka, India

Do not add GPA, coursework, awards, rankings, or academic achievements unless verified.

---

# 30. Achievement

The verified achievement is:

**2nd Place — TCS AI Hackathon**

Additional details should only be added after verification.

Do not invent:

* Competition year
* Team size
* Participant count
* Prize
* Project details
* Individual contribution

---

# 31. Links

Use GitHub and LinkedIn only when the actual URLs are verified.

Never reconstruct URLs from profile names.

If URLs are unavailable, do not invent them.

---

# 32. Formatting and Visual Constraints

Content must adapt to `resume-template.md`.

Do not redesign the resume to fit content.

If content is too long:

1. Remove low-value content.
2. Shorten wording.
3. Remove redundant skills.
4. Reduce weaker project detail.
5. Omit nonessential sections where allowed by the template.

Do not change the reference resume's fundamental visual structure simply to fit more content.

---

# 33. Density Management

The resume should be information-dense but readable.

Avoid:

* Large empty spaces caused by unnecessarily short content
* Dense walls of text
* Long paragraphs
* Excessive bullets
* Repeated technologies
* Redundant descriptions

Each line should earn its space.

---

# 34. Bullet Redundancy Check

Before finalizing, identify bullets that communicate essentially the same information.

For example, do not separately state:

* Built Python data-processing services.
* Developed Python services for data processing.

Combine or replace redundant bullets with stronger evidence.

---

# 35. Technology Repetition

Repeating an important technology is acceptable when natural.

However, avoid inserting the same technology into every bullet solely for ATS purposes.

Example:

If Python is clearly established in the experience bullets and skills section, do not force "Python" into every sentence.

---

# 36. Truthfulness Gate

Every final bullet must pass:

### Fact check

Is the underlying claim supported by `candidate-profile.md`?

### Ownership check

Does the wording accurately reflect the candidate's level of responsibility?

### Technology check

Was the technology actually used by the candidate?

### Metric check

Is every number verified?

### Scope check

Does the bullet avoid implying broader ownership than the candidate had?

### Deployment check

Does it avoid unsupported production/deployment claims?

If any answer is **no**, rewrite or remove the bullet.

---

# 37. Hallucination Prevention

Never infer:

* A technology from another related technology
* Production usage from project usage
* Leadership from participation
* Architecture ownership from implementation
* Scale from workload
* Business impact from technical completion
* Expertise from exposure
* Automation platform ownership from workflow usage

The resume must remain defensible in an interview.

---

# 38. Interview Defensibility

Every significant resume claim should be something the candidate can explain in an interview.

A strong resume is not one that contains the most keywords.

A strong resume is one where the candidate can confidently explain:

* What problem existed
* What they did
* Why they chose the approach
* What technologies they used
* What tradeoffs existed
* What the verified result was

---

# 39. JD Tailoring Workflow

For each target JD:

### Step 1 — Parse the JD

Identify:

* Required languages
* Backend technologies
* Databases
* Cloud/infrastructure technologies
* Distributed-system requirements
* AI/LLM requirements
* Architecture concepts
* Collaboration/soft-skill requirements

### Step 2 — Map to Candidate Evidence

Classify each requirement:

**A — Strong verified match**

**B — Relevant adjacent evidence**

**C — Project-only evidence**

**D — Unverified / missing**

### Step 3 — Prioritize

Use:

**A > B > C > D**

D-level technologies should not be claimed.

### Step 4 — Rewrite Emphasis

Reorder and rewrite verified evidence to match the JD's priorities.

### Step 5 — Run Truthfulness Gate

Verify every claim again.

### Step 6 — Run ATS Check

Ensure important verified JD terminology appears naturally where relevant.

### Step 7 — Run Visual Check

Ensure the tailored content still fits the reference template.

---

# 40. Different JD Types

## Backend SDE

Prioritize:

* Python
* Flask
* Node.js
* Microservices
* REST APIs
* PostgreSQL
* Elasticsearch
* Data processing
* Docker

---

## Python SDE

Prioritize:

* Python
* Flask
* PyArrow
* fastavro
* Data processing
* Asynchronous processing
* Batch ingestion
* REST APIs

---

## Data-Intensive SDE

Prioritize:

* Avro
* Parquet
* PyArrow
* fastavro
* Data pipelines
* Chunked processing
* Batch ingestion
* PostgreSQL
* Elasticsearch
* Processing state

---

## AI/LLM SDE

Prioritize:

* LLM agents
* Tool workflows
* Incident automation
* Structured data processing
* AI skill engineering
* SOP decomposition
* Input/output specification
* Incident testing
* Iterative refinement

---

## Agentic AI SDE

Prioritize:

* LLM agents
* Tool use
* Workflow logic
* Tool orchestration
* Input/output handling
* AI skills
* Incident workflows
* Testing/refinement

---

## Cloud/Infrastructure-Adjacent SDE

Prioritize only verified evidence:

* Docker
* IBM Cloud VM
* IBM Cloud Object Storage as a data source
* IaaS troubleshooting
* Infrastructure data processing
* Infrastructure workflows

Do not turn this into a cloud-administrator resume.

---

# 41. Soft Skills

Avoid a large generic soft-skills section.

The candidate's engineering behavior should demonstrate:

* Problem solving
* Analytical thinking
* Troubleshooting
* Iterative improvement
* Technical ownership where verified

Show these through bullets rather than unsupported adjectives.

---

# 42. Final Resume Quality Checklist

Before producing the final resume, verify:

### Positioning

* [ ] SDE identity is immediately clear.
* [ ] Backend/software engineering is prominent.
* [ ] Data processing is prominent.
* [ ] AI/LLM experience is visible but appropriately positioned.
* [ ] Candidate does not appear primarily as an ML Engineer, Data Scientist, DevOps Engineer, or Cloud Administrator.

### Experience

* [ ] TCS is represented as one employment entry.
* [ ] Individual assignments are not presented as fake job titles.
* [ ] Strongest engineering work receives the most space.
* [ ] Cloud Administrator assignment is omitted unless specifically relevant and truthful.
* [ ] IBM Bob work is described as AI skill/workflow engineering.

### Technical Accuracy

* [ ] Every technology is supported.
* [ ] Missing JD technologies are not added.
* [ ] Osprey is described as an endpoint/query integration, not a platform built by the candidate.
* [ ] IBM Bob is not described as built by the candidate.
* [ ] Cloud Object Storage is not described as administered by the candidate.

### Metrics

* [ ] Only verified metrics appear.
* [ ] 2–3 GB and ~2-minute constraint may be used.
* [ ] Unverified 100K+ events/day is excluded.
* [ ] Unverified latency claims are excluded.
* [ ] Unsupported performance percentages are excluded.
* [ ] Unsupported MTTR/manual-effort claims are excluded.

### ATS

* [ ] Relevant verified JD keywords appear naturally.
* [ ] No keyword stuffing.
* [ ] Skills are grouped logically.
* [ ] Important verified technologies are visible in experience where appropriate.

### Writing

* [ ] Bullets begin with meaningful action verbs.
* [ ] Bullets focus on engineering contributions.
* [ ] Ownership language is accurate.
* [ ] Redundant bullets are removed.
* [ ] Generic buzzwords are minimized.
* [ ] Every major claim is interview-defensible.

### Visual

* [ ] Reference resume structure is preserved.
* [ ] Section order follows the template.
* [ ] Typography follows the template.
* [ ] Margins and spacing follow the template.
* [ ] Bullet style follows the template.
* [ ] Resume remains readable and visually balanced.
* [ ] Content is shortened rather than redesigning the template.

---

# 43. Final Generation Principle

The final resume should be:

**Truthful + SDE-focused + evidence-driven + ATS-compatible + visually faithful to the reference template.**

The target JD determines **what to emphasize**.

The candidate profile determines **what is true**.

The career-positioning document determines **how the candidate should be perceived**.

The resume-template document determines **how the information should look**.

The final `SKILL.md` will combine these rules into a reusable generation system.

## 44. Final Formatting QA Lock — 2026-09-03

The final generated resume must also enforce these implementation details:

* Use a one-page output when the target version is specified as one page.
* Preserve a visible one-line vertical gap between major sections.
* Preserve a one-line vertical gap between each project technology line and its project bullets.
* Experience and project bullets use the same intentional tab-level indentation.
* Experience location is secondary metadata: smaller and italic, aligned with the company-name left edge.
* Project technology metadata is smaller and italic and must remain on one line.
* Education degree wording must not wrap when the final one-page version is approved; shorten/rebalance content before allowing the degree line to wrap.
* Hyperlinks must be embedded as actual PDF link annotations, not merely styled text.
* Final QA must inspect the rendered PDF and its link annotations, not only the source file.
* The final one-page PDF must use the reference-style Computer Modern family and preserve the established monochrome visual hierarchy.


# 45. IMMUTABLE GENERATION CONTRACT

This document controls **content writing and ATS behavior**. It does not grant permission to modify the candidate facts or visual template.

## Allowed transformations

The generator may only:

- rewrite verified facts for clarity
- shorten verified facts
- combine non-conflicting verified facts
- select the most relevant verified facts for the JD
- reorder bullets inside an existing section
- reorder skills within existing categories when relevant
- use exact JD terminology when it accurately describes verified experience

## Forbidden transformations

The generator MUST NOT:

- add a technology because it appears in the JD
- add a responsibility because it is common for the role
- add a metric because it would strengthen a bullet
- infer production deployment
- infer ownership or leadership
- infer scale or user adoption
- infer architecture expertise
- create a new section
- rename a required section
- reorder the required sections
- change the visual template
- create a new resume style

## Final rule

When a better-looking or more ATS-friendly alternative conflicts with a documented rule, **the documented rule wins**.

# 46. READ-ONLY WRITING-RULE LOCK

This file is a rule set, not optional advice. When generating a resume, every applicable rule is mandatory. The model MUST NOT replace these rules with its own resume-writing preferences.


## ABSOLUTE GENERATION CONTRACT — FAIL CLOSED

These rules are executable constraints, not suggestions.

### NO CREATIVE FORMATTING
The model MUST NOT redesign, modernize, rebalance whitespace, change margins/font/indentation to solve wrapping, change section order, or introduce visual elements. Formatting decisions belong to `resume-template.md`.

### NO CREATIVE CONTENT REPAIR
If content does not fit, use only compression rules explicitly authorized by `resume-template.md`. Never invent a formatting or factual solution.

### JD AUTHORITY LIMIT
The JD controls relevance, emphasis, and truthful keyword selection only. It has ZERO authority over page structure, typography, spacing, section order, or candidate facts.

### OUTPUT REJECTION
Any resume violating a locked formatting or factual rule is INVALID and must not be delivered as an alternative.

# FINAL ENFORCEMENT PATCH — WRITING v2

These rules govern wording only. They MUST NOT be interpreted as permission to modify the visual template.

## CONTENT-FIRST COMPRESSION

When the selected content does not fit the locked one-page template, reduce content before changing layout:
1. remove redundant wording;
2. shorten bullets while preserving factual meaning;
3. remove lower-priority bullets;
4. remove lower-priority skills;
5. omit low-value projects/details when necessary.

Never change font family, font size, margins, bullet indentation, section spacing, page size, section order, or visual hierarchy to accommodate content.

## NO MODEL STYLE PREFERENCE

Terms such as "improve readability," "modernize," "balance whitespace," "make it cleaner," or "make it more professional" MUST NOT trigger visual redesign. The only acceptable visual target is the locked reference/template specification.

## ATS FIREWALL

ATS optimization is limited to truthful wording and ordering of evidence within permitted sections. ATS goals NEVER override the template or candidate factual source.

## FAIL-CLOSED

If a requested wording change would require an unsupported factual claim or a forbidden formatting change, reject that change and retain the compliant version.

# FINAL ENFORCEMENT PATCH — WRITING v3 — JD TRUTH FILTER

## JD KEYWORD SELECTION ALGORITHM

For every JD keyword, classify it before using it:
- VERIFIED-PROFESSIONAL: may appear in Objective, Experience, or Skills/Tools.
- VERIFIED-PROJECT: may appear only with the relevant project.
- ADJACENT/INFERRED: do not use as a claimed skill.
- UNVERIFIED-JD: exclude.

Never collapse these classes.

## Skills anti-drift rule

The Skills / Tools section is not a free-form summary of technologies found anywhere in the source files. Each listed item must have an explicit evidence class and context. Prioritize verified professional backend skills; include project technologies only when clearly project-supported; remove lower-value items before adding any JD-only keyword.

## Objective rule

The Objective must reflect the target role using only verified professional evidence. For Python backend roles, prefer Python/backend/API/database evidence over AI/LLM terminology when space is limited.

## Bullet selection rule

For a Python backend JD, prefer bullets demonstrating backend implementation, API/service development, database integration, data-processing engineering, asynchronous/chunked/batch processing, and defect investigation/troubleshooting. AI/LLM bullets are secondary.

## Unsupported requirement handling

If a JD requests a capability the candidate lacks, do not create a substitute claim. Example: a request for SQLAlchemy/ORM and transaction management does not authorize an ORM or transaction-management claim; use the verified PostgreSQL/SQL integration evidence instead.
