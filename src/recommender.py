"""
This file will take:

match_score ----------- from scorer.py
missing_skills ---------- from missing_skills.py

and produce:

Strong Match
Medium Match
Weak Match

plus a recruiter recommendation.
This is the first recruiter decision logic:
Now:

Resume
 ↓
JD
 ↓
Matched Skills
 ↓
Score
 ↓
Recruiter Decision
"""
def generate_recommendation(match_score):

    if match_score >= 80:
        return "Strong Match"

    elif match_score >= 60:
        return "Medium Match"

    else:
        return "Weak Match"