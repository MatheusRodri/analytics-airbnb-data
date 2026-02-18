import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(layout="wide")
st.title("Airbnb Data Analysis Rio De Janeiro")

@st.cache_data
def load_data():
    df = pd.read_csv("data/listings.csv")
    df['price'] = df["price"].str.replace("$", "").str.replace(",", "").astype(float)
    return df

df_rio = load_data()


@st.cache_resource
def get_pyg_renderer(dataframe):
    return StreamlitRenderer(dataframe, spec="streamlit_config.json", spec_io_mode="rw")

renderer = get_pyg_renderer(df_rio)
renderer.viewer()