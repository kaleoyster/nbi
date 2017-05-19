'''
Program Title: Sanitize
PURPOSE: Contains Sanitization functions
VERSION: 
TEMPLATE:
Author: Akshay Kale
'''



'''
   FUNCTION NAME: def handle_string
   The purpose of this function is to sanitize strings of extra white spaces and converts strings
   into integer or float depending on the structure of the string. create URL to crawl on websites

   INPUT PARAMETER: input parameter 's' is a string. 

   OUTPUT: the returning value could be either a string, float or int.

'''
def handleString(s):
    if(s==''):
       s = 0
    else:
       try:
          result = int(s)
       except ValueError:
          result = float(s)
          return result


'''
   FUNCTION NAME: def sanitizeLongLat()
   The purpose of this function is to find incorrect values for Latitude and Longitude 
   and correct or replace all incorrect or empty values.
 
   INPUT PARAMETER: input parameters for this function are 1. Longitude is an integer.
                                                           2. Latitude is an integer.
                                                           
   OUTPUT: The function returns a True or False
'''

def sanitizeLongLat(longitude,latitude):
    lon = longitude
    lat = latitude
    if('.' in lon or '.' in latitude):
        return False
    else:
        return True
