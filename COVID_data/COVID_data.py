import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


# Load data from OWID website and save it in csv file
# Save data to csv file
url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
data = pd.read_csv(url)
data.to_csv('COVID_data.csv')
print ('Saved to CSV')


data = pd.read_csv('COVID_data.csv')

features = data.columns[5:]

# Convert date to datetime object
dates = pd.to_datetime([min(data.date), max(data.date)]).to_pydatetime()


def countries():
    countries = set(data['location'])
    countries = list(countries)
    countries.sort()
    return countries


def country_table(metric, countries=countries(), dates=dates):

    features = ['date', metric]

    df_final = pd.DataFrame()
    for country in countries: 
        df = data[data['location']==country][features]
        df.set_index(['date'], inplace=True)
        df.columns=[country]
        df_final = pd.concat([df_final,df], 1)

    df_final.index = pd.to_datetime(df_final.index).to_pydatetime()
    df_final.sort_index(inplace=True)

    return df_final[(df_final.index >= dates[0]) & (df_final.index <= dates[1])]


def case_fatality_rate(countries=countries(), dates=dates):
    # The Case Fatality Rate is the ratio between confirmed deaths and confirmed cases
    deaths = country_table('total_deaths', countries, dates)
    cases = country_table('total_cases', countries, dates)

    result = deaths.div(cases)

    return result

#### LEFT OFF HERE ####
def summary_table(countries=countries(), date=max(dates)):
    # Summary tables showing below metrics per country selected
    #   - Total Deaths (per million)
    #   - Total Cases (per million)
    #   - Total Vaccinations (per hundred)
    #   - Total hospitilizations (per million)
    #   - Total ICU patients (per million)
    #   - Case Fatality Rate

    ls = ['total_deaths_per_million', 'total_cases_per_million', 'total_vaccinations_per_hundred', 'hosp_patients_per_million', 'icu_patients_per_million']
    data = []
    for metric in ls:
        metric_data = country_table(metric, countries, [date, date])
        metric_data.index = [metric]
        data.append(metric_data)

    
    
    df = pd.concat(data)
    
    print (df)
    

summary_table(['United Kingdom', 'France'])
    



