import streamlit as st

if "project" not in st.session_state:
    st.warning("Please select project from Home")
    st.stop()
project = st.session_state.get("project")

st.title(f"👷 Resources - {project}")

df = load_resources()
df = df[df["Project"] == project]

st.dataframe(df, use_container_width=True)

st.subheader("Resource Summary")

summary = df.groupby("Responsible")["Hours"].sum().reset_index()
st.dataframe(summary)
