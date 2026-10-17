<div align="center">

# 📄 AI Resume Analyzer

### Semantic Similarity and Skill Matching for Resumes and Job Descriptions

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Sentence Transformers](https://img.shields.io/badge/Sentence_Transformers-all--MiniLM--L6--v2-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

</div>

---

An NLP-powered Streamlit application that compares resumes with job descriptions using semantic similarity and skill matching to identify relevant skills, gaps, and improvement areas.

## 📑 Table of Contents

- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [How It Works](#-how-it-works)
- [Evaluation Evidence](#-evaluation-evidence)
- [Example Output](#-example-output)
- [Installation](#-installation)
- [Limitations](#️-limitations)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## ✨ Features

| Feature | Description |
|:--|:--|
| 📄 **PDF Resume Parsing** | Extracts resume text using PyPDF2. |
| 🧬 **Semantic Similarity** | Uses Sentence Transformers (`all-MiniLM-L6-v2`) and cosine similarity to compare resumes with job descriptions. |
| 🏷️ **Skill Extraction** | Identifies supported technical skills using keyword matching and aliases. |
| 🎯 **Match Score** | Combines semantic similarity (40%) and required-skill coverage (60%) into a custom Resume–Job Match Score. |
| 🔍 **Skill Gap Analysis** | Displays matched and missing skills. |
| 📚 **Learning Recommendations** | Suggests learning resources or technologies for identified skill gaps. |
| 📊 **Visual Analytics** | Presents scores, skill comparisons, and a match chart through Streamlit. |

---

## 🛠️ Tech Stack

| Category | Tools |
|:--|:--|
| **Language** | Python |
| **Web app** | Streamlit |
| **PDF parsing** | PyPDF2 |
| **Embeddings** | Sentence Transformers |
| **Machine learning** | Scikit-learn |
| **Data handling** | Pandas |
| **Visualization** | Matplotlib |
| **Text processing** | Regular Expressions (Regex) |

---

## ⚙️ How It Works

| Step | Stage |
|:--:|:--|
| **1** | Upload a resume in PDF format. |
| **2** | Paste the target job description. |
| **3** | Extract and preprocess text from both inputs. |
| **4** | Calculate semantic similarity using sentence embeddings and cosine similarity. |
| **5** | Detect supported skills and identify matches and gaps. |
| **6** | Calculate the custom match score and display recommendations. |

### 🧮 Scoring Method

The application calculates:

**Skill Coverage**

`(Matched Required Skills / Detected Required Skills) × 100`

**Resume–Job Match Score**

`(Semantic Similarity × 0.40) + (Skill Coverage × 0.60)`

> The score is a custom heuristic, not an official ATS score or a validated hiring probability. Results depend on the skill dictionary, text extraction, and job description.

---

## 🧪 Evaluation Evidence

The skill extraction function was tested against nine predefined cases covering:

- Exact skill matches and uppercase text
- Word-boundary matching to reduce false positives
- REST API aliases
- Scikit-learn spelling variations
- NLP and PyTorch aliases
- Text with no supported skills
- Empty input
- RAG, semantic search, and transformers

**Observed results on the nine test cases:**

| Metric | Result |
|:--|--:|
| Exact-match test cases passed | 9/9 |
| Precision | 1.00 |
| Recall | 1.00 |
| F1-score | 1.00 |
| Exact-match accuracy | 100% |

> ⚠️ **Important:** These results apply only to the predefined test cases. They do not establish real-world accuracy across arbitrary resumes or job descriptions.

---

## 📊 Example Output

In one test using a resume and an AI/ML Engineer job description, the application reported:

| Metric | Result |
|:--|--:|
| Semantic similarity | 70.51% |
| Required-skill coverage | 60.00% |
| **Resume–Job Match Score** | **64.20%** |
| Matched required skills | 12 out of 20 |

The application also displayed missing skills, learning recommendations, and a match visualization. These figures are from one test, not a general performance benchmark.

---

## 🚀 Installation

```bash
git clone https://github.com/muneer-ahmad10/Resume-Analyzer.git
cd Resume-Analyzer
pip install -r requirements.txt
streamlit run app.py
```

---

## ⚠️ Limitations

| Area | Limitation |
|:--|:--|
| **Skill detection** | Depends on the supported skill dictionary and aliases. |
| **Scanned PDFs** | May require OCR if text cannot be extracted. |
| **Match score** | Heuristic and should not replace human resume review. |
| **Recommendations** | Rule-based rather than personalized AI-generated advice. |
| **Evaluation** | Currently covers nine predefined skill-extraction test cases. |

---

## 🔮 Future Improvements

- [ ] Expand skill aliases and job-role-specific skill dictionaries.
- [ ] Improve error handling for empty, invalid, and scanned PDFs.
- [ ] Evaluate performance on a larger, manually reviewed resume–job dataset.
- [ ] Improve recommendations using job requirements and candidate experience.

---

## 👨‍💻 Author

<div align="center">

**Muneer Ahmad Dar**

[![GitHub](https://img.shields.io/badge/GitHub-muneer--ahmad10-181717?style=for-the-badge&logo=github)](https://github.com/muneer-ahmad10)
[![Project](https://img.shields.io/badge/Project-Resume--Analyzer-blue?style=for-the-badge&logo=github)](https://github.com/muneer-ahmad10/Resume-Analyzer)

</div>

- GitHub: https://github.com/muneer-ahmad10
- Project: https://github.com/muneer-ahmad10/Resume-Analyzer
