'''
Program Title: NBI BRIDGE JSON ENCODER
VERSION: 1
TEMPLATE: IA16

Author: Akshay Kale
'''

import requests
import csv
import pprint
from io import BytesIO
from zipfile import ZipFile
import urllib.request
import io


from nbiEncoder import nbi_encoder
encoding = 'utf-8'
years = [1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016] #Global variable 
#years= [2013]
#States = ['AL']
States =["AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","HI","IA","ID","IL","IN","KS","KY","MA",'MD',"ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VA","VT","WA","WI","WV","WY"]
#global array States
dEliminater = ',' #Global variable delimeter 


'''
   FUNCTION NAME: def handle_string
   The purpose of this function to sanitize strings of extra white spaces and converts strings
   into integer or float depending on the structure of the string. create URL to crawl on websites

   INPUT PARAMETER: input parameter 's' is a string. 

   OUTPUT: the returning value could be either a string, float or int.

'''

def handle_string(s):
    if(s==''):
       s = 0
    else:
       try:
          result = int(s)
       except ValueError:
          result = float(s)
          return result

'''
   FUNCTION NAME: def createURL()
   The purpose of this function to create a link depending on the input year.
   INPUT PARAMETER: input parameters for this function is 'year' (integer).
                                                           
   OUTPUT: The function returns a custom link for every year and state. 
'''
def createURL(year,state):
    if (year < 2010):
        yr = year
        yr = str(yr)
        link = "https://www.fhwa.dot.gov/bridge/nbi/"+yr+"del.zip"
        return(link)
    else:
        yr = year
        yr = str(yr)
        ste = state
        filename = ste+yr[2:]+".txt"
        link ="https://www.fhwa.dot.gov/bridge/nbi/"+yr+"/delimited/"+filename
        return(link)


def sanitizeLongLat(longitude,latitude):
    lon = longitude
    lat = latitude
    if('.' in lon or '.' in latitude):
        return False
    else:
        return True


'''
   FUNCTION NAME: def convertLongLat()
   The purpose of this function to return a JSON formattd strings from a CSV file.
   
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
FUNCTION NAME: def convertLongLat()

The purpose of this function to return a JSON formattd strings from a CSV file.
   
INPUT PARAMETER: input parameters for this function are 1. Longitude is an integer.
                                                        2. Latitude is an integer.

OUTPUT: The function returns a pair of integer coordinates, longitude and latitude. 
'''

def find_all(name):
    if(name[:2] == '31'):
        return name

'''
   FUNCTION NAME:  driverProgram
 
'''

##if __name__ == '__main__':

'''
 Functions we need:
   1. main function
      -> open file "merged.json"
      -> create url
      -> download using zip file if year < 2010
         elaborate:
                1.
             def main():
                 for year in years:
                     if(year < 2010):
                         csv_url =  createURL(year, "AK")
                         file = downloadZip()
                     else:
                         for state in States:
                             csv_url = createURL(year,state)
                             file = downloadCSV()
                             
 



def downloadZip(csv_url):
    url = urllib.request.urlopen(csv_url)
    with ZipFile(BytesIO(url.read())) as zfile:
                for name in zfile.namelist():
                    fname = find_all(name)
                    with zfile.open(name) as readfile:
                        readfile = io.TextIOWrapper(readfile,encoding,errors='ignore')
                        cr = csv.reader(readfile,delimiter = ',')
                   


def downloadCSV(csv_url,state):
    download = s.get(csv_url)
    print("Downloading...")
   #decode_content = download.content.decode('utf-8')
    decode_content = download.text      
    cr = csv.reader(decode_content.splitlines(),delimiter = ',')
                  
                         
                      
        or download using csv_file if year > 2012
      -> run output file of download function on nbi_encoder
      -> write the the output of download function into a file
 
   2.file downloader
         i. zipfile downloader
         ii. CSV file downloader

'''
def downloadCSV(csv_url,year,s):
    download = s.get(csv_url)
    print("Downloading...")
   #decode_content = download.content.decode('utf-8')
    decode_content = download.text      
    cr = csv.reader(decode_content.splitlines(),delimiter = ',')
    next(cr,None)
    my_list = list(cr)
    return my_list


def downloadProcessZip(name,zfile,s):   
    with zfile.open(name) as readfile:
         readfile = io.TextIOWrapper(readfile,encoding,errors='ignore')
         cr = csv.reader(readfile,delimiter = ',')
         ### processing of the file
         next(cr,None)
         my_list = list(cr)
         return my_list
           

def processNbiRecord(my_list,year,RowCount,f):  
    RowC = RowCount
    for row in my_list:
       #print("======================================================= Line Break ===================================================")
        temp = []         
        count = 0
        for r in row:
            r = r.strip("'")
            r = r.strip(" ")
            count = count + 1
            temp.append(r)                 
        if(count > 118):               
           try:
              Longitude, Latitude = convertLongLat(temp[20],temp[19])
           except:
              Longitude = "NA"
              Latitude = "NA"
           x = nbi_encoder(temp,year,Longitude,Latitude)
           #print(x)
           f.write(x+'\n')
           RowC = RowC + 1
        else:
            continue
    return RowC 


def main():
    RowCount = 0
    with requests.Session() as s:
         f = open("mergedNBI.json", 'w')
         for year in years:
             if(year < 2010):
                csv_url = createURL(year,"AK")
                print("CRAWLING.. : " + csv_url)
                url = urllib.request.urlopen(csv_url)
                print("Downloading...")
                with ZipFile(BytesIO(url.read())) as zfile:
                    for name in zfile.namelist():
                        my_list = downloadProcessZip(name,zfile,s)
                        RowCount = processNbiRecord(my_list,year,RowCount,f)
                        print("[ + ] " + name + " CSV file DONE..")
                print("[ + ]"+ csv_url + " Zip file DONE...")
             if(year > 2009):
                for state in States:
                   csv_url = createURL(year,state) # createsURL wil return crawl 
                   print("CRAWLING..: " + csv_url)
                   my_list = downloadCSV(csv_url,year,s)
                   RowCount = processNbiRecord(my_list,year,RowCount,f)
                   print("[ + ] " + csv_url + " DONE..")
         f.close()
         print("[ ! ] Count of total documents :", RowCount)

if __name__ =="__main__":
   main()

