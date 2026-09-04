"""
Cara jalanin:

>>> streamlit run app2.py
"""

import streamlit as st

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

st.markdown("API Key: " + st.session_state["api_key"])
temp_button = st.button("Click me to start")
