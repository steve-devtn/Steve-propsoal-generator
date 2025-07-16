import streamlit as st

st.set_page_config(page_title="Steve Proposal Generator", layout="centered")

st.title("🧠 Steve Proposal Generator")
st.write("Create custom proposals for Fiverr clients instantly.")

# Input fields
gig_type = st.selectbox("Select Gig Type", [
    "Logo Design", "Web Development", "SEO Services", "Video Editing", "Translation"
])

client_request = st.text_area("Client Request or Requirements")

if st.button("Generate Proposal"):
    if not client_request.strip():
        st.warning("Please enter the client request.")
    else:
        # Simple prompt logic (Shadow AI style)
        proposal = f"""
Hello 👋,

Thank you for your interest in my {gig_type.lower()} services.

Based on your request, here’s what I can offer:

✅ High-quality, customized {gig_type.lower()}  
✅ Fast delivery and unlimited revisions  
✅ 100% satisfaction guaranteed

Let’s
