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
if os.environ.get("GOOGLE_API_KEY") is None:
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

    if is_api_key_submitted and api_key != "":
        os.environ["GOOGLE_API_KEY"] = api_key
    if os.environ.get("GOOGLE_API_KEY") is None:
        st.stop()

### Kolom Chat ###
# Bikin chat history kosong jika belum ada
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Tampilkan chat history yang ada selama ini
for chat in st.session_state["chat_history"]:
    with st.chat_message("User"):
        st.markdown(chat)

# Minta prompt dari user
user_prompt = st.chat_input("Ask AI")
if not user_prompt:
    st.stop()
st.session_state["chat_history"].append(user_prompt)

# Tampilkan prompt dari user
with st.chat_message("User"):
    st.markdown(user_prompt)
