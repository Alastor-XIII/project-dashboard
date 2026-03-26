import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.title("📅 Project Timeline")

project = st.session_state.get("project")

df = pd.read_excel("data/activities.xlsx")
df = df[df["ProjectID"] == project]

fig = px.timeline(
    df,
    x_start="Start",
    x_end="Finish",
    y="Activity",
    color="Progress"
)

fig.update_yaxes(autorange="reversed")

today = datetime.today().strftime('%Y-%m-%d')
fig.add_vline(x=today, line_dash="dash", line_color="red")

st.plotly_chart(fig, use_container_width=True)
