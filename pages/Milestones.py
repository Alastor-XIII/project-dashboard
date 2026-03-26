import streamlit as st
import pandas as pd

st.title("🎯 Milestones")

project = st.session_state.get("project")

df = pd.read_excel("data/milestones.xlsx")
df = df[df["ProjectID"] == project]

st.dataframe(df)
