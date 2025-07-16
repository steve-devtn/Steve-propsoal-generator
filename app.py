import streamlit as st

st.set_page_config(page_title="Steve Proposal Generator", layout="centered")

st.title("Steve Proposal Generator")
st.subheader("Generate freelance proposals automatically")

job_description = st.text_area("Paste the job description here:")
if st.button("Generate Proposal"):
    if job_description.strip():
        st.success("✅ Proposal generated (placeholder)")
        st.text("Dear client, ... [AI will generate this part]")
    else:
        st.warning("Please paste a job description.")
