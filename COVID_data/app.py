import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import COVID_data

tot_deaths_country = COVID_data.country_table('total_deaths')

#st.title ("My App")

#st.header("Deploying Streamlit")



activities = ["Country Comparison","Per Country"]
choices = st.sidebar.selectbox('Select Dashboard', activities)


if choices == 'Country Comparison':
	st.header("Country Comparison")

	# Filters
	st.sidebar.header("Filters")
	options = st.sidebar.multiselect('Select Countries:', COVID_data.countries(), default=['United Kingdom', 'United States', 'France'])
	slider = st.sidebar.slider('Select date range:', min_value=COVID_data.dates[0], max_value=COVID_data.dates[1], value=[COVID_data.dates[0], COVID_data.dates[0]])
	
	# First Table
	

	# First Chart
	st.header("Explore Metrics")
	metric = st.selectbox('Select Metric:', COVID_data.features)
	st.line_chart(data=COVID_data.country_table(metric, options, slider))

	# Second Chart
	st.header("Case Fatality Rate")
	st.write("The Case Fatality Rate is the ratio between confirmed deaths and confirmed cases.")
	st.line_chart(data=COVID_data.case_fatality_rate(options, slider))

elif choices == 'Per Country':
	st.header("Per Country")

	# Filters
	st.sidebar.header("Filters")
	options = st.sidebar.selectbox('Select Country:', COVID_data.countries(), index=0)
	options = [options]
	slider = st.sidebar.slider('Select date range:', min_value=COVID_data.dates[0], max_value=COVID_data.dates[1], value=[COVID_data.dates[0], COVID_data.dates[0]])

	# First Chart
	metric = st.selectbox('Select Metric:', COVID_data.features)
	st.line_chart(data=COVID_data.country_table(metric, options, slider))