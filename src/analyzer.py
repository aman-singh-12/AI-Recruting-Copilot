# NEXT GOAL:
# Extract the actual TECHNICAL SKILLS section
# from the resume instead of only checking
# whether the section exists.

def extract_skills_section(text):

    start = text.find("TECHNICAL SKILLS")

    if start == -1:
        return "Skills section not found"

    end = text.find("CERTIFICATIONS")

    if end == -1:
        return text[start:]

    return text[start:end]


# ----------------------------------------------
# splitting

def extract_skill_keywords(skills_text):

    skills_text = skills_text.replace("\n", ",")

    skills = []

    ignore_words = [
        "TECHNICAL SKILLS",
        "Languages",
        "Deep Learning",
        "Modeling",
        "XAI & ML",
        "CV & Data",
        "Backend / DevOps",
        "Domain Expertise"
    ]

    for item in skills_text.split(","):

        item = item.strip()

        if item in ignore_words:
            continue

        if len(item) > 1:
            skills.append(item)

    return skills


# --------------------------------------------------
# whether the section exists.
def analyze_resume(text):

    sections = {}

    text_upper = text.upper()

    if "EDUCATION" in text_upper:
        sections["education"] = "Found"

    skills_section = extract_skills_section(text)

    sections["skills"] = extract_skill_keywords(skills_section)

    if "PROFESSIONAL EXPERIENCE" in text_upper:
        sections["experience"] = "Found"

    if "RESEARCH & TECHNICAL PROJECTS" in text_upper:
        sections["projects"] = "Found"

    return sections