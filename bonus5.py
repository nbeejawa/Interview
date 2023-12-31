import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1: 
    st.image("images/photo.png")

with col2:
    st.title("Nikhar Beejawat")
    content = """
    I am a Python Programmer. Learning To explore more areas
    """
    st.info(content)

col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")



content = """
    I am a Python Programmer. Working on the the content added
    to show how you are performing the task assigned to modify
    certain app
    """
st.write(content)