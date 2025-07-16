import streamlit as st
import openai

# Set up page
st.set_page_config(page_title="Steve Proposal Generator", layout="centered")
st.title("Steve Proposal Generator")
st.subheader("Generate freelance proposals automatically")

# Access OpenAI key
openai.api_key = st.secrets["openai"]["api_key"]

# Input
job_description = st.text_area("Paste the job description here:")

# Generate proposal
if st.button("Generate Proposal"):
    if job_description.strip():
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional freelancer writing proposals."},
                {"role": "user", "content": f"Write a professional, friendly, and confident proposal for this job: {job_description}"}
            ]
        )
        proposal = response["choices"][0]["message"]["content"]
        st.success("✅ Proposal generated")
        st.text(proposal)
    else:
        st.warning("Please enter a job description.")
