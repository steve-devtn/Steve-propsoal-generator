import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai"]["api_key"])

st.title("Steve Proposal Generator")
st.subheader("Generate freelance proposals automatically")

job_description = st.text_area("Paste the job description here:")

if st.button("Generate Proposal"):
    if job_description.strip():
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional freelancer writing proposals."},
                {"role": "user", "content": f"Write a professional proposal for this job: {job_description}"}
            ]
        )
        proposal = response.choices[0].message.content
        st.success("✅ Proposal generated")
        st.text(proposal)
    else:
        st.warning("Please enter a job description.")
