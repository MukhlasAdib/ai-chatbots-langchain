"""
Cara jalanin:

>>> python app1.py
"""

import os
from getpass import getpass

from langchain_google_genai import ChatGoogleGenerativeAI

GOOGLE_API_KEY = getpass("Please enter your Google API Key: ")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

print()
prompt = input("User: ")
client = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
response = client.invoke(prompt)

print("AI:", response.content)
