def extract_jd_skills(jd_text):

    skills_database = [
        "Python",
        "SQL",
        "FastAPI",
        "Django",
        "Flask",
        "Docker",
        "AWS",
        "TensorFlow",
        "PyTorch",
        "Machine Learning",
        "Deep Learning",
        "Git",
        "REST API",
        "Artificial Intelligence",
        "Generative AI",
        "Data Science",
        "Cloud Computing",
        "Kubernetes",
        "Scikit-Learn",
        "Pandas",
        "NumPy",
        "OpenCV",
        "Keras"
    ]

    found_skills = []

    for skill in skills_database:

        if skill.lower() in jd_text.lower():
            found_skills.append(skill)

    return found_skills