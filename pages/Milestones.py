import streamlit as st

if "project" not in st.session_state:
    st.warning("Please select project from Home")
    st.stop()

project = st.session_state.get("project")

st.title(f"🏁 Milestones - {project}")

df = load_milestones()
df = df[df["Project"] == project]

st.dataframe(df, use_container_width=True)

completed = len(df[df["Status"] == "Done"])
total = len(df)

if total > 0:
    percent = (completed / total) * 100
else:
    percent = 0

st.progress(int(percent))
st.write(f"{percent:.1f}% Complete")
