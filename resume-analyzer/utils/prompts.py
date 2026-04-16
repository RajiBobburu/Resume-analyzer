GENERATE_RESUME_PROMPT = """
You are an expert resume writer.

Job Description:
{jd_text}

Candidate Resume:
{resume_text}

TASK:
1. Analyze job description
2. Identify missing skills
3. Improve resume professionally
4. Expand experience with strong bullet points
5. Keep content realistic

Return STRICT JSON:

{{
"name": "",
"email": "",
"phone": "",
"location": "",
"summary": "",
"skills": [],
"experience": [
  {{
    "role": "",
    "company": "",
    "duration": "",
    "bullets": []
  }}
],
"projects": [
  {{
    "title": "",
    "description": ""
  }}
],
"education": [
  {{
    "degree": "",
    "institution": ""
  }}
]
}}
"""