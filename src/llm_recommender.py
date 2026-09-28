import ollama

def generate_llm_feedback(
    match_score,
    matched_skills,
    missing_skills
):

    # print("Entered generate_llm_feedback()")# just for testing whetehr it is working till here or not

    prompt = f"""
    Candidate Match Score: {match_score}

    Matched Skills: {matched_skills}

    Missing Skills: {missing_skills}

    You are an experienced technical recruiter.

    Analyze the candidate and provide:

    1. Overall suitability.
    2. Strengths.
    3. Missing skills.
    4. Suggestions for improvement.

    Keep the response professional and concise.
    """

    # print("Sending prompt to Ollama...")# just for testing whetehr it is working till here or not

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # print("Response received from Ollama")# just for testing whetehr it is working till here or not

    return response["message"]["content"]