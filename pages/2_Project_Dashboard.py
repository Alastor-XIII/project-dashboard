import streamlit as st

if "project" not in st.session_state:
    st.warning("Please select project from Home")
    st.stop()
project = st.session_state.get("project")

st.title(f"📊 Project Dashboard - {project}")

df = load_activities()
df = df[df["Project"] == project]

progress = df["Progress"].mean()
total_tasks = len(df)
delay_tasks = len(df[df["Status"] == "Delay"])

col1, col2, col3 = st.columns(3)

col1.metric("Progress", f"{progress:.1f}%")
col2.metric("Total Tasks", total_tasks)
col3.metric("Delayed Tasks", delay_tasks)

st.dataframe(df, use_container_width=True)
