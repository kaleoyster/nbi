'''
Program Title: General
Purpose: Contains general functions.
VERSION: 
TEMPLATE: 

Author: Akshay Kale
'''

'''
   FUNCTION NAME: def convertLongLat()
   The purpose of this function is to return a JSON formattd strings from a CSV file.
   
   INPUT PARAMETER: input parameters for this function are 1. Longitude is an integer.
                                                           2. Latitude is an integer.

   OUTPUT: The function returns a pair of integer coordinates, longitude and latitude. 
'''
def convertLongLat(longitude,latitude):
   try:
        lat = latitude
        latDegree = int(lat[:2])
        latMin = int(lat[2:4])
        latMin = (latMin/60)
        latSec = int(lat[4:8])
        latSec = (latSec/360000)
        latDecimal = latDegree + latMin + latSec
        long = longitude
        longDegree = int(long[:3])
        longMin = int(long[3:5])
        longMin = (longMin/60)
        longSec = int(long[5:9])
        longSec = (longSec/360000)
        longDecimal = -(longDegree + longMin + longSec)
        return longDecimal, latDecimal
   except:
        return 0.00, 0.00


'''
FUNCTION NAME: def find_all()

This function is not yet built.
   
INPUT PARAMETER: 
OUTPUT:  
'''

def find_all(name):
    if(name[:2] == '31'):
        return name

