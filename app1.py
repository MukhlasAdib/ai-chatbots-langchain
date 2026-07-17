import os
from getpass import getpass

from langchain_google_genai import ChatGoogleGenerativeAI

GOOGLE_API_KEY = getpass("Please enter your Google API Key: ")

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


client = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

response = client.invoke("Jelaskan apa itu AI?")
print(response.text)
