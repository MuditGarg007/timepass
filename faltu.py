import streamlit as st

st.set_page_config(page_title= "Final Project", page_icon = "💩", layout="wide")

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

st.header("High Tech AI Model")
st.subheader("Enter your details")

name = st.text_input("Enter your name")

age = st.number_input("Enter age", 0)

if(st.button("Submit ✅")):
    st.write("Your name is " , name, " and your age is", str(age))