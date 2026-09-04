"""
Cara jalanin:

>>> streamlit run app2.py
"""

import streamlit as st
from langchain_groq import ChatGroq

st.title("My ChatBot")
st.markdown("Hello, this is my AI")

if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""

col1, col2 = st.columns([80, 20])
with col1:
    input_api_key = st.text_input(
        "API Key",
        type="password",
        label_visibility="collapsed",
        placeholder="Type your API key...",
    )
with col2:
    is_api_key_submitted = st.button(
        "Submit",
    )

if is_api_key_submitted:
    st.session_state["api_key"] = input_api_key

if st.session_state["api_key"] == "":
    st.stop()

client = ChatGroq(model="openai/gpt-oss-120b", api_key=st.session_state["api_key"])
response = client.invoke("What is AI")
st.markdown(response.content)
