
import re
import PyPDF2

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ==================================================
# LOAD EMBEDDING MODEL
# ==================================================

model = SentenceTransformer('all-MiniLM-L6-v2')

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
    "apis",
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

# ==================================================
# RECOMMENDATIONS MAP
# ==================================================

recommendations_map = {

    "tensorflow": "Learn Deep Learning using TensorFlow",

    "pytorch": "Build Deep Learning projects using PyTorch",

    "azure": "Explore Azure AI Services",

    "mlops": "Learn model deployment and monitoring",

    "streamlit": "Build ML web apps using Streamlit",

    "rag": "Understand Retrieval-Augmented Generation",

    "vector databases": "Learn FAISS or Pinecone",

    "semantic search": "Study embedding similarity systems",

    "transformers": "Learn HuggingFace Transformers"
}

# ==================================================
# CLEAN TEXT
# ==================================================

def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)

    text = " ".join(text.split())

    return text

# ==================================================
# EXTRACT TEXT FROM PDF
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
# SKILL EXTRACTION
# ==================================================

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS_DB:

        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))

# ==================================================
# SEMANTIC SIMILARITY
# ==================================================

def compute_similarity(resume, job):

    emb1 = model.encode([resume])

    emb2 = model.encode([job])

    score = cosine_similarity(emb1, emb2)[0][0]

    return round(float(score) * 100, 2)
