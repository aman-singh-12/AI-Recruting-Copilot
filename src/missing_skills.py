def find_missing_skills(jd_skills, matched_skills):

    missing = []

    for skill in jd_skills:

        if skill not in matched_skills:
            missing.append(skill) # which means: missing.append("AWS or any skill names")

    return missing