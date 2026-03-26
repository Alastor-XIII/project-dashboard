import streamlit as st
from utils.load_data import load_resources

st.title("👷 Resources")

df = load_resources()

project = st.selectbox("Select Project", df["Project"].unique())
df = df[df["Project"] == project]

st.dataframe(df, use_container_width=True)

st.subheader("Resource Summary")

summary = df.groupby("Responsible")["Hours"].sum().reset_index()
st.dataframe(summary)
