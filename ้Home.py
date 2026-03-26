import streamlit as st
from utils.load_data import load_projects

st.set_page_config(page_title="Project Dashboard", layout="wide")

st.title("📊 Project Portfolio Dashboard")

projects = load_projects()
project_list = projects["Project"].unique()

selected_project = st.sidebar.selectbox("Select Project", project_list)
st.session_state["project"] = selected_project
