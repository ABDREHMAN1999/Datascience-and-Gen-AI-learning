import streamlit as st

st.title("Streamlit Demo")

st.write("This is a streamlit demo")

name = st.text_input("Enter your name: ")
st.button('Enter')
st.write(name)