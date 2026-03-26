import streamlit as st
from utils.load_data import load_milestones

st.title("Milestones")

df = load_milestones()

st.dataframe(df)
