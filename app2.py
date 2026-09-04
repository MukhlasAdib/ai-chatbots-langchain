"""
Cara jalanin:

>>> streamlit run app2.py
"""

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq

st.title("My ChatBot")
st.markdown("Hello, this is my AI")

if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""

if st.session_state["api_key"] == "":
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
        st.rerun()

if st.session_state["api_key"] == "":
    st.stop()

client = ChatGroq(model="openai/gpt-oss-120b", api_key=st.session_state["api_key"])
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        SystemMessage("You are a comedian, but smart. Always reply with a joke.")
    ]
chat_history = st.session_state["chat_history"]

for chat_msg in chat_history:
    if type(chat_msg) == HumanMessage:
        role = "User"
    elif type(chat_msg) == AIMessage:
        role = "AI"
    else:
        continue
    with st.chat_message(role):
        st.markdown(chat_msg.content)

user_prompt = st.chat_input("Ask AI")
if not user_prompt:
    st.stop()
chat_history.append(HumanMessage(user_prompt))
with st.chat_message("User"):
    st.markdown(user_prompt)

response = client.invoke(chat_history)
chat_history.append(response)

with st.chat_message("AI"):
    st.markdown(response.content)
