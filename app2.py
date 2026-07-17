"""
Applikasi streamlit chatbot

Cara jalankan:
>>> streamlit run app2.py
"""

import streamlit as st

st.title("Adib Chatbot")
st.markdown("Hi! Saya adib. Silahkan chat dengan AI assistant saya ya...")

nama = st.text_input("Nama: ")
st.markdown(f"Halo {nama}!")

is_pressed = st.button("Tekan Untuk Keluarin Balon")
if is_pressed:
    st.balloons()
