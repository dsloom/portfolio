import streamlit as st
import pandas as pd

st.set_page_config(layout ="wide")
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
content2 = """

 Below you can find some of the apps I have built in Python. Feel free to contact me!
 """
st.write(content2)

col3,empty_col,col4 =st.columns([1.5,0.5,1.5])

df = pd.read_csv("/Users/prithvy/pythonProject/app2_portfolio/venv/data.csv",sep=";" )
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("/Users/prithvy/pythonProject/app2_portfolio/venv/images/"+ row["image"])
        st.write(f"[sourcecode]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("/Users/prithvy/pythonProject/app2_portfolio/venv/images/"+ row["image"])
        st.write(f"[sourcecode]({row['url']})")