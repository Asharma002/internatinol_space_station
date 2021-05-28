# program to find international space station..


import pandas as pd
import numpy as np
import plotly.express as px
url = 'http://api.open-notify.org/iss-now.json'
df = pd.read_json(url)
print(df)
df['latitude'] = df.loc['latitude','iss_position']
df['longitude'] = df.loc['longitude','iss_position']
df.reset_index(inplace = True)
print(df)
df2 = px.data.gapminder().query("year == 2007")
fig1 = px.scatter_geo(df2, locations="iso_alpha",
                     color="continent", # which column to use to set the color of markers
                     hover_name="country", # column added to hover information
                     size="pop", # size of markers
                     projection="natural earth")
fig1.show()


fig = px.scatter_geo(df,lat ='latitude', lon = 'longitude')
fig.show()


























