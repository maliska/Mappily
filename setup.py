import csv
import pickle
import plotly 
plotly.tools.set_credentials_file(username='[Insert Plotly Username]', api_key='[Insert Plotly Key]')

out = []

with open('cities.csv', 'rb') as csvfile:
  cities = csv.reader(csvfile)
  for city in cities:
    out.append([city[0].strip().lower(),city[1],city[2],city[3]])

pickle.dump(out, open('cities.p', 'wb'))