# Candidate Profile

## 1. Source-of-Truth Policy

This document is the authoritative factual profile for resume generation.

### Source priority

1. Direct information explicitly provided by the candidate during the project
2. Candidate's current resume for personal details, education, personal projects, achievement, links, and skills
3. Reference resume only for visual/template requirements — never for candidate facts

### Rules

* Never invent technologies, responsibilities, metrics, dates, titles, ownership, deployment, adoption, or business impact.
* Do not upgrade exposure into expertise.
* Do not claim a technology simply because it appears in a job description.
* When a fact is uncertain, mark it as `NEEDS VERIFICATION`.
* Resume wording may be stronger than the source wording, but the underlying factual claim must remain unchanged.
* Metrics may only be used when explicitly verified by the candidate.

---

# 2. Candidate Identity

| Field            | Value                                                           | Status                        |
| ---------------- | --------------------------------------------------------------- | ----------------------------- |
| Name             | Likith K G                                                      | Verified                      |
| Phone            | +91-9900631076                                                  | Resume-derived                |
| Email            | [likithbopanna222@gmail.com](mailto:likithbopanna222@gmail.com) | Resume-derived                |
| Location         | Bengaluru, India                                                | Resume-derived                |
| Target Role      | Software Development Engineer (SDE)                             | Verified                      |
| Current Employer | Tata Consultancy Services (TCS)                                 | Verified                      |
| Current Title    | Software Engineer                                               | Resume-derived / confirmed    |
| Start Date       | August 2024                                                     | Resume-derived / confirmed    |
| Experience       | 2+ years                                                        | Derived from employment dates |
| GitHub           | GitHub Profile                                                  | URL needs verification        |
| LinkedIn         | https://www.linkedin.com/in/likith-kg-4b6986268 | Verified                      |

---

# 3. Target Professional Positioning

## Primary Position

**Software Development Engineer (SDE)**

## Core Positioning

**Software Engineering / Backend Engineering + Data Processing + AI/LLM Automation**

## Supporting Areas

* Backend development
* Python development
* Microservices
* REST APIs
* Data processing
* Data ingestion
* ETL/data pipelines
* PostgreSQL
* Elasticsearch
* Event/data processing
* Workflow automation
* Tool orchestration
* LLM-powered workflows
* AI skill/workflow engineering
* Infrastructure troubleshooting automation

## Positions to Avoid as Primary Identity

Unless future evidence supports them:

* Machine Learning Engineer
* Data Scientist
* DevOps Engineer
* Cloud Administrator

The candidate has some ML/project exposure and infrastructure-related AI workflow experience, but these should not replace the primary SDE identity.

---

# 4. Professional Experience

## Tata Consultancy Services (TCS)

**Software Engineer**
**August 2024 – Present**
**Bengaluru, India**

The candidate's TCS experience consists of multiple assignments/projects with different technical focuses.

---

# 5. TCS Assignment 1 — Cloud Administrator

## Context

The candidate initially joined a project as a Cloud Administrator.

## Verified Experience

* The candidate was assigned to the project.
* The candidate waited approximately two months for a laptop.
* There was no meaningful work performed during this period.
* No meaningful KT/training was provided.
* The project subsequently determined that an experienced candidate was required and the candidate was removed from the assignment.

## Resume Treatment

**Do not present this as substantive Cloud Administrator experience.**

Do not claim:

* Cloud administration expertise
* Cloud infrastructure management
* Production cloud operations
* Cloud deployment ownership
* Cloud architecture
* Kubernetes administration
* Cloud certifications

This assignment may be omitted completely from the resume if space is limited.

---

# 6. TCS Assignment 2 — Data Processing & Microservices

## Context

The candidate worked on backend/data-processing services involving infrastructure/log data.

The data was available through IBM Cloud Object Storage (COS). The candidate used COS as a **data source** but did not have direct access/administrative control over the storage environment.

## Technologies / Components Used

* Python
* Flask
* Node.js
* IBM Cloud Object Storage as a data source
* Avro
* Parquet
* PyArrow
* fastavro
* PostgreSQL
* Elasticsearch
* Docker
* IBM Cloud VM

## Backend / Service Work

The candidate personally worked on Python/Flask and Node.js services that:

