import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300,)


with col2:
    st.title("Henri Tsarents")
    content = """
    Hi , I am Henri. 
    
    I am a junior Python programmer, currently learning how to make 
    web apps with python. Also learning web development. 
    
    I started my journey as a programmer at 2022 september 
    in Software Development Academy.
    Simultaneously pushing my way through numerous Udemy boot camps.
    
    
    """
    st.info(content)

st.text("Below you can find some of the apps i have built in Python. Feel free to contact me!")