# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:19:16 2020

@author: elmsc
"""

def census_clean(df, key):
    df = df[key['census_id']]
    
    for i in range(0,len(key['census_id'])):
        df = df.rename(columns = {key['census_id'][i]:key['desc'][i]})
    del(i)
    return df