
import streamlit as st
import matplotlib.pyplot as plt

from utils import *

# ==================================================
# PAGE TITLE
# ==================================================

st.title("🚀 AI Resume Analyzer")

st.write("Upload Resume and Paste Job Description")

# ==================================================
# USER INPUTS
# ==================================================

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

# ==================================================
# MAIN LOGIC
# ==================================================

if uploaded_file and job_description:

    # ----------------------------------------------
    # Extract Resume Text
    # ----------------------------------------------

    resume_text = extract_text_from_pdf(uploaded_file)

    # ----------------------------------------------
    # Clean Text
    # ----------------------------------------------

    resume_clean = clean_text(resume_text)

    job_clean = clean_text(job_description)

    # ----------------------------------------------
    # Extract Skills
    # ----------------------------------------------

    job_skills = extract_skills(job_clean)

    resume_skills = extract_skills(resume_clean)

    # ----------------------------------------------
    # Match & Missing Skills
    # ----------------------------------------------

    matched_skills = list(
        set(job_skills) & set(resume_skills)
    )

    missing_skills = list(
        set(job_skills) - set(resume_skills)
    )

    # ----------------------------------------------
    # Similarity Score
    # ----------------------------------------------

    semantic_score = compute_similarity(
        resume_clean,
        job_clean
    )

    # ----------------------------------------------
    # Skill Match Score
    # ----------------------------------------------

    if len(job_skills) > 0:

        skill_match_score = (
            len(matched_skills) / len(job_skills)
        ) * 100

    else:

        skill_match_score = 0

    # ----------------------------------------------
    # Verdict
    # ----------------------------------------------

    if semantic_score > 75:

        verdict = "Strong Match ✅"

    elif semantic_score > 50:

        verdict = "Moderate Match ⚠️"

    else:

        verdict = "Low Match ❌"

    # ==================================================
    # DISPLAY RESULTS
    # ==================================================

    st.subheader("📊 Analysis Results")

    st.write(
        f"### Semantic Match Score: {semantic_score}%"
    )

    st.write(
        f"### Skill Match Score: {round(skill_match_score, 2)}%"
    )

    st.write(
        f"### Verdict: {verdict}"
    )

    # ==================================================
    # MATCHED SKILLS
    # ==================================================

    st.write("## ✅ Matched Skills")

    st.write(matched_skills)

    # ==================================================
    # MISSING SKILLS
    # ==================================================

    st.write("## ❌ Missing Skills")

    st.write(missing_skills)

    # ==================================================
    # RECOMMENDATIONS
    # ==================================================

    st.write("## 🚀 Recommendations")

    for skill in missing_skills:

        if skill in recommendations_map:

            st.write(
                f"• {skill.upper()} → {recommendations_map[skill]}"
            )

    # ==================================================
    # VISUALIZATION
    # ==================================================

    fig, ax = plt.subplots()

    labels = ["Matched", "Missing"]

    counts = [
        len(matched_skills),
        len(missing_skills)
    ]

    ax.bar(labels, counts)

    ax.set_title("Skill Gap Analysis")

    st.pyplot(fig)
