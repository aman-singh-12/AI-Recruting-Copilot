import ollama


def analyze_candidate(
    resume_text,
    jd_text,
    match_score,
    matched_skills,
    missing_skills):

    prompt = f"""
You are an expert technical recruiter.

Analyze the candidate against the job description.

Resume:
{resume_text}

Job Description:
{jd_text}

PRE-CALCULATED RESULTS:

Match Score:
{match_score}

Matched Skills:
{matched_skills}

Missing Skills:
{missing_skills}

IMPORTANT RULES:

1. Use the provided Matched Skills and Missing Skills.
2. Do NOT invent new missing skills.
3. Do NOT mark any matched skill as missing.
4. Base your evaluation on the supplied score and skill analysis.
5. If a skill is not listed in Missing Skills, do not mention it as a missing requirement.

Provide:

1. Match Score
2. Strengths
3. Weaknesses
4. Missing Requirements
5. Overall Suitability
6. Hiring Recommendation

Keep the response professional and structured.
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