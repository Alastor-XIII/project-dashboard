import streamlit as st
import plotly.express as px
from utils.load_data import load_activities

st.title("📅 Project Timeline")

df = load_activities()

project = st.selectbox("Select Project", df["Project"].unique())
df = df[df["Project"] == project]

fig = px.timeline(
    df,
    x_start="Start",
    x_end="Finish",
    y="Activity",
    color="Section"
)

fig.update_yaxes(autorange="reversed")

st.plotly_chart(fig, use_container_width=True)
