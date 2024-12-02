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
candidate_designation = st.text_input('Candidate Designation', '')
candidate_details = st.text_input('Candidate Details- Skills, Experience. (comma separated)', '')
job_description = st.text_area('Your Job Description: ', '')

# Dropdown menu for tone selection
st.subheader("Select the Tone of the Message:")
tone_options = ["Formal", "Friendly", "Persuasive", "Neutral"]
selected_tone = st.selectbox("Tone", tone_options)

# Buttons for message type
st.subheader("Select Message Type:")
col1, col2, col3 = st.columns(3)
with col1:
    linkedin_invite = st.button("LinkedIn Invite")
with col2:
    email_invite = st.button("Email Invite")
with col3:
    whatsapp_invite = st.button("Whatsapp Invite")

# Generate message based on input
if linkedin_invite or email_invite or whatsapp_invite:
    if not candidate_name or not candidate_designation or not candidate_details or not job_description:
        st.error("Please fill in all the above details before proceeding.")
    else:
        if linkedin_invite:
            message_type = "LinkedIn Invite"
        elif email_invite:
            message_type = "Email Invite"
        else:
            message_type = "WhatsApp Invite"
        st.info(f"Generating {message_type}...")




