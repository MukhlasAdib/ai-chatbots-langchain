"""
Cara jalanin:

>>> python app1.py
"""

import os
from getpass import getpass

from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq

GROQ_API_KEY = getpass("Please enter your Groq API Key: ")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

print()
chat_history = []

while True:
    prompt = input("User: ")
    chat_history.append(HumanMessage(prompt))
    client = ChatGroq(model="openai/gpt-oss-120b")
    response = client.invoke(prompt)
    chat_history.append(response)
    print("AI:", response.content)
