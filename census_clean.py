# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:38:08 2020

@author: elmer camargo
"""

#https://www.bloomberg.com/graphics/2020-new-york-coronavirus-outbreak-how-many-hospital-beds/
#https://profiles.health.ny.gov/hospital/county_or_region/ - SCRAPE

import os
os.chdir('C:/Users/elmsc/Documents/gis/che-covid19')

import pandas as pd
from src.census_help import census_clean
import geopandas as gpd



path = 'data/census/new_york/'
dirs = []

for i in os.listdir(path):
        if os.path.isdir(path+i):
            dirs.append(i)

census = {}
keys = {}

for i in range(0,len(dirs)):
    name = dirs[i]
    census[name] = pd.read_csv(path + name + '/' + name + '.csv')
    #check keys.csv uniqueness here
    keys[name] = pd.read_csv(path + name + '/' + name + '_key.csv')
del(i,name)
  
for i in range(0,len(dirs)):
    census[dirs[i]] = census_clean(census[dirs[i]], keys[dirs[i]])
del(i)

ny = pd.DataFrame()
ny['GEOID_ZIP'] = census[dirs[1]]['GEOID_ZIP'] # only grabs the geoid

# puts all vars in single df
for i in range(0,len(dirs)):
    temp = census[dirs[i]]
    ny = ny.merge(temp, on = 'GEOID_ZIP')
del(i,temp)


ny = ny.drop(ny.index[0]) # THIS DROPS THE FIRST ROW OF THE DF THAT HAS WORDS
ny = ny.reset_index(drop = True)

# ny.columns.duplicated() # used to debug duplicated col name
cols = ny.columns.drop('GEOID_ZIP')
ny[cols] = ny[cols].apply(pd.to_numeric, errors='coerce') #assign all cols to numeric

#ny['PERCENT_POV'] = ny['pop_below_pov']/ny['pop_pov']

ny_zip = gpd.read_file('data/shp/zip/new_york_zip.shp')
# print(ny_zip.crs) # NAD83

ny_zip = ny_zip.to_crs({'init': 'epsg:4326'}) #WGS84
ny_zip = ny_zip.rename(columns = {'GEOID10':'GEOID_ZIP'})
ny_zip = ny_zip.merge(ny, on = 'GEOID_ZIP')


#ny_zip.to_file('ny++.geojson', driver = 'GeoJSON')
#ny_zip.to_file('ny++.gpkg', driver = 'GPKG')
ny_zip.to_file('output/shp/ny++.shp')



# boroughs = gpd.read_file('data/shp/ny_boroughs/borough.geojson')