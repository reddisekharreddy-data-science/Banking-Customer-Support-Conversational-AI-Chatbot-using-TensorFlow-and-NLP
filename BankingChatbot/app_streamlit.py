import streamlit as st
from chatbot_pipeline_tf import chatbot_response

st.title("🏦 Banking Customer Support Chatbot")

with st.spinner("Loading model… please wait (first time may take a few minutes)…"):
    pass

user_input = st.text_input("Ask your banking question:")

if st.button("Send"):
    if user_input.strip():
        reply = chatbot_response(user_input)
        st.write(reply)
