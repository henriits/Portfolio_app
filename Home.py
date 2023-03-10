import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("images/photo.png", width=200)

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

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f'[Source Code]({row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f'[Source Code]({row["url"]})')
