import streamlit as st

if "project" not in st.session_state:
    st.warning("Please select project from Projects Overview")
    st.stop()

project = st.session_state["project"]
