
import streamlit as st
import re
import PyPDF2
import matplotlib.pyplot as plt

from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# ==================================================
# PAGE TITLE
# ==================================================

st.title("🚀 AI Resume Analyzer")

st.write("Upload Resume + Paste Job Description")

# ==================================================
# LOAD MODEL
# ==================================================

model = SentenceTransformer('all-MiniLM-L6-v2')

# ==================================================
# CLEAN TEXT
# ==================================================

def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)

    text = " ".join(text.split())

    return text

# ==================================================
# EXTRACT PDF TEXT
# ==================================================

def extract_text_from_pdf(file):

    reader = PyPDF2.PdfReader(file)

    text = ""

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text

# ==================================================
# SKILLS DATABASE
# ==================================================

SKILLS_DB = [

    "python",
    "machine learning",
    "deep learning",
    "nlp",
    "sql",
    "pytorch",
    "tensorflow",
    "streamlit",
    "rag",
    "azure",
    "mlops",
    "api",
    "vector databases",
    "semantic search",
    "document understanding",
    "llms",
    "data analysis",
    "pandas",
    "numpy",
    "scikit learn",
    "xgboost",
    "transformers"

]


recommendations = {
    "tensorflow":"Learn Deep Learning with TensorFlow",
    "rag":"Build a RAG chatbot project",
    "azure":"Learn Azure AI Services",
    "mlops":"Learn model deployment and monitoring",
    "vector databases":"Learn FAISS and Pinecone",
    "api":"Build REST APIs using FastAPI"
}

# ==================================================
# SKILL EXTRACTION
# ==================================================


# ==================================================
# SKILL EXTRACTION
# ==================================================

SKILL_ALIASES = {
    "python": ["python"],
    "machine learning": ["machine learning"],
    "deep learning": ["deep learning"],
    "nlp": ["nlp", "natural language processing"],
    "sql": ["sql"],
    "pytorch": ["pytorch"],
    "tensorflow": ["tensorflow"],
    "streamlit": ["streamlit"],
    "rag": ["rag", "retrieval augmented generation"],
    "azure": ["azure"],
    "mlops": ["mlops", "machine learning operations"],
    "api": ["api", "apis", "rest api", "rest apis"],
    "vector databases": ["vector database", "vector databases"],
    "semantic search": ["semantic search"],
    "document understanding": ["document understanding"],
    "llms": ["llm", "llms", "large language models"],
    "data analysis": ["data analysis"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "scikit learn": ["scikit learn", "scikit-learn", "sklearn"],
    "xgboost": ["xgboost"],
    "transformers": ["transformers", "transformer models"],
}

def extract_skills(text):
    if not isinstance(text, str) or not text.strip():
        return []

    # Normalize punctuation and hyphens consistently
    text = clean_text(text)
    detected = set()

    for canonical, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            alias = clean_text(alias)

            pattern = r"(?<!\w)" + re.escape(alias) + r"(?!\w)"

            if re.search(pattern, text):
                detected.add(canonical)
                break

    return sorted(detected)




# ==================================================
# SIMILARITY
# ==================================================

def compute_similarity(resume, job):

    emb1 = model.encode([resume])

    emb2 = model.encode([job])

    score = cosine_similarity(emb1, emb2)[0][0]

    return round(score * 100, 2)

def extract_email(text):

    text = text.replace(" ", "")

    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    emails = re.findall(pattern, text)

    if emails:
        return emails[0]

    return "Not Found"

def extract_phone(text):

    pattern = r'(\+?\d[\d\s\-]{8,15}\d)'

    phones = re.findall(pattern, text)

    if phones:
        return phones[0]

    return "Not Found"

def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line.split()) >= 2:

            if line.isupper():

                return line.title()

    return "Not Found"



# ==================================================
# USER INPUTS
# ==================================================

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

job_description = st.text_area("Paste Job Description")

# ==================================================
# MAIN LOGIC
# ==================================================

