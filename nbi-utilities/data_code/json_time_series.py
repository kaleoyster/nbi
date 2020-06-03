"""Contains functions that extract nbi data from mongodb and convert into json"""
import csv
import pandas as pd
import numpy as np
from collections import defaultdict
from collections import deque

__author__ = 'Akshay Kale'
__copyright__ = 'GPL'
__credit__ = []
__email__ = 'akale@unomaha.edu'

# Import JSON Dump data model
# Function to connect to mongodb and return connection object
def connectMongo():
    pass

# Function to query mongodb given the connection object 
# and query return json format
def queryMongo(query, connection):
    pass

# Function to convert the json object into timeseries json object
def toTimeseries(jsonObject):
    return jsonTimeSeries

# Function to populate mongodb with the timeseries json object
def populateMongo(jsonTimeSeries):
    return status

def main():
    filename = ''
    pass

if __name__ == '__main__':
   main()


