import os
import pandas as pd


os.chdir('/Users/geoffreyhughes/Projects/Work/COVID-19/che-covid19/data')



# Read all CSV data
all_csv = [file_name for file_name in os.listdir(os.getcwd()) if '.csv' in file_name]
li = []


# Combine all CSV data. If missing an attribute, leave blank (null)
# e.g. 'Long_' -> 'Longitude'
for filename in all_csv:
    df = pd.read_csv(filename, index_col=None, header=0, parse_dates=True, infer_datetime_format=True)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True, sort=True)

if os.path.isfile('raw_data.csv'):
    os.remove('raw_data.csv')
frame.to_csv('raw_data.csv', index=False)


# Check for similar attributes and combine them
# e.g. 'Long_' -> 'Longitude'
print(len(li))


print(len(li))
print(len(frame))


# goes through global cases dict and filters for only US cases
# I use 2 try excepts because col names change between using '/' and '_'

# us_dict = {}
# for i in range(0,len(global_dict)):
#     temp = global_dict[csv[i]]
#     try:
#         us_temp = temp[temp['Country/Region'] == 'US']
#     except:
#         try:
#             us_temp = temp[temp['Country_Region'] == 'US']
#         except: print("error")
#     us_dict[csv[i]] = us_temp
# del(us_temp,temp)


del(li, df, frame)
