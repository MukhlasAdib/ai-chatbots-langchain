"""
Applikasi streamlit chatbot + RAG idea
"""

import os

import streamlit as st
from langchain.messages import AIMessage
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

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
        st.rerun()
    if os.environ.get("GOOGLE_API_KEY") is None:
        st.stop()

client = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

### Kolom Chat ###
# Bikin chat history kosong jika belum ada
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        SystemMessage(
            "You are a helpful chatbot, reply to user chat in short message, max 1 paragraph."
        )
    ]

# Button untuk upload document
# ...

# Dokumennya di masukin ke vector DB
# extract text -> chunking jika ukuran besar -> masukin vector

# Tampilkan chat history yang ada selama ini
for chat in st.session_state["chat_history"]:
    if type(chat) is SystemMessage:
        continue
    elif type(chat) is HumanMessage:
        role = "User"
    elif type(chat) is AIMessage:
        role = "AI"
    with st.chat_message(role):
        st.markdown(chat.text)

# Minta prompt dari user
user_prompt = st.chat_input("Ask AI")
if not user_prompt:
    st.stop()
st.session_state["chat_history"].append(HumanMessage(user_prompt))

# Tampilkan prompt dari user
with st.chat_message("User"):
    st.markdown(user_prompt)

# Lakukan retrieval
# query vector database dengan user prompt
# ambil beberapa chunk yang paling relevan
# bikin prompt dari template
# Masukkan prompt template ke chat history

# Invoke ke AI, ambil response-nya
response = client.invoke(st.session_state["chat_history"])
st.session_state["chat_history"].append(response)

# Tampilkan response AI
with st.chat_message("AI"):
    st.markdown(response.text)
