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

from datetime import datetime

if submit:
    ...
    # Save to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"proposals/proposal_{timestamp}.txt", "w") as f:
        f.write(proposal)

✅ High-quality, customized {gig_type.lower()}  
✅ Fast delivery and unlimited revisions  
✅ 100% satisfaction guaranteed

Let’s get started — I’m ready when you are!

Best regards,  
Steve
"""
        st.success("✅ Proposal generated!")
        st.code(proposal, language="markdown")

from datetime import datetime

if submit:
    ...
    # Save to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"proposals/proposal_{timestamp}.txt", "w") as f:
        f.write(proposal)
