import os
import streamlit as st
from google import genai

MODEL = "gemini-3.1-pro-preview"

@st.cache_resource
def get_client():
    api_key = "Geminni 3.1 pro preview key"

    if not api_key:
        try:
            api_key = "Geminni 3.1 pro preview key"
        except:
            api_key = None

    if not api_key:
        st.error("❌ GEMINI_API_KEY not found")
        return None

    return genai.Client(api_key=api_key)


def call_gemini(prompt):
    client = get_client()
    if not client:
        return ""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text
