# Version 1 Improvement Module
SKILL_RELATIONSHIPS = {

    "TensorFlow": [
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence"
    ],

    "PyTorch": [
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence"
    ],

    "Scikit-Learn": [
        "Machine Learning",
        "Artificial Intelligence"
    ],

    "Keras": [
        "Deep Learning",
        "Artificial Intelligence"
    ],

    "FastAPI": [
        "Backend Development"
    ],

    "Django": [
        "Backend Development"
    ],

    "Flask": [
        "Backend Development"
    ],

    "Docker": [
        "DevOps"
    ],

    "Git": [
        "Version Control"
    ]
}


def expand_resume_skills(resume_skills):

    expanded_skills = set(resume_skills)

    for skill in resume_skills:

        if skill in SKILL_RELATIONSHIPS:

            for related_skill in SKILL_RELATIONSHIPS[skill]:

                expanded_skills.add(related_skill)

    return list(expanded_skills)