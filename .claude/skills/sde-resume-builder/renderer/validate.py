import logging
from typing import Any, Dict, List, Tuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_resume_data(data: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Validates the resume data for minimum required fields.
    Returns a tuple of (is_valid, list_of_errors).
    """
    errors = []

    # Validate Header
    header = data.get("header", {})
    if not header:
        errors.append("Header section is missing.")
    else:
        if not header.get("name"):
            errors.append("Header: 'name' is required.")
        if not header.get("email"):
            errors.append("Header: 'email' is highly recommended.")

    # Validate Experience (not strictly required, but we can check structure if present)
    experience = data.get("experience", [])
    if not isinstance(experience, list):
        errors.append("Experience must be a list of entries.")
    else:
        for i, exp in enumerate(experience):
            if not exp.get("company") or not exp.get("role"):
                errors.append(f"Experience entry {i+1}: 'company' and 'role' are required.")

    # Validate Education
    education = data.get("education", [])
    if not isinstance(education, list):
        errors.append("Education must be a list of entries.")
    else:
        for i, edu in enumerate(education):
            if not edu.get("institution") or not edu.get("degree"):
                errors.append(f"Education entry {i+1}: 'institution' and 'degree' are required.")

    # Validate Skills
    skills = data.get("skills", {})
    if not skills:
        errors.append("Skills section is missing or empty.")
    elif not isinstance(skills, (dict, list)):
        errors.append("Skills must be a dictionary (category -> list) or a list of skills.")

    is_valid = len([e for e in errors if "required" in e.lower()]) == 0

    # We consider the resume 'valid' if all required fields are present,
    # even if some recommended ones are missing.

    return is_valid, errors

if __name__ == "__main__":
    # Basic test
    test_data = {
        "header": {"name": "John Doe"},
        "experience": [{"company": "Tech Corp", "role": "SDE"}],
        "education": [{"institution": "Uni", "degree": "CS"}],
        "skills": {"Languages": ["Python", "Java"]}
    }
    valid, errs = validate_resume_data(test_data)
    print(f"Valid: {valid}, Errors: {errs}")

    test_data_bad = {
        "header": {},
        "experience": [{"company": "Tech Corp"}]
    }
    valid_bad, errs_bad = validate_resume_data(test_data_bad)
    print(f"Valid: {valid_bad}, Errors: {errs_bad}")
