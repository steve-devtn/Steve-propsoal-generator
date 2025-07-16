import streamlit as st
from openai import OpenAI
from io import BytesIO
from docx import Document

client = OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(page_title="Steve Proposal Generator", layout="centered")

st.title("Steve Proposal Generator")
st.subheader("Generate personalized freelance proposals with AI")

# Input fields in two columns
col1, col2 = st.columns(2)
with col1:
    client_name = st.text_input("Client's Name (optional)")
    project_budget = st.text_input("Project Budget (optional)")
with col2:
    timeline = st.text_input("Project Timeline (optional)")
    style = st.selectbox("Proposal Style", ["Formal", "Casual", "Technical", "Persuasive"])

job_description = st.text_area("Paste the job description here:")

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

def generate_prompt():
    return f"""
You are a professional freelancer writing a {style.lower()} proposal.

Job description: {job_description}

Client name: {client_name or 'N/A'}
Project budget: {project_budget or 'N/A'}
Project timeline: {timeline or 'N/A'}

Write a friendly, confident, and professional proposal addressing these details.
Keep it clear and persuasive.
"""

def proposal_to_docx(text):
    doc = Document()
    for line in text.split('\n'):
        doc.add_paragraph(line)
    f = BytesIO()
    doc.save(f)
    return f.getvalue()

def proposal_to_txt(text):
    return text.encode('utf-8')

proposal = ""

if st.button("Generate Proposal"):
    if not job_description.strip():
        st.warning("Please enter a job description.")
    else:
        with st.spinner("Generating proposal..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a professional freelancer writing proposals."},
                        {"role": "user", "content": generate_prompt()}
                    ],
                    temperature=0.7,
                    max_tokens=400,
                )
                proposal = response.choices[0].message.content.strip()
                st.success("✅ Proposal generated")
                st.session_state.history.append(proposal)
            except Exception as e:
                st.error(f"❌ Error generating proposal: {e}")

if proposal:
    st.markdown("---")
    st.markdown("### Generated Proposal:")
    st.markdown(proposal)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Copy to Clipboard"):
            st.experimental_set_query_params()
            st.toast("Copied to clipboard!")
            # Clipboard copy only works in the frontend. Use workaround or extensions if needed.

    with col2:
        st.download_button(
            label="Download as DOCX",
            data=proposal_to_docx(proposal),
            file_name="proposal.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    with col3:
        st.download_button(
            label="Download as TXT",
            data=proposal_to_txt(proposal),
            file_name="proposal.txt",
            mime="text/plain"
        )

if st.session_state.history:
    st.markdown("---")
    st.markdown("### Proposal History")
    for i, p in enumerate(reversed(st.session_state.history[-5:]), 1):
        st.markdown(f"**#{i}**:")
        st.markdown(p)
