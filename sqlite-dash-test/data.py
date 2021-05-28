import pandas as pd
from sqlalchemy import create_engine

# Load data from file into a SQLite database
raw_data = pd.read_csv('BankChurners.csv', index_col='CLIENTNUM')
raw_data.pop(raw_data.columns[21])
raw_data.pop(raw_data.columns[20])

engine = create_engine('sqlite:///BankChurners.db')
sqlite_connection = engine.connect()
raw_data.to_sql('data', sqlite_connection, if_exists='replace')



# Pull data table from SQLite, one attribute and multiple metrics
def grab_sql_table(attribute, metrics=[]):
    cols = attribute
    for metric in metrics:
        cols = cols + ', ' + metric
    table = pd.read_sql('SELECT ' + cols + ' FROM data', con=sqlite_connection)

    return table

# Table to sum over metrics within each category (attribute)
def summary_table(attribute, metrics=[]):
    table = grab_sql_table(attribute, metrics)
    categories = list(set(table[attribute]))

    # More elegant solution to this?
    rows = []
    for category in categories:
        row = [0 for metric in metrics]
        for i in range(len(table)):
            if table.iloc[i][attribute] == category:
                row = [row[j] + table.iloc[i][metrics[j]] for j in range(len(metrics))]
        rows.append(row)

    df = pd.DataFrame(data = rows, index=categories, columns=metrics)

    return df

# Income category table
def income_category():
    income_category = summary_table('Income_Category', ['Credit_Limit', 'Total_Revolving_Bal'])
    income_category['Avg_Utilization_Ratio'] = income_category['Total_Revolving_Bal'] / income_category['Credit_Limit']
    income_category.to_sql('income_category', sqlite_connection, if_exists='replace')
    income_category = income_category.reindex(index = ['Unknown', 'Less than $40K', '$40K - $60K', '$60K - $80K', '$80K - $120K', '$120K +'])
    return income_category

def education_category():
    education_category = summary_table('Education_Level', ['Credit_Limit', 'Total_Revolving_Bal'])
    education_category['Avg_Utilization_Ratio'] = education_category['Total_Revolving_Bal'] / education_category['Credit_Limit']
    education_category.to_sql('education_category', sqlite_connection, if_exists='replace')
    education_category = education_category.reindex(index = ['Unknown', 'Uneducated', 'High School', 'College', 'Graduate', 'Post-Graduate', 'Doctorate'])
    return education_category


# sqlite_connection.close()