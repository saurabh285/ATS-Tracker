from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Page Configuration
st.set_page_config(page_title="📄 ATS Resume Expert", layout="centered")

# Custom CSS for Compact Styling
st.markdown(
    """
    <style>
        /* Reduce font sizes for a compact design */
        h1 {font-size: 26px !important;}
        h2 {font-size: 22px !important;}
        h3 {font-size: 18px !important;}
        .stTextArea textarea {font-size: 13px !important;}
        .stButton>button {
            width: 100%;
            font-size: 14px !important;
            font-weight: bold;
            border-radius: 8px;
            padding: 6px;
        }
        .stFileUploader label {font-size: 14px !important;}
        .uploadedFile { 
            font-weight: bold;
            color: #4CAF50;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path="/usr/bin")
        first_page = images[0]

        # Convert to Bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format="JPEG")
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


# Function to get AI response
def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text

# App Header
st.title("📄 ATS Resume Expert")
st.markdown("#### Optimize your resume for ATS and boost your chances of getting hired!")

# Job Description Input
st.markdown("##### 🏢 **Enter Job Description**")
input_text = st.text_area("Paste the job description here:", key="input", height=120)

# Resume Upload
st.markdown("##### 📂 **Upload Your Resume (PDF)**")
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file:
    st.success("✅ Resume Uploaded Successfully!")

# UI Layout with Columns for Buttons
st.markdown("##### 🛠️ **Select an Analysis Option**")
col1, col2 = st.columns(2)

# Buttons with Updated Labels
with col1:
    submit1 = st.button("📊 Percentage Match", help="Check how well your resume matches the job description")
    submit2 = st.button("🔍 Keywords (Matching & Missing)", help="See which keywords your resume includes or lacks")

with col2:
    submit3 = st.button("📜 Overall Evaluation Report", help="Get a detailed analysis of your resume")
    submit4 = st.button("💡 Improve for Better Score", help="Receive actionable suggestions to improve your resume")

# Prompts for AI
input_prompt1 = """
You are an ATS scanner evaluating a resume against a job description. Provide:
1. **Match Percentage** (0-100%)
2. **Brief explanation** of how well the resume aligns with the job role.
"""

input_prompt2 = """
Analyze the resume and extract:
1. **Matching keywords** (found in both resume & job description).
2. **Missing keywords** (present in job description but not in resume).
3. **Suggestions to optimize the resume** based on missing keywords.
"""

input_prompt3 = """
You are an experienced HR Manager analyzing a resume. Provide:
1. **Strengths** - Key qualifications aligning with the job.
2. **Weaknesses** - Gaps or missing qualifications.
3. **Overall assessment** - How well the resume fits the job description.
4. **Final Verdict** - Strong, moderate, or weak alignment?
"""

input_prompt4 = """
You are a career coach helping candidates optimize their resumes. Provide:
1. **Skills & certifications** to add.
2. **Keyword optimization** for ATS-friendliness.
3. **Resume structuring tips** for better readability & parsing.
4. **Final improvement steps** to boost the match percentage.
"""

# Processing User Selection
if uploaded_file:
    pdf_content = input_pdf_setup(uploaded_file)

    if submit1:
        st.markdown("#### 📊 **Percentage Match**")
        with st.spinner("Analyzing Resume..."):
            response = get_gemini_response(input_text, pdf_content, input_prompt1)
            st.success("✅ Analysis Complete!")
            st.write(response)

    elif submit2:
        st.markdown("#### 🔍 **Keywords Analysis**")
        with st.spinner("Extracting Keywords..."):
            response = get_gemini_response(input_text, pdf_content, input_prompt2)
            st.success("✅ Keywords Processed!")
            st.write(response)

    elif submit3:
        st.markdown("#### 📜 **Overall Evaluation Report**")
        with st.spinner("Generating Report..."):
            response = get_gemini_response(input_text, pdf_content, input_prompt3)
            st.success("✅ Report Ready!")
            st.write(response)

    elif submit4:
        st.markdown("#### 💡 **Improvement Suggestions**")
        with st.spinner("Generating Recommendations..."):
            response = get_gemini_response(input_text, pdf_content, input_prompt4)
            st.success("✅ Recommendations Ready!")
            st.write(response)
