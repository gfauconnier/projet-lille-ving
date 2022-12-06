import streamlit as st
import pandas as pd
import numpy as np
from geopy import Nominatim
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
from modules.heatmap import *
from modules.map_utils import *

locator = Nominatim(user_agent='myGeocoder')

st.set_page_config(layout="wide")

features_df = pd.read_csv('./data/cat_features.csv')

target_df = pd.read_csv('./data/dataset_22k_250m.csv')
icons_dict = get_icons_colors()

with st.form("form"):
    st_columns = st.columns(3,gap="medium")

    checkbox_features = {}
    # adding the checkboxes depending on categories
    # for key in icons_dict.keys():
    #     checkbox_features[key] = st.checkbox(key)
    checkbox_features['bar'] = st_columns[0].checkbox('Bar')
    checkbox_features['restaurant'] = st_columns[0].checkbox('Restaurant')
    checkbox_features['park'] = st_columns[0].checkbox('Park')

    # adds a slider to select a range of prices
    price_range = st_columns[1].select_slider('Fourchette de prix au m²', options=np.arange(1000, 7750, 250), value=(2000,3000))

    submitted = st.form_submit_button("Submit")
    # creates the map
    map = folium.Map(location=[50.62925, 3.057256], zoom_start=13, control_scale=True)

    if submitted:
        # gets the categories that are checked in a list
        selected_features = [key for key, value in checkbox_features.items() if value]
        # gets the rows of the dataframe depending on the price range
        df_HM=selector(price_range[0],price_range[1],target_df, selected_features)

        # gets the Heatmap data
        HeatMap(df_HM[['lat','lon']],radius=10,min_opacity=0.57, blur=7).add_to(map)

        # adds the features in a Circle Map
        # df_HM.apply(lambda row:folium.Circle(location=[row['lat'],row['lon']],radius=2, popup=row['prix_m2']).add_to(map), axis=1)

        # prints the map
        st_map = st_folium(map, width=1724)
