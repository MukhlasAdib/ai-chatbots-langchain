"""
Applikasi streamlit chatbot

Cara jalankan:
>>> streamlit run app2.py
"""

import os

import streamlit as st

st.title("Adib Chatbot")
st.markdown("Hi! Saya adib. Silahkan chat dengan AI assistant saya ya...")

### API Key processing ###
st.markdown("API Key")
col1, col2 = st.columns([0.8, 0.2])
with col1:
    api_key = st.text_input(
        "API Key",
        type="password",
        label_visibility="collapsed",
        placeholder="Type your API key...",
    )
with col2:
    is_api_key_submitted = st.button(
        "Submit",
    )
GOOGLE_API_KEY = ""
if is_api_key_submitted and api_key != "":
    os.environ["GOOGLE_API_KEY"] = api_key

if os.environ.get("GOOGLE_API_KEY") is None:
    st.stop()

st.markdown("API Key sudah ada")
