import ollama


def generate_interview_questions(
    resume_skills,
    matched_skills,
    missing_skills
):

    prompt = f"""
    You are an experienced technical interviewer.

    Candidate Skills:
    {resume_skills}

    Matched Skills:
    {matched_skills}

    Missing Skills:
    {missing_skills}

    Generate:

    1. Technical Interview Questions
       - Based on matched skills
       - 5 questions

    2. Skill Gap Questions
       - Based on missing skills
       - 3 questions

    3. Behavioral Questions
       - Based on projects and experience
       - 3 questions

    Keep questions specific and professional.
    """

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
#Resume
#JD
#Matched Skills
#Missing Skills
#        ↓
#interview_generator.py
#        ↓
#Technical Questions

#Skill Gap Questions

#Behavioral Questions