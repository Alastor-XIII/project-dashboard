import streamlit as st
import pandas as pd

st.title("📁 Projects Overview")

df = pd.read_excel("data/projects.xlsx")

for i, row in df.iterrows():
    col1, col2, col3, col4 = st.columns([3,2,2,1])

    col1.write(f"### {row['ProjectName']}")
    col2.write(f"Start: {row['Start']}")
    col3.write(f"Finish: {row['Finish']}")

    if col4.button("Open", key=i):
        st.session_state["project"] = row["ProjectID"]
        st.switch_page("pages/2_Project_Dashboard.py")
