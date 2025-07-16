import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

# Page setup
st.set_page_config(page_title="Steve Proposal Generator", layout="centered")
st.title("Steve Proposal Generator")
st.subheader("Generate personalized freelance proposals with AI")

# Input fields
client_name = st.text_input("Client's Name (optional)")
project_budget = st.text_input("Project Budget (optional)")
timeline = st.text_input("Project Timeline (optional)")
job_description = st.text_area("Paste the job description here:")

# Generate button
if st.button("Generate Proposal"):
    if not job_description.strip():
        st.warning("Please enter a job description.")
    else:
        prompt = f"""
You are a professional freelancer writing a proposal.

Job description: {job_description}

Client name: {client_name or 'N/A'}
Project budget: {project_budget or 'N/A'}
Project timeline: {timeline or 'N/A'}

Write a friendly, confident, and professional proposal addressing these details.
Keep it clear and persuasive.
"""

        with st.spinner("Generating proposal..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a professional freelancer writing proposals."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=400,
                )
                proposal = response.choices[0].message.content.strip()
                st.success("✅ Proposal generated")
                st.text_area("Your Proposal", value=proposal, height=300)
            except Exception as e:
                st.error(f"❌ Error generating proposal: {e}")
