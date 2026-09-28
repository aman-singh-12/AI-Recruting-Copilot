import streamlit as st


from src.parser import extract_resume_text # for parser.py
from src.analyzer import analyze_resume # for analyzer.py
from src.jd_parser import extract_jd_skills # for jd_parser.py
from src.matcher import match_skills # for matcher.py
from src.scorer import calculate_match_score # for scorer.py
from src.missing_skills import find_missing_skills # for missing_skills.py
from src.llm_recommender import generate_llm_feedback # llm_recommender.py
from src.skill_mapper import expand_resume_skills # for skill_mapper.py
from src.ai_matcher import analyze_candidate # for ai_matcher.py
from src.interview_generator import generate_interview_questions# for interview_generator.py

st.title("AI Recruiting Copilot")

st.write("Upload a resume and paste a job description.")

# Resume Upload
resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# Job Description Text Area
jd_text = st.text_area(
    "Paste Job Description",
    height=200
)


# Analyze Button
analyze_button = st.button("Analyze")

if analyze_button:

    if resume_file is None:
        st.error("Please upload a resume.")
        st.stop()

    if not jd_text.strip():
        st.error("Please paste a job description.")
        st.stop()

    st.success(f"Uploaded: {resume_file.name}") # should see Uploaded: Kavita.pdf

    with open("temp_resume.pdf", "wb") as f:
        f.write(resume_file.getbuffer())

    

    resume_text = extract_resume_text("temp_resume.pdf")

    

    resume_data = analyze_resume(resume_text) # Call analyze_resume() for analyzer.py
    

    jd_skills = extract_jd_skills(jd_text) # Call extract_jd_skills() for jd_parser.py
    

    expanded_resume_skills = expand_resume_skills(resume_data["skills"]) # for skill_mapper.py
    
    #st.write("Resume Skills:", resume_data["skills"])

    #st.write("Expanded Resume Skills:", expanded_resume_skills)
    
    matched_skills = match_skills(expanded_resume_skills,jd_skills)

    

    match_score = calculate_match_score(matched_skills,jd_skills) # Call calculate_match_score()

    

    missing_skills = find_missing_skills(jd_skills,matched_skills)

    st.write("Generating AI feedback...") # just for testing whetehr it is working till here or not

    #st.write("JD Skills:", jd_skills)

    #st.write("Matched Skills:", matched_skills)

    #st.write("Missing Skills:", missing_skills)

    #st.write("Match Score:", match_score)
    
    #import time
    #start = time.time()

    st.subheader("Match Summary")

    st.metric("Match Score", f"{match_score}%")

    st.subheader("Matched Skills")

    for skill in matched_skills:
        st.success(f"✔ {skill}")

    st.subheader("Missing Skills")

    for skill in missing_skills:
        st.error(f"✖ {skill}")

    llm_feedback = analyze_candidate(
    resume_text,
    jd_text,
    match_score,
    matched_skills,
    missing_skills
    )

    #st.write("Evaluation Time:", round(time.time() - start, 2), "seconds")

    #start = time.time()

    interview_questions = generate_interview_questions(
    resume_data["skills"],
    matched_skills,
    missing_skills
    )

    #st.write("Evaluation Time:", round(time.time() - start, 2), "seconds")

    st.subheader ("AI Candidate Evaluation Report") # for llm_feedback 
    st.write(llm_feedback)

    st.subheader("Interview Questions") # for interview_questions
    st.write(interview_questions)

    