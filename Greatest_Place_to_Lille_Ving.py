import streamlit as st
from modules.style import *

st.set_page_config(
            layout="wide",
            page_title="Greatest place to Lille'ving",
            initial_sidebar_state='collapsed'
            )

add_bg_from_local('./data/logo.png')
add_button_style()

add_link_button('Heatmap')
add_link_button('Surrounding')
