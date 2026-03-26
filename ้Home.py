import streamlit as st
from utils.load_data import load_projects

st.set_page_config(page_title="Project Dashboard", layout="wide")

projects = load_projects()

project_list = projects["Project"].unique()
selected_project = st.sidebar.selectbox("Select Project", project_list)

st.session_state["project"] = selected_project

st.title("Project Portfolio Dashboard")

pg = st.navigation([
    st.Page("pages/Projects_Overview.py", title="Projects Overview"),
    st.Page("pages/Project_Dashboard.py", title="Project Dashboard"),
    st.Page("pages/Timeline.py", title="Timeline"),
    st.Page("pages/Milestones.py", title="Milestones"),
    st.Page("pages/Resources.py", title="Resources"),
])

pg.run()
