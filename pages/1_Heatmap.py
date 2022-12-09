import streamlit as st
import pandas as pd
import numpy as np
from geopy import Nominatim
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
from modules.heatmap import *
from modules.map_utils import *
from modules.style import *

# getting the location api
locator = Nominatim(user_agent='myGeocoder')

st.set_page_config(
            layout="wide",
            page_title="Greatest place to Lille'ving",
            initial_sidebar_state='collapsed'
            )

# loading the dataframes
features_df = pd.read_csv('./data/cat_features.csv')
target_df = pd.read_csv('./data/df_22k_250m_c.csv')

# creates the form
with st.form("form", clear_on_submit=False):
    st_columns = st.columns(3,gap="medium")

    # add drop selector
    type_local = st_columns[0].selectbox('Type de bien : ', ('Tous', 'Maisons', 'Appartements'))

    # adds a slider to select a range of prices
    price_range = st_columns[1].select_slider('Fourchette de prix au m²', options=np.arange(1000, 7750, 250), value=(2000,3000))

    # adds input text boxes for budget and surface
    budget = st_columns[2].number_input('Budget : ', step=5000)
    surface = st_columns[2].number_input('Surface en m² : ', step=1)

    # gets the categories dictionary and create the checkboxes
    cat_dict = get_cat_dict()

    checkbox_expander = st.expander("Selectionnez les catégories", expanded=False)
    with checkbox_expander:
        st_columns_check = st.columns(3,gap="small")
        checkbox_features = {}
        for key in cat_dict.keys():
            col = int(list(cat_dict.keys()).index(key)/9)
            checkbox_features[key] = st_columns_check[col].checkbox(key if key != 'Mosqué' else 'Mosquée')


    submitted = st.form_submit_button("Submit")

    # creates the map
    map = folium.Map(location=[50.62925, 3.057256], zoom_start=13, control_scale=True)

    if submitted:
        # gets the price per m² if both surface and budget are inputed
        budget_price_m2 = 0
        if budget != 0 and surface != 0:
            budget_price_m2 = round(budget / surface, 2)

        # gets the categories that are checked in a list
        selected_categories = [key for key, value in checkbox_features.items() if value]

        # gets the rows of the dataframe depending on the slider values if budget and surface aren't typed
        code_type_local = get_type_local(type_local)
        if budget_price_m2:
            df_HM = selector((budget_price_m2 - 250),(budget_price_m2 + 250),target_df, selected_categories, code_type_local)
        else:
            df_HM = selector(price_range[0],price_range[1],target_df, selected_categories, code_type_local)

        # gets the Heatmap data
        HeatMap(df_HM[['lat','lon']],radius=10,min_opacity=0.57, blur=7).add_to(map)

        # prints the map
        st_map = st_folium(map, width=1724)

# add links to other pages
link_col = st.columns((1,2,2,1))
with link_col[1]:
    add_link_button('Index')
with link_col[2]:
    add_link_button('Surrounding')
add_button_style()
