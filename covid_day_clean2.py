import os
import pandas as pd


os.chdir('/Users/geoffreyhughes/Projects/Work/COVID-19/che-covid19/data')
all_csv = [file_name for file_name in os.listdir(os.getcwd()) if '.csv' in file_name]

li = []

for filename in all_csv:
    df = pd.read_csv(filename, index_col=None, header=0, parse_dates=True, infer_datetime_format=True)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True), sort=True)
frame.to_csv('melted_csv.csv', index=False)
