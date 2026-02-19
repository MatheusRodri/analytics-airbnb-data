import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Airbnb Data Analysis Rio De Janeiro")

@st.cache_data
def load_data():
    df = pd.read_csv("data/listings.csv")
    df['price'] = df["price"].str.replace("$", "").str.replace(",", "").astype(float)
    return df

df_rio = load_data()

st.sidebar.header("Filters")
maximinum_price = st.sidebar.slider("Maximinum Price", 30,3000,30000)

df_filtered = df_rio[df_rio['price'] <= maximinum_price]

fig = px.scatter_mapbox(
    df_filtered,
    lat="latitude",
    lon="longitude",
    color="price",
    size="price",
    hover_name="name",
    color_continuous_scale=px.colors.sequential.Plasma,
    zoom=10,
    mapbox_style="carto-darkmatter"
)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig, use_container_width=True)