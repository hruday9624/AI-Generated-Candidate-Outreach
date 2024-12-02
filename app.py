import streamlit as st
import google.generativeai as genai

# App header
st.header("Candidate Outreach Using Ai")

# Retrieve the API key from Streamlit secrets
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]

# Configure the Google Generative AI API with your API key
genai.configure(api_key=GOOGLE_API_KEY)

# Input field for the medicine name
st.subheader("Enter Candidate Details:")
candidate_name = st.text_input('Candidate Name', '')
#st.subheader("Enter Candidate Designation:")
candidate_designation = st.text_input('Candidate_Designation', '')
#st.subheader("Enter Candidate Details:")
candidate_details = st.text_area('Candidate_Details', '')




