import streamlit as st
import plotly.express as px
import datetime
from utils.load_data import load_activities

if "project" not in st.session_state:
    st.warning("Please select project from Home")
    st.stop()

project = st.session_state["project"]

st.title(f"Timeline - {project}")

df = load_activities()
df = df[df["Project"] == project]

fig = px.timeline(
    df,
    x_start="Start",
    x_end="Finish",
    y="Activity",
    color="Section"
)

fig.update_yaxes(autorange="reversed")

today = datetime.date.today()
fig.add_vline(x=today, line_dash="dash", line_color="red")

st.plotly_chart(fig, use_container_width=True)
