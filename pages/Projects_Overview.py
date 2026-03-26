import streamlit as st
from utils.load_data import load_projects

st.title("📁 Projects Overview")

df = load_projects()

col1, col2, col3 = st.columns(3)

col1.metric("Total Projects", len(df))
col2.metric("Active Projects", len(df[df["Status"] == "Active"]))
col3.metric("Completed", len(df[df["Status"] == "Completed"]))

st.dataframe(df, use_container_width=True)
