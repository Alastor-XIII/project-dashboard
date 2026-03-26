import streamlit as st

if "project" not in st.session_state:
    st.warning("Please select project from Home")
    st.stop()

st.title("📁 Projects Overview")

df = load_projects()

col1, col2, col3 = st.columns(3)

col1.metric("Total Projects", len(df))
col2.metric("Active Projects", len(df[df["Status"] == "Active"]))
col3.metric("Completed", len(df[df["Status"] == "Completed"]))

st.dataframe(df, use_container_width=True)
