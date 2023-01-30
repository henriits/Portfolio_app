import streamlit as st
from send_email import send_email
import pandas


df = pandas.read_csv("topics.csv")


with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")

    options = df["topic"]
    topic = st.selectbox(
        'What topic do you want to discuss?',options)

    raw_message = st.text_area("Your message")

    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {topic}

{raw_message}
"""

    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")