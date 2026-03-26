import streamlit as st
from utils.load_data import load_projects, load_activities

st.title("📊 Project Dashboard")

projects = load_projects()
activities = load_activities()

project_list = projects["Project"].unique()
selected_project = st.selectbox("Select Project", project_list)

proj_data = projects[projects["Project"] == selected_project]
act_data = activities[activities["Project"] == selected_project]

st.subheader("Project Info")
st.dataframe(proj_data)

st.subheader("Activities")
st.dataframe(act_data)

progress = act_data["Progress"].mean()
st.progress(int(progress))
st.write(f"Overall Progress: {progress:.2f}%")