if uploaded_file and job_description:

    # Extract Resume Text
    resume_text = extract_text_from_pdf(uploaded_file)

    # st.write("### Debug Resume Text")

    # st.text(resume_text[:1000])

    name = extract_name(resume_text)

    email = extract_email(resume_text)

    phone = extract_phone(resume_text)

    # Clean
    resume_clean = clean_text(resume_text)

    job_clean = clean_text(job_description)

    # Skills
    job_skills = extract_skills(job_clean)

    resume_skills = sorted(extract_skills(resume_clean))

    matched = sorted(list(set(job_skills) & set(resume_skills)))
    missing = sorted(list(set(job_skills) - set(resume_skills)))

    # Scores
    semantic_score = compute_similarity(resume_clean, job_clean)

    skill_score = (
    len(matched) / len(job_skills) * 100
    if len(job_skills) > 0
    else 0
    )

    ats_score = round(
    semantic_score * 0.4 +
    skill_score * 0.6,
    2
    )
    if ats_score >= 80:
        verdict = "Strong Match ✅"

    elif ats_score >= 60:
        verdict = "Moderate Match ⚠️"

    else:
        verdict = "Low Match ❌"

    # Verdict
    # if semantic_score > 75:
    #     verdict = "Strong Match ✅"

    # elif semantic_score > 50:
    #     verdict = "Moderate Match ⚠️"

    # else:
    #     verdict = "Low Match ❌"

    strengths = []

    if "python" in matched:
        strengths.append("Python expertise detected")

    if "machine learning" in matched:
        strengths.append("Machine Learning experience detected")

    if "nlp" in matched:
        strengths.append("NLP skills detected")

    if semantic_score > 50:
        strengths.append("Resume aligns reasonably with job description")


    improvements = []

    if "tensorflow" in missing:
        improvements.append(
            "Add TensorFlow projects to strengthen deep learning profile."
        )

    if "mlops" in missing:
        improvements.append(
            "Learn deployment and MLOps workflows."
        )

    if semantic_score < 70:
        improvements.append(
            "Tailor your resume keywords according to the job description."
        )

    # ==================================================
    # DISPLAY RESULTS
    # ==================================================

    st.subheader("📊 Analysis Results")

    st.subheader("📄 Resume Information")

    st.write(f"**Name:** {name}")

    st.write(f"**Email:** {email}")

    st.write(f"**Phone:** {phone}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Semantic Score", f"{semantic_score}%")

    with col2:
        st.metric("Skill Score", f"{round(skill_score,2)}%")

    with col3:
        st.metric("Resume–Job Match Score", f"{ats_score}%")
        st.caption(
            "Heuristic score based on semantic similarity (40%) "
            "and required-skill coverage (60%). Not an official ATS score."
        )


    if ats_score < 70:

      st.warning(
          "Your resume may not align strongly with this job description."
      )

    # st.metric(
    # "ATS Compatibility Score",
    # f"{ats_score}%"
    # )

    # st.write(f"### Skill Match Score: {round(skill_score,2)}%")

    st.write(
    f"Matched {len(matched)} out of {len(job_skills)} required skills"
    )

    st.write(f"### Verdict: {verdict}")

    st.write("## ✅ Matched Skills")

    st.write(", ".join(matched))

    st.write("## ❌ Missing Skills")

    st.write(", ".join(missing))

    st.subheader("📌 Resume Skills")

    st.write(", ".join(resume_skills))

    st.subheader("📚 Learning Recommendations")

    for skill in missing:

      if skill in recommendations:

          st.write(
              f"✅ {skill} → {recommendations[skill]}"
          )

    st.subheader("💪 Resume Strengths")

    for s in strengths:
       st.success(s)

    st.subheader("🚀 Resume Improvement Suggestions")

    for item in improvements:
        st.warning(item)



    # ==================================================
    # CHART
    # ==================================================

    fig, ax = plt.subplots()

    labels = ['Matched', 'Missing']

    counts = [len(matched), len(missing)]

    bars = ax.bar(labels, counts)

    for bar in bars:
        height = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width()/2,
            height,
            str(height),
            ha='center'
        )

    ax.set_title("Skill Gap Analysis")
    ax.set_ylabel("Number of Skills")
    st.pyplot(fig)

    st.subheader("ATS Match")

    st.progress(min(int(ats_score), 100))

    st.markdown("---")
    st.caption(
        'Built with Python • Streamlit • Sentence Transformers • NLP • Cosine Similarity • ATS Analysis'
    )
