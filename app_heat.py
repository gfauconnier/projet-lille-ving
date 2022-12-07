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
target_df = pd.read_csv('./data/df_22k_250m.csv')

with st.form("form", clear_on_submit=False):
    st_columns = st.columns(4,gap="medium")

    checkbox_features = {}
    # adding the checkboxes depending on categories
    # for key in icons_dict.keys():
    #     checkbox_features[key] = st.checkbox(key)
    checkbox_features['bar'] = st_columns[0].checkbox('Bar')
    checkbox_features['restaurant'] = st_columns[0].checkbox('Restaurant')
    checkbox_features['park'] = st_columns[0].checkbox('Park')

    type_local = st_columns[1].selectbox('Type de bien : ', ('Tous', 'Maisons', 'Appartements'))

    # adds a slider to select a range of prices
    price_range = st_columns[2].select_slider('Fourchette de prix au m²', options=np.arange(1000, 7750, 250), value=(2000,3000))

    budget = st_columns[3].number_input('Budget : ', step=5000)
    surface = st_columns[3].number_input('Surface en m² : ', step=1)

    submitted = st.form_submit_button("Submit")
    # creates the map
    map = folium.Map(location=[50.62925, 3.057256], zoom_start=13, control_scale=True)

    if submitted:
        code_type_local = get_type_local(type_local)
        budget_price_m2 = 0
        if budget != 0 and surface != 0:
            budget_price_m2 = round(budget / surface, 2)

        # gets the categories that are checked in a list
        selected_features = [key for key, value in checkbox_features.items() if value]

        # gets the rows of the dataframe depending on the slider values if budget and surface aren't typed
        if budget_price_m2:
            df_HM = selector((budget_price_m2 - 100),(budget_price_m2 + 100),target_df, selected_features, code_type_local)
        else:
            df_HM = selector(price_range[0],price_range[1],target_df, selected_features, code_type_local)

        # gets the Heatmap data
        HeatMap(df_HM[['lat','lon']],radius=10,min_opacity=0.57, blur=7).add_to(map)

        # adds the features in a Circle Map
        # df_HM.apply(lambda row:folium.Circle(location=[row['lat'],row['lon']],radius=2, popup=row['prix_m2']).add_to(map), axis=1)

        # prints the map
        st_map = st_folium(map, width=1724)
