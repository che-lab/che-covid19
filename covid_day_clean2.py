import os
import pandas as pd
import download_covid19_data


# Change to directory with the CSV files
os.chdir('/Users/geoffreyhughes/Projects/Work/COVID-19/che-covid19/data/csse_covid_19_daily_reports')


# Clear previous CSVs if they exist
if os.path.isfile('raw_data.csv'):
    os.remove('raw_data.csv')

if os.path.isfile('clean_data.csv'):
    os.remove('clean_data.csv')


# Read all CSV data
all_csv = [file_name for file_name in os.listdir(os.getcwd()) if '.csv' in file_name]
li = []


# Combine all CSV data. If missing an attribute, leave blank (NaN)
for filename in all_csv:
    df = pd.read_csv(filename, index_col=None, header=0, parse_dates=True, infer_datetime_format=True)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True, sort=True)

if os.path.isfile('raw_data.csv'):
    os.remove('raw_data.csv')
frame.to_csv('raw_data.csv', index=False)


# Check for similar attributes and combine them
# Using x_y naming convention (underscores)
# e.g. 'Long_' -> 'Longitude'; 'Country/Region' -> 'Country_Region'
print(len(li))
print(len(li))
print(len(frame))

# 'Country/Region' -> 'Country_Region'
frame['Country_Region'] = frame['Country/Region'].fillna('') + frame['Country_Region'].fillna('')
del frame['Country/Region']

# 'Province/State' -> 'Province_State'
frame['Province_State'] = frame['Province/State'].fillna('') + frame['Province_State'].fillna('')
del frame['Province/State']

# 'Lat' -> 'Latitude'
frame['Latitude'] = frame['Lat'].fillna(0) + frame['Latitude'].fillna(0)
del frame['Lat']
frame['Latitude'].replace([0, 0.0], '', inplace=True)

# 'Long_' -> 'Longitude'
frame['Longitude'] = frame['Long_'].fillna(0) + frame['Longitude'].fillna(0)
del frame['Long_']
frame['Longitude'].replace([0, 0.0], '', inplace=True)


if os.path.isfile('clean_data.csv'):
    os.remove('clean_data.csv')
frame.to_csv('clean_data.csv', index=False)

# Delete working variables; Done
del(li, df, frame)
