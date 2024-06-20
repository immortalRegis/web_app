import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')


col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("shegs")
    content = """
        I am a beginner python developer.
    """

    st.info(content)
content2 = "Below are some of my projects. Feel free to contact me"
st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
