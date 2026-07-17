"""
Applikasi Python sederhana chatbot dengan gemini.
Chatbot dibuat melalui interaksi di terminal.

Cara jalankan:
>>> python app1.py
"""

import os
from getpass import getpass

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

GOOGLE_API_KEY = getpass("Please enter your Google API Key: ")

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


client = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

chat_history = [
    SystemMessage(
        "You are a helpful chatbot, reply to user chat in short message, max 1 paragraph."
    )
]

while True:
    user_prompt = input("User: ")
    chat_history.append(HumanMessage(user_prompt))
    response = client.invoke(chat_history)
    chat_history.append(response.text)
    print("AI:", response.text)
