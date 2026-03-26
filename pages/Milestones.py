import streamlit as st
from utils.load_data import load_milestones

if "project" not in st.session_state:
    st.warning("Please select project from Home")
    st.stop()

project = st.session_state["project"]

st.title(f"Milestones - {project}")

df = load_milestones()
df = df[df["Project"] == project]

st.dataframe(df)
