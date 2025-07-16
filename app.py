import streamlit as st
from openai import OpenAI
import streamlit_authenticator as stauth

# User credentials (example)
users = {
    "hyper": {
        "name": "Hyper",
        "password": "hashed_password_here"  # use stauth.Hasher to hash your password
    }
}

# Hashed passwords example (generate once)
# import streamlit_authenticator as stauth
# hashed_passwords = stauth.Hasher(['your_password']).generate()
# print(hashed_passwords)

# Setup authenticator
authenticator = stauth.Authenticate(
    users,
    "steve_proposal_generator",
    "abcdef",  # cookie key
    cookie_expiry_days=30
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    client = OpenAI(api_key=st.secrets["openai"]["api_key"])
    st.set_page_config(page_title="Steve Proposal Generator", layout="centered")
    st.title(f"Welcome {name}")
    st.subheader("Generate personalized freelance proposals with AI")

    client_name = st.text_input("Client's Name (optional)")
    project_budget = st.text_input("Project Budget (optional)")
    timeline = st.text_input("Project Timeline (optional)")
    style = st.selectbox("Proposal Style", ["Formal", "Casual", "Technical", "Persuasive"])
    job_description = st.text_area("Paste the job description here:")

    if st.button("Generate Proposal"):
        if not job_description.strip():
            st.warning("Please enter a job description.")
        else:
            prompt = f"""
You are a professional freelancer writing a {style.lower()} proposal.

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

    authenticator.logout("Logout", "sidebar")

elif authentication_status is False:
    st.error("Username/password is incorrect")
elif authentication_status is None:
    st.warning("Please enter your username and password")
