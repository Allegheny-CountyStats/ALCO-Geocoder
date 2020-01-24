#!/usr/bin/env python
# coding: utf-8
import requests
import json
import pandas as pd
import re
import numpy as np

# Function to Geocode using the Allegheny County Geocoder
def county_geocode (address):
    # Base URL
    url = "http://gisdata.alleghenycounty.us/arcgis/rest/services/Geocoders/Composite/GeocodeServer/findAddressCandidates"
    
    # Query string
    query = {"SingleLine": address ,"outSR":"4326","f":"pjson"}
    # GET request
    r = requests.request("GET", url, params=query)
    j = r.json()['candidates']
    c = pd.DataFrame.from_dict(j)
    
    # If there are results grab X Y
    if c.shape[0] > 0:
        top = c.head(1)
        locs = str(top['location'])
        x = re.search(': (.+?),', locs).group(1)
        y = re.search('\'y\': (.+?)}', locs).group(1)
        df = pd.DataFrame({'X': [x], 'Y': [y]})
    # Handle no locations
    else:
        df = pd.DataFrame({'X': [np.nan], 'Y': [np.nan]})
        
    return(df)

# Function to Geocode using the Allegheny County Geocoder on a Pandas DataFrame
def county_geo_pd (df, col = 'Address'):
    # Build empty pd
    final = pd.DataFrame({'X' : [], 'Y' : []})
    
    # Geocode each rows
    for index, row in test.iterrows():
        temp = county_geocode(row['Address'])
        final = final.append(temp)
        
    # Bind complete geocoders to initial dataframe
    return(pd.concat([df, final.reset_index(drop=True)], axis = 1))

