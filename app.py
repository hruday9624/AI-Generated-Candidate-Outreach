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
candidate_designation = st.text_input('Candidate_Designation', '')
candidate_details = st.text_area('Candidate_Details-Skills, Experience. (comma separated)', '')

# Dropdown menu for tone selection
st.subheader("Select the Tone of the Message:")
tone_options = ["Formal", "Friendly", "Persuasive", "Neutral"]
selected_tone = st.selectbox("Tone", tone_options)

# Buttons for message type
st.subheader("Select Message Type:")
col1, col2 = st.columns(2)
with col1:
    linkedin_invite = st.button("LinkedIn Invite")
with col2:
    email_invite = st.button("Email Invite")


