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

import app_body2 as body

warnings.filterwarnings('ignore')

st.title('COVID Chatbot')

## Side Bar Information
image = Image.open('logo/eskwelabs.png')
st.sidebar.image(image, caption='', use_column_width=True)
st.sidebar.markdown("<h1 style='text-align: center;margin-bottom:50px'>DS Cohort VI</h1>", unsafe_allow_html=True)

## Create Select Box and options
add_selectbox = st.sidebar.radio(
	"Chatbot",
	("Information on COVID-19","COVID-19 Statistics","Information on COVID-19 Vaccines","Chatbot")
)



if add_selectbox == 'Information on COVID-19':
	col1, col2, col3, col4 = st.beta_columns(4)	

	image1 = Image.open('B-Bawal-walang-mask.png')
	col1.image(image1, caption='', width = 350)
	image2 = Image.open('I-isanitize-ang-mga-kamay.png')
	col2.image(image2, caption='', width = 350)
	image3 = Image.open('D-dumistansya-ng-isang-metro.png')
	col3.image(image3, caption='', width = 350)
	image4 = Image.open('A-alamin-ang-totoong-importmasyon.png')
	col4.image(image4, caption='', width = 350)
	body.covid_info()


if add_selectbox == 'COVID-19 Statistics':
	body.covid_statistics_table()
	st.write('Source: Our World in Data - https://covid.ourworldindata.org/data/owid-covid-data.csv')
	st.write('')	
	body.covid_statistics()
	st.write('Source: Our World in Data - https://covid.ourworldindata.org/data/owid-covid-data.csv')