* Retrieved/consumed data from the available data source.
* Processed Avro/Parquet data.
* Transformed data.
* Loaded processed data into databases.
* Exposed processed information through APIs where applicable.
* Worked with PostgreSQL.
* Worked with Elasticsearch.
* Used Docker for service execution/containerization.

## Data Processing Challenge

A key engineering problem involved processing approximately **2–3 GB of data within a roughly 2-minute processing window**.

The original processing approach involved:

1. Downloading Avro/Parquet data
2. Converting data to CSV
3. Writing the CSV to disk
4. Reading the data back from disk
5. Processing the data
6. Loading the result into the database

This created unnecessary disk I/O and processing overhead.

## Engineering Solution

The candidate proposed and implemented a more efficient processing approach based on processing the data directly/on-the-fly rather than relying on the intermediate CSV-on-disk workflow.

The implementation involved:

* PyArrow
* fastavro
* Chunked processing
* Asynchronous processing
* Batch database insertion
* Direct/on-the-fly processing of the source data

## Verified Outcome

The redesigned approach enabled the processing workload to complete within the required approximately **2-minute processing window** for the approximately **2–3 GB data workload**.

Do not invent or state a percentage performance improvement unless one is later verified.

## Duplicate / State Management

The candidate implemented a persisted processing-state mechanism using a JSON file.

The mechanism recorded previously processed data.

During subsequent polling:

* The previous processing window and new window could overlap.
* Previously recorded data was checked against the persisted state.
* Previously processed data was skipped.
* New/unprocessed data was processed.

This was used to avoid duplicate processing across overlapping polling windows.

## Deployment

The candidate manually deployed one of the services to an IBM Cloud VM by:

* Cloning the repository
* Running the service using Docker
* Exposing the service externally

This should be described as **manual deployment to an IBM Cloud VM**.

Do not describe this as a sophisticated CI/CD or Kubernetes deployment.

---

# 7. TCS Assignment 3 — Incident Automation

## Context

The candidate worked on an automation workflow environment containing components such as LLM/agent blocks and tool-oriented workflow steps.

The work focused on automating parts of incident investigation and data collection.

## Verified Work

The candidate worked on workflows involving:

* Osprey
* Osprey endpoint/query usage
* Tools
* LLM agents
* Incident investigation
* Data collection
* Structured output generation
* TSV normalization
* Resource extraction
* Diagnostic workflow steps

## Osprey Usage

The candidate used an available Osprey endpoint to query required information.

Important boundary:

> The candidate did not build or administer Osprey.

Resume wording should describe **querying/using an Osprey endpoint**, not ownership of Osprey.

## LLM / Tool Workflow

The workflows could:

1. Obtain information using available tools/endpoints.
2. Provide relevant information to an LLM agent.
3. Process or normalize the resulting information.
4. Produce structured TSV output suitable for subsequent workflow steps.

Other workflow logic involved extracting relevant resources from provided information and constructing diagnostic commands where applicable.

## Resume Treatment

Position this as:

**LLM-powered incident investigation and workflow automation**

or equivalent wording.

Do not claim:

* Autonomous remediation
* Full autonomous incident resolution
* ServiceNow-triggered workflows
* Production-wide deployment
* Quantified MTTR reduction
* Quantified reduction in operational effort

unless separately verified.

---

# 8. TCS Current Assignment — IBM Bob AI Skill Engineering

## Context

The candidate is currently working with IBM Bob, an internal AI chat/coding assistant.

The work involves converting infrastructure troubleshooting knowledge into AI skills that Bob can use when responding to troubleshooting scenarios.

## Domain

* IaaS troubleshooting
* Acadia
* NetApp storage

## Source Knowledge

The candidate works with a broad knowledge base of infrastructure/SOP material.

The knowledge exists in sources such as files and repositories.

The candidate cannot expose confidential internal IBM Bob skill implementations.

## Skill Engineering Workflow

The candidate's workflow is:

```text
SOP
 ↓
Understand troubleshooting procedure
 ↓
Break procedure into steps
 ↓
Identify steps requiring tools
 ↓
Identify required inputs
 ↓
Identify expected outputs
 ↓
Translate procedure into skill instructions
 ↓
Test against incidents
 ↓
Identify failures
 ↓
Refine instructions
 ↓
Repeat testing
```

## Engineering Nature of the Work

The work involves:

