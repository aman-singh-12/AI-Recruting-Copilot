"""def match_skills(resume_skills, jd_skills):

    matched = []

    for skill in jd_skills:

        if skill in resume_skills:
            matched.append(skill)

    return matched"""
def match_skills(resume_skills, jd_skills):

    matched = []

    resume_skills_lower = [
        skill.lower()
        for skill in resume_skills
    ]

    for skill in jd_skills:

        if skill.lower() in resume_skills_lower:
            matched.append(skill)

    return matched