
import streamlit as st
import send_email
st.header("Contact Details")

with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address")
    user_message = st.text_area("Your message")
    message = user_message + "\n" + user_email
    button = st.form_submit_button("Submit")
    if button:
        send_email.send_email(message)
        st.info("Your email was sent successfully")