* Knowledge extraction
* Procedure decomposition
* AI skill design
* Tool identification
* Input/output specification
* Troubleshooting workflow design
* Incident-based testing
* Iterative refinement
* AI-assisted operational workflow engineering

## Current Boundaries

Do not claim:

* Public skill publication
* Production deployment
* Production adoption
* Number of users
* Business impact
* Quantified time savings
* Quantified incident reduction
* Ownership of IBM Bob
* Development of the underlying IBM Bob platform

The candidate is **developing and testing AI skills/workflows**, not building the underlying IBM Bob product.

## Current Technology Boundary

The candidate has explicitly stated that the current IBM Bob skill-development work does **not** involve Python or Git as part of this specific work.

---

# 9. Personal Projects

## Cloud Service Observability & Monitoring Platform

**Technologies:** FastAPI, PostgreSQL, Docker, AWS CloudWatch

### Verified resume-derived details

* Web-based monitoring and observability platform for cross-cloud resource monitoring.
* Built real-time event streaming and monitoring dashboards.
* Designed an event-driven architecture using Server-Sent Events (SSE).
* Implemented JWT-based role-based access control (RBAC).
* Containerized the application using Docker.

### Resume Boundary

Do not add:

* Production deployment
* Number of users
* Cloud scale
* Business impact
* Availability/SLA claims
* Performance metrics

unless verified separately.

---

## Heart Disease Prediction System — ML Backend

**Technologies:** Python, Flask, Scikit-learn, Pandas

### Verified resume-derived details

* Python-based web application for predicting the likelihood of heart disease.
* Built REST APIs for ML inference.
* Developed an end-to-end ML pipeline covering preprocessing, training, and inference.
* Evaluated Logistic Regression, Random Forest, and SVM models using precision-recall metrics.

### Resume Boundary

The existing resume states a **sub-100ms inference latency** claim.

Status:

**NEEDS VERIFICATION**

Do not use the metric until confirmed.

This project demonstrates ML/backend project experience but does not change the candidate's primary professional positioning from SDE to ML Engineer.

---

# 10. Technical Skills

## Languages

### Verified / Strongly Supported

* Python
* SQL

## Backend

* Flask
* FastAPI
* Node.js
* REST APIs
* Microservices

## Data Processing

* Avro
* Parquet
* PyArrow
* fastavro
* Chunked processing
* Asynchronous processing
* Batch processing / ingestion

## Databases / Search

* PostgreSQL
* Elasticsearch
* MySQL

## Containers / Infrastructure

* Docker

## AI / LLM

* LLM integration
* Prompt engineering
* Agentic workflows
* LLM agents
* AI skill/workflow engineering

## Developer Tools

* VS Code
* Postman
* Linux
* Git
* GitHub

## Skills Requiring Verification Before Professional-Experience Claims

The following appear in the existing resume but should not automatically be presented as professional experience:

* Kubernetes
* CI/CD
* AWS CloudWatch
* OpenAI API
* Groq API
* HuggingFace
* Ollama
* Claude Code
* PostgreSQL indexing
* PostgreSQL partitioning
* System design

These may be included in a final skills section only after their actual level/context is established.

---

# 11. Education

**Shree Devi Institute of Technology**
**Bachelor of Engineering in Information Science and Engineering**
**2020 – 2024**
Mangalore, Karnataka, India

Additional academic details:

`NEEDS VERIFICATION`

---

# 12. Achievement

**2nd Place — TCS AI Hackathon**

Additional information such as:

* Year
* Team size
* Number of participants
* Project/topic
* Individual/team achievement
* Prize

is:

`NEEDS VERIFICATION`

---

# 13. Links

* GitHub: `URL NEEDS VERIFICATION`
* LinkedIn: `URL NEEDS VERIFICATION`

Never reconstruct or invent the URLs.

---

# 14. Verified Metrics

The following metrics are currently safe to use:

| Metric                           | Status             | Usage      |
| -------------------------------- | ------------------ | ---------- |
| 2–3 GB data workload             | Verified           | Can use    |
| ~2-minute processing window      | Verified           | Can use    |
| 2+ years professional experience | Derived from dates | Can use    |
| 100K+ events/day                 | Unverified         | Do not use |
| Sub-second PostgreSQL latency    | Unverified         | Do not use |
| Sub-100ms ML inference           | Unverified         | Do not use |
| MTTR reduction                   | Unverified         | Do not use |
| Manual effort reduction          | Unverified         | Do not use |

