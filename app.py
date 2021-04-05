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

st.title('COVID Chatbot')


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
            
local_css("style.css") #for styling, contains css for the background and the button style



st.markdown("""<style>.css-1aumxhk {background-color: #efede8; background-image: none; color: #efede8}</style>""", unsafe_allow_html=True) # changes background color of sidebar #



st.title("Title")
st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #




## Side Bar Information
image = Image.open('logo/eskwelabs.png')
st.sidebar.image(image, caption='', use_column_width=True)
st.sidebar.markdown("<h1 style='text-align: center;margin-bottom:50px'>DS Cohort VI</h1>", unsafe_allow_html=True)

## Create Select Box and options
add_selectbox = st.sidebar.radio(
	"Chatbot",
	("Information on COVID-19","Information on COVID-19 Vaccines","COVID-19 Statistics","Chatbot")
)


if add_selectbox == 'Information on COVID-19':	
	body.covid_info()


if add_selectbox == 'Information on COVID-19 Vaccines':
	body.vaccine_info()


if add_selectbox == 'COVID-19 Statistics':
	body.covid_statistics_table()
	st.write('Source: Our World in Data - https://covid.ourworldindata.org/data/owid-covid-data.csv')
	st.write('')	
	body.covid_statistics()
	st.write('Source: Our World in Data - https://covid.ourworldindata.org/data/owid-covid-data.csv')


if add_selectbox == 'Chatbot':
	body.chatterbot()
	
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	st.markdown('<div style="font-style: italic;">This is a capstone project of Eskwelabs Cohort 6 Data Science Fellows.</div>',unsafe_allow_html=True)
	st.markdown("""<a style='display: block; text-align: left;color:#84a3a7;text-decoration: none;' href="https://talkingvac.herokuapp.com">Click here to know 	more.</a>""",unsafe_allow_html=True)