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