---

# 15. Explicitly Unsupported Claims

Unless independently verified later, do not claim:

* 100K+ infrastructure events/day
* Kubernetes professional experience
* CI/CD implementation
* PostgreSQL indexing/partitioning optimization
* Sub-second query latency
* Sub-100ms ML inference
* MTTR reduction
* Percentage performance improvements
* ServiceNow-triggered workflows
* Autonomous incident remediation
* Production adoption of IBM Bob skills
* Public publication of IBM Bob skills
* User adoption of IBM Bob skills
* Building the IBM Bob platform
* Administering IBM Cloud Object Storage
* Building/administering Osprey
* Cloud Administrator as substantive professional experience

---

# 16. Candidate's Strongest Evidence

The strongest engineering evidence currently available is:

### Evidence 1 — Data Processing Engineering

The candidate identified a processing bottleneck involving approximately 2–3 GB of Avro/Parquet data that needed to be processed within roughly two minutes, redesigned the processing path to avoid intermediate CSV disk I/O, and implemented direct/chunked/asynchronous processing with batch ingestion.

### Evidence 2 — Stateful Data Processing

The candidate implemented persisted processing state to handle overlapping polling windows and avoid duplicate processing.

### Evidence 3 — Backend Services

The candidate built Python/Flask and Node.js services for data processing, ingestion, and API-oriented backend workflows.

### Evidence 4 — Incident Automation

The candidate implemented workflow logic using tools, Osprey endpoint queries, and LLM agents to support incident investigation and structured data processing.

### Evidence 5 — AI Skill Engineering

The candidate currently converts infrastructure SOPs into structured AI troubleshooting skills, identifies tool/input/output requirements, tests skills against incidents, and iteratively improves the workflows.

---

# 17. Overall Professional Story

The candidate's experience should be represented as a progression:

```text
Backend / Data Processing
        ↓
Microservices & APIs
        ↓
Performance-oriented Data Pipelines
        ↓
Automation & Tool Orchestration
        ↓
LLM-powered Incident Workflows
        ↓
AI Skill / Agent Workflow Engineering
        ↓
SDE + Backend + AI Automation
```

The central identity remains:

**Software Development Engineer**

The candidate should appear as a hands-on software engineer who has developed from backend/data-processing engineering into AI-powered automation and skill/workflow engineering.

---

# 18. Resume Generation Rule

When generating a resume from this profile:

> Present the strongest relevant evidence for the target SDE role without changing the underlying facts.

The job description determines **which verified evidence receives emphasis**.

It does not determine what experience the candidate has.

## 19. Final Resume QA Lock — 2026-09-03

The current one-page SDE resume uses the following presentation rules:

* GitHub is displayed as `GitHub Profile` and the PDF contains a clickable hyperlink targeting `https://github.com/likithkg`.
* The GitHub destination remains `NEEDS VERIFICATION` in the factual profile until the candidate confirms the exact URL.
* LinkedIn remains `NEEDS VERIFICATION` until its exact URL is confirmed.
* The resume omits the initial Cloud Administrator assignment as substantive experience.
* Education uses the verified degree wording and keeps `Bachelor of Engineering in Information Science and Engineering` on one line in the final layout.
* The final resume is one US Letter page.
* No unsupported metrics or technologies were added during final formatting.


# 20. IMMUTABLE FACTUAL SOURCE CONTRACT — DO NOT OVERRIDE

This file is the **authoritative candidate-fact database**. A resume generator MUST treat it as read-only source data.

## Absolute rules

1. Never invent, infer, embellish, reconcile, or "improve" a candidate fact.
2. Never replace a candidate fact with a more impressive equivalent.
3. `NEEDS VERIFICATION` means **DO NOT USE AS VERIFIED RESUME CONTENT**.
4. An item marked unverified may only be used after the candidate explicitly verifies it.
5. The target JD can request emphasis, but it can never upgrade an item from unverified to verified.
6. The reference resume can provide visual information only; it can never provide candidate facts.
7. If another source conflicts with this file, this file wins unless the candidate explicitly provides a newer correction.
8. If a fact is missing, the generator must omit it rather than guess.

