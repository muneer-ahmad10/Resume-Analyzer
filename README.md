# 🚀 AI Resume Analyzer — NLP & Semantic Search

> An intelligent resume screening tool that goes beyond keyword matching using transformer-based semantic embeddings to understand the *meaning* behind resumes and job descriptions.

---

## 📌 Problem Statement

Traditional ATS (Applicant Tracking Systems) rely on keyword matching, which causes:

- Strong candidates rejected because exact keywords are missing
- Resumes with copied keywords passing without real understanding
- Recruiters spending significant time on manual screening

This project solves that with **NLP + Semantic Similarity** — understanding context, not just keywords.

---

## 🎯 What It Does

| Feature | Description |
|---|---|
| 📄 Resume Parsing | Extracts text from uploaded PDF resumes via PyPDF2 |
| 🧠 Semantic Matching | Uses `all-MiniLM-L6-v2` sentence transformer embeddings |
| ✅ Skill Extraction | Matches against a curated skills database |
| 📊 Skill Gap Analysis | Identifies matched vs. missing skills |
| 💡 Recommendations | Suggests learning resources for missing skills |
| 📈 Visualization | Bar chart of skill gap breakdown via Matplotlib |
| 🏆 Recruiter Verdict | Classifies as Strong / Moderate / Low match |

---

## 🧠 Core NLP Concepts

- Text Preprocessing & Token Cleaning
- Sentence Transformer Embeddings (`HuggingFace`)
- Cosine Similarity via `scikit-learn`
- Skill Extraction from a domain-specific skills database
- Embedding-based Information Retrieval

---

## ⚙️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| NLP / ML | Sentence Transformers, HuggingFace, spaCy, scikit-learn |
| PDF | PyPDF2 |
| Visualization | Matplotlib |
| UI / Deployment | Streamlit |

---

## 🏗️ Architecture

```
Resume PDF Upload
      ↓
PDF Text Extraction (PyPDF2)
      ↓
Text Cleaning & NLP Preprocessing
      ↓
Skill Extraction (Skills DB lookup)
      ↓
Sentence Embedding Generation (all-MiniLM-L6-v2)
      ↓
Cosine Similarity Calculation
      ↓
Skill Gap Analysis (Matched vs Missing)
      ↓
Recommendations + Verdict + Visualization
```

---

## 📂 Project Structure

```
Resume-Analyzer/
├── app.py              # Streamlit UI — upload, inputs, results display
├── utils.py            # Core logic — PDF extraction, embeddings, similarity, skills
├── requirements.txt    # Dependencies
└── README.md
```

### Key Functions in `utils.py`

| Function | Purpose |
|---|---|
| `extract_text_from_pdf(file)` | Reads all pages from uploaded PDF |
| `clean_text(text)` | Lowercases, removes punctuation, normalizes whitespace |
| `extract_skills(text)` | Matches text against `SKILLS_DB` list |
| `compute_similarity(resume, job)` | Generates embeddings and returns cosine similarity (0–100%) |

---

## 📊 Example Output

```
Semantic Match Score:   82.4%
Skill Match Score:      75.0%
Verdict:                Strong Match ✅

Matched Skills:  ['python', 'sql', 'pytorch', 'nlp']
Missing Skills:  ['mlops', 'azure', 'rag']

Recommendations:
  • MLOPS  → Learn model deployment and monitoring
  • AZURE  → Explore Azure AI Services
  • RAG    → Understand Retrieval-Augmented Generation
```

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/muneer-ahmad10/Resume-Analyzer.git
cd Resume-Analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
```

---

## 🔍 Why Semantic Search?

Traditional systems treat words as exact tokens:
```
"deep learning" ≠ "neural networks"   ← keyword mismatch → rejected
```

This project uses embeddings so the model understands:
```
deep learning ≈ neural networks       ← semantic match → correctly scored
```

---

## 🔮 Future Improvements

- [ ] LLM-powered personalized resume feedback
- [ ] FAISS vector database for faster similarity search
- [ ] Multi-resume batch ranking
- [ ] RAG pipeline integration
- [ ] Cloud deployment (Streamlit Cloud / HuggingFace Spaces)
- [ ] AI Interview Preparation Assistant
- [ ] Job recommendation engine

---

## 🧠 Key Learning Outcomes

- End-to-end NLP pipeline design
- Semantic search with transformer embeddings
- Streamlit app development
- Modular, production-oriented Python architecture
- Resume-job matching workflows

---

## 👨‍💻 Author

**Muneer Ahmad Dar** — AI Engineer  
Focus areas: NLP · LLMs · Semantic Search · Deep Learning · Generative AI

[![GitHub](https://img.shields.io/badge/GitHub-muneer--ahmad10-black?style=flat&logo=github)](https://github.com/muneer-ahmad10)
