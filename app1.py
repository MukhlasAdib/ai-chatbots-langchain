"""
Cara jalanin:

>>> python app1.py
"""

import os
from getpass import getpass

from langchain_groq import ChatGroq

GROQ_API_KEY = getpass("Please enter your Groq API Key: ")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

print()
prompt = input("User: ")
client = ChatGroq(model="openai/gpt-oss-120b")
response = client.invoke(prompt)

print("AI:", response.content)