## Context boundaries

A technology listed under a personal project is not automatically professional experience.

A technology listed in the general skills inventory is not automatically evidence of professional use.

An endpoint used by the candidate does not mean the candidate built or administered the underlying platform.

A workload size does not imply production scale.

A successful technical outcome does not imply business impact, user adoption, or percentage improvement.

## Resume-generation lock

The generator may change **wording, emphasis, ordering of bullets within an allowed section, and JD relevance**.

The generator MUST NOT change the underlying factual meaning.

# 21. READ-ONLY SOURCE LOCK

This file is input data, not a drafting suggestion. During resume generation, the model MUST read it as authoritative, MUST NOT edit or reinterpret it, and MUST NOT use outside knowledge to fill missing fields.


## ABSOLUTE FACT LOCK — FAIL CLOSED

This file is the factual authority. Do not add, infer, upgrade, normalize, or substitute candidate facts. JD technologies are never evidence of candidate experience. Exposure is not expertise; usage is not ownership; querying is not building/administering. Metrics, scale, performance, deployment, adoption, impact, leadership, dates, titles, and responsibilities require explicit support.

If a requested claim is unsupported, OMIT IT. If sources conflict, STOP and flag the conflict rather than silently reconciling it. Reject any output containing unsupported technology, metric, responsibility, ownership, production/deployment/adoption claim, leadership claim, or upgraded factual meaning.

# FINAL ENFORCEMENT PATCH — FACT v2

This file is the factual source of truth. It is read-only during resume generation.

## FACTUAL FIREWALL

The generator MUST distinguish between:
- verified professional experience;
- verified project experience;
- skills/tool exposure;
- items requiring verification.

A technology listed for a project MUST NOT be silently promoted to professional experience. A skill listed in the profile MUST NOT be presented as deep expertise unless the profile explicitly supports that level.

The target JD MUST NEVER be used to fill a factual gap.

## NO RESUME-CONTENT INVENTION

The generator MUST NOT add, strengthen, quantify, or reinterpret:
- technologies;
- responsibilities;
- ownership;
- leadership;
- deployment claims;
- scale;
- metrics;
- performance claims;
- business impact;
- user adoption;
- certifications;
- titles;
- dates.

If a requested JD keyword is unsupported, omit it. Do not force keyword coverage.

## READ-ONLY RULE

This document is input data, not a drafting canvas. The model MUST NOT edit this source, reinterpret it to improve the resume, or use outside knowledge to complete it.

# FINAL ENFORCEMENT PATCH — FACT v3 — RESUME-ELIGIBLE EVIDENCE MATRIX

This section is authoritative for what may appear in the generated resume. It exists to prevent JD-driven skill invention and context mixing.

## Professional experience — resume-eligible

Verified professional evidence includes: Python, Flask, Node.js, microservices, REST/API-oriented backend services, Avro, Parquet, PyArrow, fastavro, PostgreSQL, Elasticsearch, SQL, chunked processing, asynchronous processing, batch insertion/ingestion, polling-based processing, JSON-based processing state, Docker, manual deployment of a service to an IBM Cloud VM, Osprey endpoint/query usage, tools and LLM agents, structured TSV normalization, incident investigation/data collection, diagnostic/resource-extraction workflows where applicable, AI skill/workflow engineering, SOP-to-AI-skill conversion, incident-based testing, and iterative refinement.

## Project-only / contextual evidence

The following may be used only in the appropriate project/context: FastAPI, AWS CloudWatch, SSE, JWT-based RBAC, Scikit-learn, Pandas, Logistic Regression, Random Forest, SVM, and precision-recall evaluation.

Do not move project-only technologies into professional experience.

## Not resume-eligible unless separately verified

Do not add or infer: SQLAlchemy, ORM, transaction-management expertise, typed Python, Django, message queues, automated backend/unit-test ownership, CI/CD, Kubernetes, PostgreSQL indexing/partitioning expertise, production-wide deployment, autonomous remediation, quantified MTTR/manual-effort reduction, Prompt Engineering as a standalone professional skill, or GitHub as a technical/professional skill solely because a GitHub profile link exists.

## JD technology firewall

A technology appearing in a JD remains UNVERIFIED unless it exists in the approved evidence above or is separately verified later. JD presence can never promote it into the candidate's skill inventory.
