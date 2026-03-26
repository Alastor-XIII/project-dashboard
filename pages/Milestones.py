import streamlit as st

if "project" not in st.session_state:
    st.warning("Please select project first")
    st.stop()

project = st.session_state["project"]
