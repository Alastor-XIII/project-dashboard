import streamlit as st
import pandas as pd

st.title("👷 Resources")

df = pd.read_excel("data/resources.xlsx")

st.dataframe(df)
