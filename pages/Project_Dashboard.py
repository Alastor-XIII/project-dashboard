import streamlit as st
import pandas as pd

st.title("📊 Project Dashboard")

project = st.session_state.get("project")

df = pd.read_excel("data/activities.xlsx")
df = df[df["ProjectID"] == project]

progress = df["Progress"].mean()

st.metric("Overall Progress", f"{progress:.1f}%")
st.metric("Total Activities", len(df))
st.metric("Completed Tasks", len(df[df["Progress"]==100]))
