import streamlit as st
from datetime import datetime

st.title("Steve Proposal Generator")

gig_type = st.selectbox("Select gig type", ["Graphic Design", "Writing", "Programming", "Marketing", "Other"])

client_request = st.text_area("Client request")

if st.button("Generate Proposal"):
    if not client_request.strip():
        st.warning("Please enter the client request.")
    else:
        proposal = f"""
Hello 👋,

Thank you for your interest in my {gig_type.lower()} services.

Based on your request, here’s what I can offer:

✅ High-quality, customized {gig_type.lower()}  
✅ Fast delivery and unlimited revisions  
✅ 100% satisfaction guaranteed

Let’s get started — I’m ready when you are!

Best regards,  
Steve
"""
        st.success("✅ Proposal generated!")
        st.code(proposal, language="markdown")

        # Save proposal to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"proposals/proposal_{timestamp}.txt", "w") as f:
            f.write(proposal)

import streamlit as st

def generate_proposal(gig_title: str) -> str:
    return f"""Hello,

I’m very interested in your project: "{gig_title}".
With my experience and skills, I guarantee quality, on-time delivery, and clear communication.
Let’s discuss your requirements and get started!

Best regards,
Steve
"""

st.title("Steve Proposal Generator")

gig_title = st.text_input("Enter Fiverr gig title:")

if gig_title:
    proposal = generate_proposal(gig_title)
    st.subheader("Generated Proposal:")
    st.write(proposal)

