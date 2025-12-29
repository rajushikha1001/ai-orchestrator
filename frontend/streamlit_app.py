import requests
import streamlit as st

st.title("AI Orchestrator Assistant")

API_URL = "http://localhost:8000/query"

user_input = st.text_area("Ask me anything:")

if st.button("Run"):
    with st.spinner("Thinking..."):
        res = requests.post(API_URL, json={"text": user_input})
        st.write(res.json()["response"])