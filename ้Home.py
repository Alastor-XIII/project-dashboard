import streamlit as st

st.set_page_config(page_title="Project Dashboard", layout="wide")

pg = st.navigation([
    st.Page("pages/Projects_Overview.py", title="Projects Overview"),
    st.Page("pages/Project_Dashboard.py", title="Project Dashboard"),
    st.Page("pages/Timeline.py", title="Timeline"),
    st.Page("pages/Milestones.py", title="Milestones"),
    st.Page("pages/Resources.py", title="Resources"),
])

pg.run()
