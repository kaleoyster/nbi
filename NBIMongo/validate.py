import requests
import csv
from io import BytesIO
from zipfile import ZipFile
import urllib.request

# import libraries
from createURL import createURL
from download import downloadCSV
from general import convertLongLat

#importing geopy 
from geopy.geocoders import Nominatim

#delcaration of variables
years = [2010]
states = ['NE']

dEliminater = ','


def main():
    with requests.Session() as s:
         f = open('results.txt', 'w')
         for year in years: 
             for state in states:
                 csv_url = createURL(year,state)
                 datalist = downloadCSV(csv_url,year,s)
                 for row in datalist: 
                     temp = []
                     for r in row:
                         r = r.strip("'")
                         r = r.strip("")
                         temp.append(r)
                     lon , lat = convertLongLat(temp[20], temp[19])
                     lon = str(lon)
                     lat = str(lat)
                     
                     coordinates = str(lat+","+lon)
                     geolocator = Nominatim()
                     location = geolocator.reverse(coordinates)
                     f.write(location.address)
          
         f.close()

main() 
