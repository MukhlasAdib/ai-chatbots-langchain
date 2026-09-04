"""
Cara jalanin:

>>> streamlit run app1.py
"""

import streamlit as st

st.title("Adib App")
st.markdown("Nama saya Adib")

pressed = st.button("Click me")

if pressed:
    st.slider("Umurmu berapa?", min_value=0, max_value=100)
