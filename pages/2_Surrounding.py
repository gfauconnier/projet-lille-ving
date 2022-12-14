import streamlit as st
import pandas as pd
import numpy as np
from geopy import Nominatim
import folium
from folium import FeatureGroup
from streamlit_folium import st_folium
from modules.lille_grid import *
from modules.lille_distance import *
from modules.map_utils import *
from modules.style import *
from PIL import Image

# getting the api from osm
locator = Nominatim(user_agent='myGeocoder')

# creating streamlit page
st.set_page_config(
            layout="wide",
            page_title="Greatest place to Lille'ving",
            initial_sidebar_state='collapsed'
            )

# loading the csv in dataframes
target_df = pd.read_csv('./data/target.csv')
features_df = pd.read_csv('./data/cat_features.csv')

# getting the map circle colors
circle_color_dict = get_circle_colors()
cat_dict = get_cat_dict()

# create a form to display and enter adress searches
with st.form("form"):
    # adding columns for better display
    st_columns = st.columns(2,gap="medium")
    # setting a text box with a default value
    with st_columns[0]:
        address = st.text_input('Adresse : ', '27 rue Nationale, Lille')
        # creating a slider to select the radius of the features search
        dist = st.slider('Distance(m) : ', 250, 2000, 500, step=250)
    #adds legend under the map
    image = Image.open('./data/legende.png')
    st_columns[1].image(image)
    # submit button
    submitted = st.form_submit_button("Submit")

    # when the submit button is pressed
    if submitted:
        # gets the adress entered in the text box and centers the map on it
        adr_coords = locator.geocode(address)
        map = folium.Map(location=[adr_coords.latitude, adr_coords.longitude], zoom_start=16, control_scale=True)

        # gets the 10 closest targets and calculates the mean of their Prix m2
        closest_t = get_surrounding_targets(adr_coords.latitude, adr_coords.longitude, target_df, dist)
        estimate = round(target_df.iloc[closest_t]['prix_m2'].mean(),2)

        # draws a circle around the given adress
        folium.Circle(
                    location=[adr_coords.latitude, adr_coords.longitude],
                    popup = f"Estimation : {estimate}??? au m??",
                    radius = dist,
                    fill=True,
                    fill_color="#3186cc"
                ).add_to(map)
        folium.Circle(
                    location=[adr_coords.latitude, adr_coords.longitude],
                    tooltip = f"Estimation : {estimate}??? au m??",
                    radius = 3,
                    fill=True
                ).add_to(map)

        # gets the surrounding features in given radius meters
        surround_features = get_surrounding_features(adr_coords.latitude, adr_coords.longitude, features_df, dist)

        # adding all features on the map
        for key, value in surround_features.items():
            for id_f in value:
                # get the category from the Sous_cat and get its cricle color
                cat_color = [key_cat for key_cat, value in cat_dict.items() if key in value]
                if len(cat_color) == 1:
                    folium.Circle(
                        location=[features_df.iloc[id_f]['lat'], features_df.iloc[id_f]['lon']],
                        tooltip = key,
                        radius=4,
                        color = circle_color_dict[cat_color[0]]
                    ).add_to(map)

        # display the map
        st_map = st_folium(map, width=1724)

        # #adds legend under the map
        # image = Image.open('./data/legende.png')
        # col_legend = st.columns((1,2,1))
        # col_legend[1].image(image)

# add links to other pages
link_col = st.columns((1,2,2,1))
with link_col[1]:
    add_link_button('Index')
with link_col[2]:
    add_link_button('Heatmap')
add_button_style()
