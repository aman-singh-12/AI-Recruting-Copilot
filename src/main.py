from parser import extract_resume_text # for parser.py
from analyzer import analyze_resume # for analyzer.py
from jd_parser import extract_jd_skills # for parsing jd skills from jd_parser.py
from matcher import match_skills # for matcher resume skills and jd skills from matcher.py
from scorer import calculate_match_score # for scorer.py
from missing_skills import find_missing_skills # for missing_skills.py
from recommender import generate_recommendation # for recommender.py
from llm_recommender import generate_llm_feedback # for llm_recommender.py

print("AI Recruiting Copilot Started")

resume_text = extract_resume_text("resumes/Kavita.pdf") # for parser.py
# resume_text
# This variable stores the entire text extracted from the PDF.

analysis = analyze_resume(resume_text) # for analyzer.py

print(analysis) # for analyzer.py

#print(resume_text) # for parser.py
# temporary comment - This will make the terminal output much cleaner.

# --------------------------------------------------------------------------------
with open("data/sample_jd.txt", "r") as file:
    jd_text = file.read()

jd_skills = extract_jd_skills(jd_text)

# jd skills vs resume skills matching
matched_skills = match_skills(analysis["skills"],jd_skills) 
# jd_skills from matcher.py and skills from analyzer.py of splitting section
"""which means:

Resume Skills
      VS
JD Skills
      ↓
Matched Skills"""

match_score = calculate_match_score(matched_skills,jd_skills) # for scorer.py

missing_skills = find_missing_skills(jd_skills,matched_skills) 
# to find_missing_skills from missing_skills.py

recommendation = generate_recommendation(match_score) # for recommender.py

llm_prompt = generate_llm_feedback(match_score,matched_skills,missing_skills) # for llm_recommender.py


print(jd_skills) # output of jd_parser.py function
print(matched_skills) # output of matcher.py function
print(match_score) # output of scorer.py function
print(missing_skills) # output of missing_skills.py function
print(recommendation) # for recommender.py
print(llm_prompt)
"""
I do:

print(resume_text)

to quickly verify:

PDF reading works
Text extraction works
Data looks correct
-------------------------
Why this order?

Because each step depends on the previous step:

matched_skills
      ↓
match_score
      ↓
missing_skills
      ↓
recommendation
      ↓
llm_prompt
"""