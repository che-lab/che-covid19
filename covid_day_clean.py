import os
import pandas as pd

#os.chdir('C:/Users/elmsc/Documents/gis/che-covid19')
os.chdir('/Users/geoffreyhughes/Projects/Work/COVID-19/che-covid19')

#path = 'data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/'
path = 'data/'

# Stores all csvs as df within a dictionary

csv = [f for f in os.listdir(path) if f.endswith('.csv') and os.path.isfile(os.path.join(path, f))]
csv_count = len(csv)

global_dict = {}

for i in range(0,csv_count):
    name = csv[i]
    global_dict[name] = pd.read_csv(path + name)

del(i,name,csv_count)
len(global_dict)

#test = days[csv[0]] # assigning df
#test['Country/Region'].unique()
#list(test) # list column names for df

# goes through global cases dict and filters for only US cases
# I use 2 try excepts because col names change between using '/' and '_'

us_dict = {}
for i in range(0,len(global_dict)):
    temp = global_dict[csv[i]]
    try:
        us_temp = temp[temp['Country/Region'] == 'US']
    except:
        try:
            us_temp = temp[temp['Country_Region'] == 'US']
        except: print("error")
    us_dict[csv[i]] = us_temp
del(us_temp,temp)

# same as above but now scoping to NY

ny_dict = {}
for i in range(0,len(us_dict)):
    temp = us_dict[csv[i]]
    try:
        ny_temp = temp[temp['Province/State'] == 'New York']
    except:
        try:
            ny_temp = temp[temp['Province_State'] == 'New York']
        except: print("error")
    ny_dict[csv[i]] = ny_temp
del(ny_temp,temp)

#ny_df = pd.DataFrame()

csv[63]
df = ny_dict[csv[63]]

list(df)

#github test
