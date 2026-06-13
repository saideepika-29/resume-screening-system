import streamlit as st

st.title("Resume Screening System")

job_skills = st.text_input(
    "Enter Job Skills (comma separated)"
)

resume_skills = st.text_input(
    "Enter Resume Skills (comma separated)"
)

if st.button("Check Match"):

    job = [x.strip().lower()
           for x in job_skills.split(",")]

    resume = [x.strip().lower()
              for x in resume_skills.split(",")]

    matched = []

    for skill in job:
        if skill in resume:
            matched.append(skill)

    score = (len(matched) / len(job)) * 100

    st.write("Matched Skills:", matched)
    st.write("Match Score:", score, "%")