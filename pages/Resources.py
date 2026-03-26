import streamlit as st
from utils.load_data import load_resources

project = st.session_state.get("project")

st.title(f"👷 Resources - {project}")

df = load_resources()
df = df[df["Project"] == project]

st.dataframe(df, use_container_width=True)

st.subheader("Resource Summary")

summary = df.groupby("Responsible")["Hours"].sum().reset_index()
st.dataframe(summary)
