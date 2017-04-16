import pickle
import facebook
import json
import plotly.plotly as py
from plotly.graph_objs import *
from time import sleep

# import city names
cities = pickle.load(open('cities.p', 'rb'))

# function to get city coordinates
def getLatLon(str):
  str = str.strip().lower()
  pop = 0	
  for city in cities:
    if city[0] == str:
      return [city[2], city[3]]
  return -1

# parse facebook comments
token = '[Insert Token]' #facebook user token
post_id = '[Insert Id]' #facebook post id

mapbox_access_token = '[Insert Token]' #mapbox access token

visits0 = []

graph = facebook.GraphAPI(access_token=token, version='2.7', )

while True:
  comments = graph.get_connections(id=post_id,connection_name='comments')["data"]

  i = 0
  names = []
  visits = []
  lats = []
  lons = []
  for comment in comments:
    name = comment["from"]["name"]
    message = comment["message"].strip().lower()
    for city in cities:
      if city[0] in message and name not in names:
        names.append(name)
        visits.append(name + ': ' + city[0])
        lats.append(city[2])
        lons.append(city[3])
        print [name,city]
        break
    i = i + 1
  if visits != visits0:
    visits0 = visits
    # Map it
    data = Data([
      Scattermapbox(
        lat=lats,
        lon=lons,
        marker=Marker(
          size=14
        ),
        text=visits      )
    ])
    layout = Layout(
      autosize=True,
      mapbox=dict(
        accesstoken=mapbox_access_token,
        center=dict(
          lat=39,
          lon=-98
        ),
        zoom=4
      )
    )
    fig = dict(data=data, layout=layout)
    py.plot(fig, filename='Road Trip')
    print names
    print visits
    print 'Map updated!'
  sleep(20)