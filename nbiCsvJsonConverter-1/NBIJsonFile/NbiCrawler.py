'''
Program Title: NBI BRIDGE JSON ENCODER
VERSION: 1
Template: NBI Record Format
Author: Akshay Kale
'''

import requests
import csv

from io import BytesIO
from zipfile import ZipFile
import urllib.request

from createURL import createURL
from download import downloadCSV, browseZip
from processNbiData import processNbiRecord
from sanitize import handleString, sanitizeLongLat
from general import convertLongLat

years = [1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016] #Global variable 
States =["AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","HI","IA","ID","IL","IN","KS","KY","MA",'MD',"ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VA","VT","WA","WI","WV","WY"]
#global array States
dEliminater = ',' #Global variable delimeter 

'''
FUNCTION NAME: def main()
This function is a driver program.
'''
def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost',27017)
    db = client.testDB1
    return db 

 
def main():
    myDb = get_db()
    myCollection = myDb.testDB1
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
                        my_list = browseZip(name,zfile,s) 
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

