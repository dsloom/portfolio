import streamlit as st

st.set_page_config(layout = "wide")
col1,col2 = st.columns(2)


with col1:
    st.image("/Users/prithvy/pythonProject/app2_portfolio/venv/images/my_photo.png")

with col2:
    st.title("Prithvy Krishna")
    content =""" 
    I am Prithvy Krishna, B.Tech graduate, recently
    completed a Data Science Bootcamp, excelling in Python, 
    data analysis, and machine learning. Former IT Assistant,
    now dedicated to applying evolving data science skills to 
    meaningful projects. Eager to collaborate on opportunities
    aligning with my passion for technology and informed 
    decision-making. Let's connect for exciting possibilities.
    """
    st.info(content)