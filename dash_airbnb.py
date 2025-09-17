import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(layout="wide")
st.title("Airbnb Data Analysis Rio De Janeiro")

df_rio = pd.read_csv("data/listings.csv")
df_rio['price'] = df_rio["price"].str.replace("$", "").str.replace(",", "").astype(float)

renderer = StreamlitRenderer(df_rio)
renderer.explorer()