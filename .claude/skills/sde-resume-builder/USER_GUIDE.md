# SDE Resume Builder User Guide

The `sde-resume-builder` skill is a professional system designed to generate truthful, ATS-friendly, and high-impact Software Development Engineer (SDE) resumes tailored to specific job descriptions.

## 1. What This Skill Does

This skill transforms a comprehensive candidate profile into a polished, one-page resume. Unlike generic resume builders, it performs a deep analysis of the target Job Description (JD) to emphasize the most relevant skills and experiences from the candidate's history without fabricating information.

**Key Features:**
- **JD Tailoring:** Maps candidate evidence to job requirements using a priority matrix (Strong Match $\rightarrow$ Adjacent Evidence $\rightarrow$ Project Evidence).
- **Truthfulness Guard:** Strictly adheres to the provided candidate profile; no hallucinations or "JD leakage."
- **Fixed Visual Fidelity:** Produces a professional, one-page resume using a locked reference format (Computer Modern font, US Letter geometry).
- **Automated Validation:** Every generated resume is validated for length, placeholders, and visual constraints.

## 2. Providing Your Data

To generate a resume, you must provide two primary inputs: a **Candidate Profile** and a **Job Description**.

### The Candidate Profile
The Candidate Profile is the "Source of Truth." It should be a JSON object that follows the schema defined in `data/candidate-schema.json`.

**Required Sections:**
- **Identity:** Full name, email, and contact details.
- **Experience:** Professional work history with dates, companies, and achievement-based bullet points.
- **Education:** Degrees, institutions, and graduation dates.
- **Skills:** Categorized technical skills (e.g., Languages, Frameworks, Cloud).

**Optional Sections:**
- **Projects:** Personal or open-source work.
- **Achievements:** Certifications, awards, and honors.

You can provide this data as a JSON file path or by pasting the JSON directly into your prompt.

### The Job Description (JD)
Provide the full text of the job posting you are applying for. The system will use this to determine which parts of your profile to highlight.

## 3. How to Trigger Resume Generation

To use the skill, invoke it via the Claude CLI and provide the necessary inputs.

**Example Command:**
`/sde-resume-builder "Here is my profile: [path/to/profile.json] and here is the JD: [Paste JD text here]"`

**What happens next:**
1. **Analysis:** Claude parses the JD and creates a requirement matrix.
2. **Mapping:** Your profile is mapped against these requirements.
3. **Content Generation:** A tailored content manifest is created.
4. **Rendering:** The system uses the internal renderer to create the files.
5. **Validation:** The final output is checked against the one-page and visual constraints.

## 4. What Output to Expect

The skill does not just output text to the console; it generates actual documents.

**Deliverables:**
- **PDF Resume:** A high-fidelity, one-page PDF.
- **DOCX Resume:** An editable Word version of the same resume.

**Location:**
The files are saved to the `./output/` directory relative to the project root. You will be provided with the absolute file paths to these documents once the generation and validation steps are complete.
