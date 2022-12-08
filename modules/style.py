import streamlit as st
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .main {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def add_link_button(link):
    st.write(f'''
        <a target="_self" href="./{link}">
            <button class="button">
                {link}
            </button>
        </a>
        ''',
        unsafe_allow_html=True
    )

def add_button_style():
    st.markdown(
        f"""
        <style>
        .button {{
            background-color: white;
            color: black;
            border: 2px solid black;
            border-radius: 8px;
            transition-duration: 0.4s;
            padding: 10px 24px;
            margin: 20px;
        }}
        .button:hover {{
            background-color: #e7e7e7;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
