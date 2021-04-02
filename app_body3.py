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


def covid_info():
	st.header('Frequently Asked Questions on COVID-19')

	st.subheader('COVID-19')	
	if st.button('What is COVID-19?'):	
		st.write('COVID-19 is the disease caused by a new coronavirus called SARS-CoV-2.  WHO first learned of this new virus on 31 December 2019, following a report of a cluster of cases of ‘viral pneumonia’ in Wuhan, People’s Republic of China.')
		st.write('Source: World Health Organization - https://www.who.int/news-room/q-a-detail/coronavirus-disease-covid-19')

	st.subheader('COVID-19 Symptoms')	
	if st.button('What are the symptoms of COVID-19?'):	
		st.write('The most common symptoms of COVID-19 are *Fever, Dry cough, and Fatigue*.\n') 
		st.write('Other symptoms that are less common and may affect some patients include *Loss of taste or smell, Nasal congestion, Conjunctivitis (also known as red eyes), Sore throat, Headache, Muscle or joint pain, Different types of skin rash, Nausea or vomiting, Diarrhea, Chills or dizziness*.\n') 
		st.write('Symptoms of severe COVID‐19 disease include *Shortness of breath, Loss of appetite, Confusion, Persistent pain or pressure in the chest, High temperature (above 38 °C)*.\n') 
		st.write('Other less common symptoms are *Irritability, Confusion, Reduced consciousness (sometimes associated with seizures), Anxiety, Depression, Sleep disorders*.\n')
		st.write('More severe and rare neurological complications such as *strokes, brain inflammation, delirium and nerve damage*.\n') 
		st.write('People of all ages who experience fever and/or cough associated with difficulty breathing or shortness of breath, chest pain or pressure, or loss of speech or movement should seek medical care immediately. If possible, call your health care provider, hotline or health facility first, so you can be directed to the right clinic.')
		st.write('Source: World Health Organization - https://www.who.int/news-room/q-a-detail/coronavirus-disease-covid-19')

	if st.button('How long does it take to develop symptoms?'):	
		st.write('The time from exposure to COVID-19 to the moment when symptoms begin is, on average, 5-6 days and can range from 1-14 days. This is why people who have been exposed to the virus are advised to remain at home and stay away from others, for 14 days, in order to prevent the spread of the virus, especially where testing is not easily available.')
		st.write('Source: World Health Organization - https://www.who.int/news-room/q-a-detail/coronavirus-disease-covid-19')

	if st.button('Who is most at risk of severe illness from COVID-19?'):	
		st.write('People aged 60 years and over, and those with underlying medical problems like high blood pressure, heart and lung problems, diabetes, obesity or cancer, are at higher risk of developing serious illness. .\n')
		st.write('However, anyone can get sick with COVID-19 and become seriously ill or die at any age. \n')
		st.write('Source: World Health Organization - https://www.who.int/news-room/q-a-detail/coronavirus-disease-covid-19')

	st.subheader('COVID-19 Transmission & Prevention')
	if st.button('How does COVID-19 spread?'):	
		st.write('COVID-19 is transmitted from person to person via droplets, contact, and fomites. It is transmitted when one individual talks, sneezes, or coughs producing ‘droplets’ of saliva containing the COVID-19 virus. These droplets are then inhaled by another person. COVID-19 transmission usually occurs among close contacts -- including family members and healthcare workers. It is therefore important to maintain a distance of more than 1 meter away from any person who has respiratory symptoms.')
		st.write('Source: Department of Health - https://doh.gov.ph/COVID-19/FAQs'

	if st.button('Can COVID-19 be caught from a person who has no symptoms?'):	
		st.write('The risk of getting COVID-19 from a person without any signs and symptoms is very low. Remember, COVID-19 is only spread through respiratory droplets coughed by an infected person. Therefore, if an infected person does not cough, he/she most likely will not infect others. However, many infected persons only experience mild symptoms. This is particularly true at the early stages of the disease. It is therefore possible to get COVID-19 from an infected person with mild cough but is not feeling ill.')
		st.write('Source: Department of Health - https://doh.gov.ph/COVID-19/FAQs')

	if st.button('What can I do to prevent the spread of COVID-19?'):	
		st.write('DOH advises the public to practice protective measures. It is still the best way to protect oneself against COVID-19.') 
		st.write('- Practice frequent and proper handwashing - wash hands often with soap and water for at least 20 seconds. Use an alcohol-based hand sanitizer if soap and water are not available.')
		st.write('- Practice proper cough etiquette - Cover mouth and nose using tissue or sleeves/bend of the elbow when coughing or sneezing; Move away from people when coughing; Do not spit; Throw away used tissues properly; Always wash your hands after sneezing or coughing; Use alcohol/sanitizer.')
		st.write('- Maintain distance of at least one meter away from individual/s experiencing respiratory symptoms.')
		st.write('- Avoid unprotected contact with farm or wild animals (alive or dead), animal markets, and products that come from animals (such as uncooked meat).')
		st.write('- Ensure that food is well-cooked.')
		st.write('Source: Department of Health - https://doh.gov.ph/COVID-19/FAQs')

	st.subheader('COVID-19 Testing')
	if st.button('When should I get tested for COVID-19?'):	
		st.write('Anyone with symptoms should be tested, wherever possible. People who do not have symptoms but have had close contact with someone who is, or may be, infected may also consider testing – contact your local health guidelines and follow their guidance.')
		st.write('While a person is waiting for test results, they should remain isolated from others. Where testing capacity is limited, tests should first be done for those at higher risk of infection, such as health workers, and those at higher risk of severe illness such as older people, especially those living in seniors’ residences or long-term care facilities.') 
		st.write('Source: World Health Organization - https://www.who.int/news-room/q-a-detail/coronavirus-disease-covid-19')

	if st.button('What test should I get to see if I have COVID-19?'):	
		st.write('In most situations, a molecular test is used to detect SARS-CoV-2 and confirm infection. Polymerase chain reaction (PCR) is the most commonly used molecular test. Samples are collected from the nose and/or throat with a swab. Molecular tests detect virus in the sample by amplifying viral genetic material to detectable levels. For this reason, a molecular test is used to confirm an active infection, usually within a few days of exposure and around the time that symptoms may begin. ')
		st.write('Rapid antigen tests (sometimes known as a rapid diagnostic test – RDT) detect viral proteins (known as antigens). Samples are collected from the nose and/or throat with a swab. These tests are cheaper than PCR and will offer results more quickly, although they are generally less accurate. These tests perform best when there is more virus circulating in the community and when sampled from an individual during the time they are most infectious.') 
		st.write('Source: World Health Organization - https://www.who.int/news-room/q-a-detail/coronavirus-disease-covid-19')

	st.subheader('DOH COVID-19 Response')
	if st.button('What are the DOH and other concerned agencies doing to contain the situation?'):	
		st.write('DOH is closely monitoring individuals who manifested signs of respiratory infection and had a history of travel to China or other countries with confirmed COVID-19 cases, and is coordinating with WHO and China Center for Disease Control for updates.  The Department is also strictly monitoring our repatriates from Wuhan, China and the M/V Diamond Princess in Japan, and continues to conduct contact tracing of our positive cases to ascertain that the spread of the virus locally is put to a halt.\n')
		st.write('Moreover, DOH has instituted the Interagency Task Force for the Management of Emerging Infectious Diseases (IATF-EID), the agency in-charge for the overall management of COVID-19 preparedness and response. It has likewise created the DOH Emergency Operation Center (DOH EOC) for COVID-19, a command center in-charge of consolidating updates and information as the COVID-19 health event evolves.\n')
		st.write('In terms of communicating developments to the public, the Department holds press briefings thrice a week to ensure the government’s transparency and accountability.')
		st.write('DOH also enhanced its coronavirus laboratory testing capacity, hospital preparedness, rapid response, and its risk communication and information dissemination. Personal Protective Equipment is made available at the Bureau of Quarantine, Centers for Health Development, and DOH Hospitals')
		st.write('Finally, the Bureau of Quarantine is working with airlines and airport authorities to strengthen border surveillance, while the Epidemiology Bureau is heightening its community surveillance.')
		st.write('Source: Department of Health - https://doh.gov.ph/COVID-19/FAQs')


def vaccine_info():
	st.header('Frequently Asked Questions on COVID-19 Vaccines')
	
	st.subheader('Available COVID-19 Vaccines')
	if st.button('Is there a vaccine for COVID-19?'):	
		st.write('Yes there are now several vaccines that are in use. The first mass vaccination programme started in early December 2020 and as of and as of 15 February 2021, 175.3 million vaccine doses have been administered. At least 7 different vaccines (3 platforms) have been administered.')
		st.write('WHO issued an Emergency Use Listing (EULs) for the Pfizer COVID-19 vaccine (BNT162b2) on 31 December 2020. On 15 February 2021, WHO issued EULs for two versions of the AstraZeneca/Oxford COVID-19 vaccine, manufactured by the Serum Institute of India and SKBio. WHO is on track to EUL other vaccine products through June.')
		st.write('Once vaccines are demonstrated to be safe and efficacious, they must be authorized by national regulators, manufactured to exacting standards, and distributed. WHO is working with partners around the world to help coordinate key steps in this process, including to facilitate equitable access to safe and effective COVID-19 vaccines for the billions of people who will need them.')
		st.write('Source: World Health Organization - https://www.who.int/news-room/q-a-detail/coronavirus-disease-(covid-19)-vaccines')

	if st.button('When will the COVID-19 vaccine be available in the Philippines?'):	
		st.write('The government is currently in the initial phase of vaccine rollout with the availability of Sinovac and AstraZeneca vaccines in the country. Likewise, the country is in the advanced stages of negotiations with the COVAX Facility and various other vaccine manufacturers.')
		image = Image.open('vaccine tracker.png')
		st.image(image, caption='', width = 800)
		st.write('Source: Department of Health - https://doh.gov.ph/vaccines/Questions-and-Answers')

	st.subheader('Know your COVID-19 vaccine brands!')
	vaccine = st.selectbox('Select Vaccine Brand', ('Pfizer-BioNTech','Oxford-AstraZeneca','CoronaVac (Sinovac)','Sputnik V'))
	if vaccine == 'Pfizer-BioNTech':
		image = Image.open('pfizer.png')
		st.image(image, caption='', width = 600)
		st.write('Source: Department of Health - https://doh.gov.ph/vaccines')		
	if vaccine == 'Oxford-AstraZeneca':
		image = Image.open('astrazeneca.png')
		st.image(image, caption='', width = 600)
		st.write('Source: Department of Health - https://doh.gov.ph/vaccines')	
	if vaccine == 'CoronaVac (Sinovac)':
		image = Image.open('sinovac.png')
		st.image(image, caption='', width = 600)
		st.write('Source: Department of Health - https://doh.gov.ph/vaccines')	
	if vaccine == 'Sputnik V':
		image = Image.open('sputnik.png')
		st.image(image, caption='', width = 600)	
		st.write('Source: Department of Health - https://doh.gov.ph/vaccines')

	st.subheader('Necessity of Vaccination')
	if st.button('Why do we need to get vaccinated for COVID-19?'):	
		st.write('The COVID-19 pandemic has taken many lives, and continues to put many at risk. It has also disrupted the economy, leaving many Filipinos jobless or underemployed.')
		st.write('With the availability of COVID-19 vaccines which can (1) prevent symptomatic infection and possibly (2) prevent severe infection and (3) prevent transmission, we have the opportunity to get ahead of the virus.')
		st.write('However, like many vaccines being used in the past decades, the protective effect on our community is maximized only when at least 70% of the population get vaccinated.')
		st.write('For example, if your barangay has 100,000 people, at least 70,000 should be vaccinated to ensure protection of the community.')
		st.write('So remember, this is not just about getting you or your family vaccinated, this is about getting your barangay, city, province up for it.')
		st.write('Source: Department of Health - https://doh.gov.ph/vaccines')

	if st.button('How do COVID-19 vaccines work?'):	
		st.write('To understand how COVID-19 vaccines work, it helps to first look at how our bodies fight illness. When germs, such as the virus that causes COVID-19, invade our bodies, they attack and multiply. This invasion, called an infection, is what causes illness. Our immune system uses several tools to fight infection.')
		st.write('The first time a person is infected with the virus that causes COVID-19, it can take several days or weeks for their body to make and use all the germ-fighting tools needed to get over the infection. After the infection, the person’s immune system remembers what it learned about how to protect the body against that disease. COVID-19 vaccines help our bodies develop immunity to the virus that causes COVID-19 without us having to get the illness.')
		st.write('Different types of vaccines work in different ways to offer protection. But with all types of vaccines, the body is left with a supply of “memory” T-lymphocytes as well as B-lymphocytes that will remember how to fight that virus in the future. Sometimes after vaccination, the process of building immunity can cause symptoms, such as fever. These symptoms are normal and are signs that the body is building immunity.')
		st.write('Source: Centers for Disease Control and Prevention - https://www.cdc.gov/coronavirus/2019-ncov/vaccines/different-vaccines/how-they-work.html')

	st.subheader('COVID-19 Vaccine Safety and Efficacy')
	if st.button('How will we know if COVID-19 vaccines are safe?'):	
		st.write('Ensuring the safety and quality of vaccines is one of WHO’s highest priorities. WHO works closely with national authorities to ensure that global norms and standards are developed and implemented to assess the quality, safety and efficacy of vaccines.')
		st.write('The process to develop COVID vaccines is fast-tracked while maintaining the highest standards: Given the urgent need to stop the pandemic, pauses between steps, often needed to secure funding, have been shortened, or eliminated, and in some cases, steps are being carried out in parallel to accelerate the process, wherever that is safe to do. COVID-19 vaccine developers have issued a joint pledge not to seek government approval for their vaccines until they’ve been proven to be safe and effective.')
		st.write('There are many strict protections in place to help ensure that COVID-19 vaccines are safe. Like all vaccines, COVID-19 vaccines are going through a rigorous, multi-stage testing process, including large (phase III) trials that involve tens of thousands of people. These trials, which include some groups at high risk for COVID-19 (certain groups like pregnant and lactating women were not included in vaccine trials), are specifically designed to identify any common side effects or other safety concerns.')
		st.write('Once a clinical trial shows that a COVID-19 vaccine is safe and effective, a series of independent reviews of the efficacy and safety evidence is required, including regulatory review and approval in the country where the vaccine is manufactured, before WHO considers a vaccine product for EUL or prequalification. EUL or Prequalification verifies to those countries that would want to procure a particular vaccine that there has been an assurance by WHO that the regulatory review process, usually in the country of manufacture, has held up to the highest standards. Part of this process also involves a review of all the safety evidence by the Global Advisory Committee on Vaccine Safety.')
		st.write('Source: World Health Organization - https://www.who.int/news-room/q-a-detail/coronavirus-disease-(covid-19)-vaccines')

	if st.button('What are the side-effects of COVID-19 vaccines?'):	
		st.write('After getting vaccinated, you might have some side effects, which are normal signs that your body is building protection. Common side effects are pain, redness, and swelling in the arm where you received the shot, as well as tiredness, headache, muscle pain, chills, fever, and nausea throughout the rest of the body. These side effects could affect your ability to do daily activities, but they should go away in a few days.')
		st.write('Source: Centers for Disease Control and Prevention - https://www.cdc.gov/coronavirus/2019-ncov/vaccines/faq.html')	

	if st.button('Can a COVID-19 vaccine make me sick with COVID-19?'):	
		st.write('No. None of the authorized and recommended COVID-19 vaccines or COVID-19 vaccines currently in development in the United States contain the live virus that causes COVID-19. This means that a COVID-19 vaccine cannot make you sick with COVID-19.')
		st.write('There are several different types of vaccines in development. All of them teach our immune systems how to recognize and fight the virus that causes COVID-19. Sometimes this process can cause symptoms, such as fever. These symptoms are normal and are a sign that the body is building protection against the virus that causes COVID-19.')
		st.write('It typically takes a few weeks for the body to build immunity (protection against the virus that causes COVID-19) after vaccination. That means it’s possible a person could be infected with the virus that causes COVID-19 just before or just after vaccination and still get sick. This is because the vaccine has not had enough time to provide protection.')
		st.write('Source: Centers for Disease Control and Prevention - https://www.cdc.gov/coronavirus/2019-ncov/vaccines/facts.html')

	st.subheader('COVID-19 Vaccine Deployment')
	if st.button('Is vaccination mandatory?'):	
		st.write('Vaccination is not mandatory. But the government highly encourages the public to get vaccinated and be protected against preventable disease.')
		st.write('The COVID-19 pandemic has taken many lives, and continues to put many at risk. It has also disrupted the economy, leaving many Filipinos jobless or underemployed. With the availability of COVID-19 vaccines which can (1) prevent symptomatic infection and possibly (2) prevent severe infection and (3) prevent transmission, we have the opportunity to get ahead of the virus. However, like many vaccines being used in the past decades, the protective effect on our community is maximized only when at least 70% of the population get vaccinated. For example, if your barangay has 100,000 people, at least 70,000 should be vaccinated to ensure protection of the community. So remember, this is not just about getting you or your family vaccinated, this is about getting your barangay, city, province up for it.')
		st.write('Source: Department of Health - https://doh.gov.ph/vaccines/Questions-and-Answers')

	if st.button('Who gets the vaccine first?'):	
		st.write('Since we need to ensure that our health system will be able to continuously care for all of us, medical frontliners will be the first to receive the vaccines.')
		st.write('This is to be followed by eligible senior citizens who are at greatest risk of severe infection or deaths. We know from our local data that COVID-19 is more dangerous for the elderly.')
		st.write('The sequence of who will be prioritized have been determined with the help of our experts.')
		st.write('Source: Department of Health - https://doh.gov.ph/vaccines')

	if st.button('If I am not part of the priority group, how will I get access to the vaccine?'):	
		st.write('The government is continuing negotiations to ensure adequate vaccine supply for all Filipinos, including those not in the priority groups.')
		st.write('The objective is to provide equitable access to safe and effective COVID-19 vaccines to the priority eligible groups or almost 70 million Filipinos by 2021, 60-70% of Filipinos by 2022, and followed by the remaining Filipino population in the next three (3) years.')
		st.write('Source: Department of Health - https://doh.gov.ph/vaccines')

	if st.button('How much will I have to pay for the COVID-19 vaccine?'):	
		st.write('Government will provide the vaccine for free. You do not need to pay for anything to be vaccinated.')
		st.write('Source: Department of Health - https://doh.gov.ph/vaccines')
	
	st.subheader('COVID-19 Vaccine Dosage')
	if st.button('Can a second dose of a different vaccine brand be administered?'):	
		st.write('No. The same brand is required to be given for a 2nd dose, to ensure the maximum protection of the vaccinee. The DOH is coordinating with the Local Government Units to ensure allocation of adequate doses of the same Philippine FDA-approved vaccine brand.')
		st.write('Source: Department of Health - https://doh.gov.ph/vaccines/Questions-and-Answers')

	if st.button('What is the interval between the 1st and 2nd dose of COVID vaccine?'):	
		st.write('Interval of doses varies per vaccine. For those currently available, Sinovac is taken 4 weeks (28 days) apart, while AstraZeneca is taken 4 to 12 weeks apart.')
		st.write('Source: Department of Health - https://doh.gov.ph/vaccines/Questions-and-Answers')


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