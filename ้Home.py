import streamlit as st
from utils.load_data import load_projects

projects = load_projects()

project_list = projects["Project"].unique()

selected_project = st.sidebar.selectbox("Select Project", project_list)

st.session_state["project"] = selected_project
