# 🔍 AI Resume Analyzer — NLP & Semantic Search

> Going beyond keyword matching to understand the *meaning* of your resume.

![Python](https://img.shields.io/badge/Python-3.9+-0f2027?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Deployed-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 🚩 The problem

Most ATS (Applicant Tracking Systems) use **keyword matching**. This creates a serious flaw:

- Strong candidates get rejected because exact keywords are missing
- Candidates who copy-paste keywords get shortlisted without real understanding
- Recruiters waste hours manually screening resumes

---

## ✅ The solution

This project uses **Natural Language Processing** and **Semantic Similarity** to understand the *context and meaning* of resumes — not just scan for words.

```
"deep learning" ≈ "neural networks"   ← semantic search understands this
"deep learning" ≠ "neural networks"   ← keyword search misses this
```

---

## ⚙️ How it works

```
Resume PDF
    ↓
PDF Text Extraction  (PyPDF2)
    ↓
Text Cleaning & NLP Preprocessing  (spaCy)
    ↓
Skill Extraction
    ↓
Sentence Embedding Generation  (Sentence Transformers / HuggingFace)
    ↓
Cosine Similarity Calculation  (Scikit-learn)
    ↓
Skill Gap Analysis + Recommendations
    ↓
Streamlit Web App
```

---

## 🎯 Features

| Feature | Description |
|---|---|
| 📄 Resume Parsing | Extracts text directly from uploaded PDF resumes |
| 🧠 Semantic Matching | Transformer embeddings instead of keyword matching |
| 🔍 Skill Gap Analysis | Detects matched skills and missing skills |
| 💡 AI Recommendations | Suggests what to learn to improve job fit |
| 📊 Visualization | Charts for matched vs missing skills |
| ⚖️ Recruiter Verdict | Auto-classifies: Strong / Moderate / Low Match |

---

## 📊 Example output

```
Semantic Match Score:   82.4%
Verdict:                Strong Match ✅

Matched skills:   ['python', 'sql', 'pytorch', 'nlp']
Missing skills:   ['mlops', 'azure', 'rag']

Recommendation: Consider learning MLOps fundamentals and RAG pipelines
to significantly improve your match score for this role.
```

---

## 🛠️ Tech stack

| Category | Tools |
|---|---|
| Language | Python 3.9+ |
| NLP | spaCy, Sentence Transformers, HuggingFace |
| ML | Scikit-learn (cosine similarity) |
| Visualization | Matplotlib |
| Deployment | Streamlit |
| PDF Processing | PyPDF2 |

---

## 🚀 Run locally

```bash
# Clone the repo
git clone https://github.com/muneer-ahmad10/Resume-Analyzer.git
cd Resume-Analyzer

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📁 Project structure

```
Resume-Analyzer/
├── app.py              # Streamlit frontend
├── utils.py            # NLP pipeline & matching logic
├── requirements.txt    # Dependencies
└── README.md
```

---

## 🔮 Planned improvements

- [ ] LLM-powered resume feedback (GPT / Claude API)
- [ ] FAISS vector database for multi-resume ranking
- [ ] RAG pipeline integration
- [ ] Cloud deployment (Streamlit Cloud / HuggingFace Spaces)
- [ ] AI Interview Preparation Assistant
- [ ] Job recommendation engine

---

## 👨‍💻 Author

**Muneer Ahmad Dar**

AI/NLP Engineer · IIT Guwahati AIML Certification · BCA

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/muneerahmad-826363267)
[![GitHub](https://img.shields.io/badge/GitHub-0f2027?style=flat-square&logo=github&logoColor=white)](https://github.com/muneer-ahmad10)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:abrard855@gmail.com)
