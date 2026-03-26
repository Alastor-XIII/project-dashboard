import streamlit as st
from utils.load_data import load_milestones

st.title("🏁 Milestones")

df = load_milestones()

project = st.selectbox("Select Project", df["Project"].unique())
df = df[df["Project"] == project]

st.dataframe(df, use_container_width=True)

st.subheader("Milestone Progress")

completed = len(df[df["Status"] == "Done"])
total = len(df)

if total > 0:
    percent = (completed / total) * 100
else:
    percent = 0

st.progress(int(percent))
st.write(f"{percent:.1f}% Complete")
