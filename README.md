# AI Resume Analyzer (GenAI Powered)
An AI-powered Resume Analyzer and Generator that creates tailored, job-specific resumes using Google Gemini 3.1 Pro and exports them as downloadable PDFs.
---
##  Overview
This application allows users to input a job description (text or URL) and upload their existing resume (PDF/DOCX).  
It then analyzes both inputs using a Large Language Model and generates a professionally optimized resume aligned with the job requirements.
The final output is a clean, ATS-friendly resume available for direct download in PDF format.
---
## Features
- Accept Job Description via text or URL
- Upload Resume (PDF / DOCX)
- AI-powered resume optimization (Gemini 3.1 Pro)
- Skill gap identification and enhancement
- Improved experience bullet points
- Direct PDF resume generation
- Simple and clean Streamlit UI
---
## Tech Stack
- **Python**
- **Streamlit**
- **Google GenAI (Gemini 3.1 Pro Preview)**
- **pdfplumber / docx2txt** (resume parsing)
- **BeautifulSoup** (web scraping)
- **ReportLab** (PDF generation)
---
## How to Run Locally

### 1️. Clone Repository
### 2️. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️. Set API Key
```bash
set GEMINI_API_KEY=your_api_key
```
### 4️. Run Application
```bash
python -m streamlit run app.py
```
### Use Cases
- Resume optimization for job applications
- ATS-friendly resume generation
- Skill gap identification
- Rapid resume customization for multiple roles
---
### Limitations
- Depends on AI response quality
- Some job portals may restrict scraping
- Requires active Gemini API access
---
### Demo

<img width="1771" height="785" alt="image" src="https://github.com/user-attachments/assets/cb48675f-78ba-4e41-8339-6ad199cdaedc" />

Author : Raji Bobburu








