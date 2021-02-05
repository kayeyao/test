import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import seaborn as sns
import streamlit as st
from PIL import Image
from streamlit_folium import folium_static
from streamlit import caching

def introduction():
    image = Image.open('logo/nyoy_pic.PNG').convert('RGB')
    st.image(image, caption='', width=800, height=300)
    st.write('')
    st.header('Tuloy Pa Rin')
    st.header('Client: Nyoy Volante')
    st.write('Nyoy Volante is a Filipino singer and songwriter, initially dubbed as "The Prince of Acoustic Pop" turned "The King of Philippine Acoustic Pop."')
    st.write('Nyoy Volante wants to jumpstart his 2021 music career. He wishes to land a spot in the Spotify PH Top Daily 200.')
    st.header('Business Objectives')
    st.write('1. Identify popular music genres in the Philippines.')
    st.write('2. Determine genres Nyoy can venture into.')
    st.write('3. Provide a list of potential artirts Nyoy can collaborate with.')
 
def dataset():
    st.write('')
    st.header('Spotify Data Set')
    
    st.write('<b>Top 200 Daily Charts:</b>')
    st.write('<b>Date Range</b>: January 1, 2017 - December 31, 2020')

    dailychart = {
                      'Column Name': ['date', 'position', 'track_id', 'track_name', 'artist', 'streams'], 
                      'Description': ['Daily Chart Date', 'Song Charting Position', 'Song Unique Identifier', 'Song Name', 'Name of Singer', 'Total Number of Daily Streams'],
                      'Sample Data': ['2020-12-31','200','2S80c51YXgJQhkhX603fMA','Prinsesa','6cyclemind','17516']
			}
    st.table(dailychart)

    st.markdown('<b>Track Audio Features:</b>', unsafe_allow_html=True)

    audiofeatures = {
                      'Column Name': ['duration_ms', 'key', 'mode', 'acousticness', 'danceability', 'energy','instrumentalness','liveness','loudness','speechiness','valence','tempo'], 
                      'Desription': ['The duration of the track in milliseconds.','The key the track is in.','Indicates the modality (major or minor) of a track, the type of scale from which it is melodic.',
				'A confidence measure from 0.0 to 1.0 of whether the track is acoustic.','Describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity.',
				'A measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.','Predicts whether a track contains no vocals.',
				'Detects the presence of an audience in the recording.','The overall loudness of a track in decibels (dB).','Detects the presence of spoken words in a track.','A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.',
				'The overall estimated tempo of a track in beats per minute (BPM).']
			}
    st.table(audiofeatures)

    st.markdown('<b>Playlist Date:</b>', unsafe_allow_html=True)

    playlistdata = {
                      'Column Name': ['playlist_id','playlist_name','playlist_total_tracks','owner_id','owner_name','total_followers'],
                     'Description': ['Playlist Unique Identification','Name of the Playlist','Total Number of Songs in the Playlist','Playlist Owner Unique Identification','Playlist Owner','Total Followers of the Playlist']
			}
    st.table(playlistdata)


def tools():
    st.write('')
    st.header('List of Tools')
    st.write('-----------------------------------------------------------------------') 
    image = Image.open('logo/Spotify.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/jupyter.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/pandas.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/heroku.jpg').convert('RGB')
    st.image(image, caption='', width=150, height=50)
    image = Image.open('logo/streamlit.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/github.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/scipy.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/seaborn.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/matplotlib.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/numpy.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)

def cleaning():
    st.write('')
    st.header('Data Cleaning')

def eda():
    caching.clear_cache()
    st.write('')
    st.header('Exploratory Data Analysis')
    st.write('-----------------------------------------------------------------------') 
    st.write('<b>Popular Genres in the Philippines</b>')
    

def genre_classification():
    caching.clear_cache()
    st.write('')
    st.header('Song Genre Classification')
    st.write('-----------------------------------------------------------------------') 
    st.write('')


def recommenderengine():
    caching.clear_cache()
    st.write('')
    st.header('Recommended Artist Collaborations')
    st.write('-----------------------------------------------------------------------') 
    st.write('') 


def conclusion():
    caching.clear_cache()
    st.write('')
    st.header('Recommended Business Strategies')
    st.write('-----------------------------------------------------------------------') 
    st.write('')   

def contributors():
    caching.clear_cache()
    st.write('')
    st.header('Contributors')
    st.write('-----------------------------------------------------------------------') 
    st.write('')

    st.subheader('Generoso Roberto')
    st.subheader('Kaye Janelle Yao')
    st.subheader('Rodel Arenas')
    st.subheader('Tyron Rex Frago')
    st.subheader('Emerson Fili Chua - Mentor')