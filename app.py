import warnings

import folium
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from PIL import Image
from streamlit import caching
from streamlit_folium import folium_static

import app_body4 as body

warnings.filterwarnings('ignore')


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
            
local_css("style.css") #for styling, contains css for the background and the button style



st.markdown("""<style>.css-1aumxhk {background-color: #efede8; background-image: none; color: #efede8}</style>""", unsafe_allow_html=True) # changes background color of sidebar #


## Side Bar Information
image = Image.open('logo/eskwelabs.png')
st.sidebar.image(image, caption='', use_column_width=True)


## Create Select Box and options
add_selectbox = st.sidebar.radio(
	"Chatbot",
	("Information on COVID-19","Information on COVID-19 Vaccines","COVID-19 Statistics","Chatbot")
)


if add_selectbox == 'Information on COVID-19':	
	st.title("Title")
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	body.covid_info()


if add_selectbox == 'Information on COVID-19 Vaccines':
	st.title("Title")
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	body.vaccine_info()


if add_selectbox == 'COVID-19 Statistics':
	st.title("Title")
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	body.covid_statistics_table()
	st.write('Source: Our World in Data - https://covid.ourworldindata.org/data/owid-covid-data.csv')
	st.write('')	
	body.covid_statistics()
	st.write('Source: Our World in Data - https://covid.ourworldindata.org/data/owid-covid-data.csv')


if add_selectbox == 'Chatbot':
	st.title("Title")
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	body.chatterbot()
	

st.sidebar.markdown('<div style="font-style: italic;">This is a capstone project of Eskwelabs Cohort 6 Data Science Fellows.</div>',unsafe_allow_html=True)
st.sidebar.markdown("""<a style='display: block; text-align: left;color:#84a3a7;text-decoration: none;' href="https://talkingvac.herokuapp.com">Click here to know 	more.</a>""",unsafe_allow_html=True)