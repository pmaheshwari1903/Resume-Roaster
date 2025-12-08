import streamlit as st
from dotenv import load_dotenv
import PyPDF2
import io
import os
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

st.title("Resume Roaster")
st.divider()
file = st.file_uploader("Upload your Resume file here (pdf or txt files only)", type=["pdf", "txt"])
role = st.text_input("Enter the Job role you're targetting: ")
analyze = st.button("Analyze")

def pdf_data_extraction(file_byte):
    reader = PyPDF2.PdfReader(file_byte)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def extract_data_from_file(file):
    file_type = file.type
    
    if file_type == "application/pdf":
        with io.BytesIO(file.read()) as file_byte:
            return pdf_data_extraction(file_byte)
    elif file_type == "text/plain":
        return file.read().decode("utf-8")

if analyze and file:
    try:
        file_content = extract_data_from_file(file)
        
        if not file_content or not file_content.strip():
            st.error("File does not have any content")
            st.stop()
            
        prompt = f""" You are an experienced HR reviewer who is candid, sarcastic and brutally honest but inevitably constructive. Roast this resume like a sharp stand-up bit (witty, sarcastic), BUT always include:
        1) top 5 actionable improvements (bulleted),
        2) 2 strengths to keep,
        3) a suggested one-line rewrite for the resume summary.
        Keep overall length between 200 and 300 words.
        Respond in English. Be harsh and direct but do NOT encourage self-harm or demeaning language that attacks protected attributes.
        Role: {role or 'N/A'}
        Resume (begin):
        {file_content}
        Resume (end).
        Give the roast and then the actionable bullets.
        """
        
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        st.markdown("### ANALYSIS RESULT")
        st.markdown(response.text)
    except Exception as e:
        st.error("An Error Occured!")
