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
import datetime as dt
import altair as alt

stats = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
stats['date'] = pd.to_datetime(stats['date'])


countries = ('World', 'Afghanistan', 'Africa', 'Albania', 'Algeria', 'Andorra', 'Angola','Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Asia','Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain','Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin','Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina','Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso','Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde','Cayman Islands', 'Central African Republic', 'Chad', 'Chile','China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica',"Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czechia','Democratic Republic of Congo', 'Denmark', 'Djibouti', 'Dominica','Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador','Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia','Europe', 'European Union', 'Faeroe Islands', 'Falkland Islands','Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia','Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada','Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana','Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India','Indonesia', 'International', 'Iran', 'Iraq', 'Ireland','Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey','Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan','Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya','Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Madagascar','Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta','Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico','Micronesia (country)', 'Moldova', 'Monaco', 'Mongolia','Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar','Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua','Niger', 'Nigeria', 'North America', 'North Macedonia','Northern Cyprus', 'Norway', 'Oceania', 'Oman', 'Pakistan','Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru','Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia','Rwanda', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia','Saint Vincent and the Grenadines', 'Samoa', 'San Marino','Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia','Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia','Solomon Islands', 'Somalia', 'South Africa', 'South America','South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan','Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan','Tajikistan', 'Tanzania', 'Thailand', 'Timor', 'Togo','Trinidad and Tobago', 'Tunisia', 'Turkey','Turks and Caicos Islands', 'Uganda', 'Ukraine','United Arab Emirates', 'United Kingdom', 'United States','Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican', 'Venezuela','Vietnam', 'Yemen', 'Zambia', 'Zimbabwe')


st.markdown("""
<style>
.small-font {
    font-size:10px !important;
}
</style>
""", unsafe_allow_html=True)



def covid_info():
	st.header('Information on COVID-19')
	
	if st.button('What is COVID-19?'):	
		st.write('COVID-19 is the disease caused by a new coronavirus called SARS-CoV-2.  WHO first learned of this new virus on 31 December 2019, following a report of a cluster of cases of ‘viral pneumonia’ in Wuhan, People’s Republic of China.')
		st.markdown('<p class="small-font">Source: World Health Organization - https://www.who.int/news-room/q-a-detail/coronavirus-disease-covid-19</p>', unsafe_allow_html=True)
		st.write('Source: World Health Organization - https://www.who.int/news-room/q-a-detail/coronavirus-disease-covid-19')
	
	if st.button('What are the symptoms of COVID-19?'):	
		st.write('The most common symptoms of COVID-19 are *Fever, Dry cough, and Fatigue*.\n') 
		st.write('Other symptoms that are less common and may affect some patients include *Loss of taste or smell, Nasal congestion, Conjunctivitis (also known as red eyes), Sore throat, Headache, Muscle or joint pain, Different types of skin rash, Nausea or vomiting, Diarrhea, Chills or dizziness*.\n') 
		st.write('Symptoms of severe COVID‐19 disease include *Shortness of breath, Loss of appetite, Confusion, Persistent pain or pressure in the chest, High temperature (above 38 °C)*.\n') 
		st.write('Other less common symptoms are *Irritability, Confusion, Reduced consciousness (sometimes associated with seizures), Anxiety, Depression, Sleep disorders*.\n')
		st.write('More severe and rare neurological complications such as *strokes, brain inflammation, delirium and nerve damage*.\n') 
		st.write('People of all ages who experience fever and/or cough associated with difficulty breathing or shortness of breath, chest pain or pressure, or loss of speech or movement should seek medical care immediately. If possible, call your health care provider, hotline or health facility first, so you can be directed to the right clinic.')
		st.write('Source: World Health Organization - https://www.who.int/news-room/q-a-detail/coronavirus-disease-covid-19')


def covid_statistics_table():
	st.header('COVID-19 Statistics')

	country = st.selectbox('Country', countries)
	
	country_stats = stats[stats['location'] == country].reset_index()

	for i in range(1, len(country_stats)):
		if country_stats['total_vaccinations'].isnull()[i]:
			country_stats['total_vaccinations'][i] = country_stats['total_vaccinations'][i-1]
	
	end_date = country_stats['date'].max()
	country_stats_timeframe = country_stats
	latest_status = country_stats[country_stats['date'] == end_date]

	if country in ['World','Philippines','United States']:
		st.subheader('Status of COVID-19 cases in the ' + country + ' as of ' + end_date.strftime("%b %d %Y") + ':')
	else:
		st.subheader('Status of COVID-19 cases in ' + country + ' as of ' + end_date.strftime("%b %d %Y") + ':')

	covidstats = pd.DataFrame({
			'Column': ['Total Cases', 'New Cases', 'Total Deaths', 'New Deaths', 'Total Vaccinations'], 
                 	'Data as of ' + end_date.strftime("%b %d %Y"): [f"{int(latest_status['total_cases'].iloc[0]):,d}",f"{int(latest_status['new_cases'].iloc[0]):,d}",f"{int(latest_status['total_deaths'].iloc[0]):,d}", f"{int(latest_status['new_deaths'].iloc[0]):,d}",f"{int(latest_status['total_vaccinations'].iloc[0]):,d}"]
		})

	covidstats.set_index('Column', inplace = True)	

	st.table(covidstats)


def covid_stats(country,status,length):
	country_stats_merged = pd.DataFrame(columns = stats.columns)		

	for x in country:
		country_stats = stats[stats['location']==x].reset_index()

		for i in range(1, len(country_stats)):
			if country_stats['total_vaccinations'].isnull()[i]:
				country_stats['total_vaccinations'][i] = country_stats['total_vaccinations'][i-1]
		
		if length == 0:
			end_date = country_stats['date'].max()
			country_stats_timeframe = country_stats
			latest_status = country_stats[country_stats['date'] == end_date]
		else:    
			end_date = country_stats['date'].max()
			start_date = end_date - dt.timedelta(length)
			start_index = country_stats.index[country_stats['date'] == start_date]
			end_index = country_stats.index[country_stats['date'] == end_date]
			country_stats_timeframe = country_stats.iloc[start_index[0]:]
			latest_status = country_stats[country_stats['date'] == end_date]

		country_stats_merged = country_stats_merged.append(country_stats_timeframe)

	st.subheader('COVID-19 ' + status)

	country_stats_graph = pd.DataFrame(columns = ['date'])
	for x in country:
		if status == 'Daily Cases':
			data = country_stats_merged[country_stats_merged['location']==x][['new_cases','date']].rename(columns={"new_cases": x})
			country_stats_graph =  country_stats_graph.merge(data, on = 'date', how = 'outer')
		elif status == 'Total Cases':
			data = country_stats_merged[country_stats_merged['location']==x][['total_cases','date']].rename(columns={"total_cases": x})
			country_stats_graph =  country_stats_graph.merge(data, on = 'date', how = 'outer')
		elif status == 'Daily Deaths':
			data = country_stats_merged[country_stats_merged['location']==x][['new_deaths','date']].rename(columns={"new_deaths": x})
			country_stats_graph =  country_stats_graph.merge(data, on = 'date', how = 'outer')
		elif status == 'Total Deaths':
			data = country_stats_merged[country_stats_merged['location']==x][['total_deaths','date']].rename(columns={"total_deaths": x})
			country_stats_graph =  country_stats_graph.merge(data, on = 'date', how = 'outer')
		elif status == 'Total Vaccinations':
			data = country_stats_merged[country_stats_merged['location']==x][['total_vaccinations','date']].rename(columns={"total_vaccinations": x})
			country_stats_graph =  country_stats_graph.merge(data, on = 'date', how = 'outer')

	st.line_chart(country_stats_graph.rename(columns={'date':'index'}).set_index('index'))


def covid_statistics():
	st.header('COVID-19 Cases + Vaccinations')
	col1, col2 = st.beta_columns(2)	

	country = st.multiselect('Country', countries)
		
	status = col1.selectbox('Information',('Daily Cases','Total Cases','Daily Deaths','Total Deaths','Total Vaccinations'))

	length = col2.selectbox('Timeframe',('All Time', '1 Week', '2 Weeks', '1 Month', '2 Months'))
	
	length_tag = {'All Time':0,'1 Week':7,'2 Weeks':14,'1 Month':30,'2 Months':60}

	covid_stats(country, status, length_tag[length])