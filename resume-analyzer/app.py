import streamlit as st
from utils.gemini_client import call_gemini
from utils.extractor import extract_pdf, extract_docx
from utils.scraper import scrape_url
from utils.prompts import GENERATE_RESUME_PROMPT
from utils.parser import safe_json
from utils.pdf_generator import build_resume_pdf

st.set_page_config(page_title="Resume Analyzer", layout="wide")

st.title("📄 AI Resume Generator")

jd = st.text_area("Paste Job Description")
jd_link = st.text_input("Or paste Job Description URL")
resume = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if st.button("Generate Resume"):
    if not (jd or jd_link) or not resume:
        st.warning("Provide Job Description and Resume")
        st.stop()

    # JD extraction
    if jd_link:
        jd_text = scrape_url(jd_link)
    else:
        jd_text = jd

    # Resume extraction
    file_bytes = resume.read()
    if resume.name.endswith(".pdf"):
        resume_text = extract_pdf(file_bytes)
    else:
        resume_text = extract_docx(file_bytes)

    with st.spinner("Generating your resume..."):
        prompt = GENERATE_RESUME_PROMPT.format(
            jd_text=jd_text,
            resume_text=resume_text
        )

        response = call_gemini(prompt)
        final_data = safe_json(response)

    if not final_data:
        st.error("⚠️ Failed to generate resume. Try again.")
        st.stop()

    st.success("✅ Your resume is ready!")

    # Generate PDF
    pdf_bytes = build_resume_pdf(final_data)

    st.download_button(
        "⬇ Download Resume PDF",
        data=pdf_bytes,
        file_name="generated_resume.pdf",
        mime="application/pdf"
    )