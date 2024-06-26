import streamlit as st
import send_email

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input('Enter your email address')
    inquiry = st.selectbox(label="What do you want to discuss?",
                           options=['Job Inquiries', 'Project Proposal', 'Others'])
    raw_message = st.text_area('Your message')
    button = st.form_submit_button()

    message = f'''\
Subject: New Email from {user_email}

From: {user_email}
Topic: {inquiry}
{raw_message}
    '''

    if button:
        send_email.send_new_email(message)
        st.info("Your message was sent successfully.")
        print(message)
