'''
Python
Program ProcessMain.py
This program will convert CSV files to JSON file

'''
#Importing Modules

import csv
import os
from urllib.request import urlopen

from nbiEncoder import *
from validationFunctions import *
from crossValidationFunctions import *

####### MongoDB    ##########
fillMongoDB = False

# Note: Default value for fillMongoDB is false
#importing directly to MongoDB is not yet not properly implemented
#the issue is being handled and will be updated as soon as possible
###### SELECT YEARS #########

years = [1992,
         1993,
         1994,
         1995,
         1996,
         1997,
         1998,
         1999,
         2000,
         2001,
         2002,
         2003,
         2004,
         2005,
         2006,
         2007,
         2008,
         2009,
         2010,
         2011,
         2012,
         2013,
         2014,
         2015,
         2016,
         2017
       ]

###### SELECT STATES #######


states = ["AK",
          "AZ",
          "AL",
          "AR",
          "CA",
          "CO",
          "CT",
          "DC",
          "DE",
          "FL",
          "GA",
          "HI",
          "IA",
          "ID",
          "IL",
          "IN",
          "KS",
          "KY",
          "MA",
          "MD",
          "ME",
          "MI",
          "MN",
          "MO",
          "MS",
          "MT",
          "NC",
          "ND",
          "NE",
          "NH",
          "NJ",
          "NM",
          "NV",
          "NY",
          "LA",
          "OH",
          "OK",
          "OR",
          "PA",
          "PR",
          "RI",
          "SC",
          "SD",
          "TN",
          "TX",
          "UT",
          "VA",
          "VT",
          "WA",
          "WI",
          "WV",
          "WY"]

files = [] #global variable for Files

#Connection to MongoDB
def get_db():
    from pymongo import MongoClient
    file = open("dbConnect.txt", 'r')
    dbConnectionString = str(file.read()).strip()
    client = MongoClient(dbConnectionString)
    db = client.bridge
    return db


#return a list of files which will helpful for renaming files
def createFileList(states,years):
    files = []
    for state in states:
        for year in years:
            yr = str(year)
            f = state + yr + '.txt'
            files.append(f)
    return files


files = createFileList(states,years)

#convertion of geo co-ordinates
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


def countValidCoordinates(Longitude, Latitude, cvc, structureNumber, year,missingGeo):
    if (Longitude == -0.0 and Latitude == 0.0):
        cvc = cvc + 1
        print('year: %d, Structure Number: %s' % (year, structureNumber),file=missingGeo)
    return cvc



# how to close file with open technique
def processFilesJSON(files):
    directory = 'ValidationLog'
    crossValidationDirectory = 'CrossValidationLog'
    mergedFile = open('mergedJSON.json','w')
    summary = open('Summary.txt','w')
    missingGeo = open('missingeo.txt','w')
    if not os.path.exists(directory):
       os.makedirs(directory)
       os.makedirs(crossValidationDirectory)
    for f in files:
        state , year = f[:2] , int(f[2:6])
        with open(os.path.join('NBIDATA',f),'r', encoding='utf-8', errors = 'ignore') as csvfile:
            reader = csv.reader(csvfile,delimiter = ',')
            headerRow = next(reader,None)
            validationFileName = f[:6] + 'validationLog.txt'
            crossValidationFileName = f[:6] + 'CrossValidationLog.txt'
            validation = open(os.path.join(directory,validationFileName),'w')
            crossValidation = open(os.path.join(crossValidationDirectory,crossValidationFileName),'w')
            fieldErrorCountArray = []
            size = 150
            fieldErrorCountArray = initializeValidationArray(fieldErrorCountArray,size)
            cvc = 0
            RowCount = 0
            IndexErrorCount = 0
            fieldSizeCount = []
            fieldSizeDict = {}
            for row in reader:
                temp = []
                RowCount = RowCount + 1
                for r in row:
                    r = r.strip("'")
                    r = r.strip(" ")
                    temp.append(r)
                ErrorCheck = []
                temp, ErrorCheck = validateNBIfields(temp, ErrorCheck, fieldErrorCountArray,validation,size,year)
                crossCheckValidation(temp,crossValidation)
                fieldSize = len(temp)
                fieldSizeCount.append(fieldSize)
                fieldErrorCountArray[fieldSize] = fieldErrorCountArray[fieldSize] + 1
                if 1 in ErrorCheck:
                   pass
                else:
                   structureNumber = temp[1]
                   Longitude, Latitude = convertLongLat(temp[20],temp[19])
                   cvc = countValidCoordinates(Longitude, Latitude, cvc,structureNumber,year,missingGeo)
                   try:
                      x = nbiEncoder(temp,year,Longitude,Latitude)
                   except IndexError as i:
                      IndexErrorCount = IndexErrorCount + 1
                      print("IndexError: ", i)
                      continue
                   #print(x)
                   mergedFile.write(x)
            fieldSizeDict = {x: fieldSizeCount.count(x) for x in fieldSizeCount}
            print("===================================",file=summary)
            print('Year: %s, State: %s' %(year, state),file=summary)
            print("Valid Coordinates:", RowCount - cvc, file=summary) #valid coordinates includes coordinates which have longitude latitude with in proper range.
            print("Invalid Coordinates:", cvc, file=summary) #Invalid coordinates includes coordinates which have value'0' or ' '
            print("Total Records:", RowCount, file=summary)
            print('Index Error Count: ', IndexErrorCount)
            print('Year: %s, State: %s' %(year, state))
            print(fieldSizeDict)
    validation.close()
    missingGeo.close()
    summary.close()
    mergedFile.close()


def processFilesMongo(files):
    myDb = get_db()
    myCollection =myDb['nbi']
    directory = 'ValidationLog'
    crossValidationDirectory = 'CrossValidationLog'
    summary = open('Summary.txt','w')
    missingGeo = open('missingeo.txt','w')
    if not os.path.exists(directory):
       os.makedirs(directory)
       os.makedirs(crossValidationDirectory)
    for f in files:
        state , year = f[:2] , int(f[2:6])
        with open(os.path.join('NBIDATA',f),'r', encoding='utf-8', errors = 'ignore') as csvfile:
            reader = csv.reader(csvfile,delimiter = ',')
            headerRow = next(reader,None)
            validationFileName = f[:6] + 'validationLog.txt'
            crossValidationFileName = f[:6] + 'CrossValidationLog.txt'
            validation = open(os.path.join(directory,validationFileName),'w')
            crossValidation = open(os.path.join(crossValidationDirectory,crossValidationFileName),'w')
            fieldErrorCountArray = []
            size = 150
            fieldErrorCountArray = initializeValidationArray(fieldErrorCountArray,size)
            cvc = 0
            RowCount = 0
            IndexErrorCount = 0
            fieldSizeCount = []
            fieldSizeDict = {}
            for row in reader:
                temp = []
                RowCount = RowCount + 1
                for r in row:
                    r = r.strip("'")
                    r = r.strip(" ")
                    temp.append(r)
                ErrorCheck = []
                temp, ErrorCheck = validateNBIfields(temp, ErrorCheck, fieldErrorCountArray,validation,size,year)
                crossCheckValidation(temp,crossValidation)
                fieldSize = len(temp)
                fieldSizeCount.append(fieldSize)
                fieldErrorCountArray[fieldSize] = fieldErrorCountArray[fieldSize] + 1
                if 1 in ErrorCheck:
                   pass
                else:
                   structureNumber = temp[1]
                   Longitude, Latitude = convertLongLat(temp[20],temp[19])
                   cvc = countValidCoordinates(Longitude, Latitude, cvc,structureNumber,year,missingGeo)
                   try:
                      x = nbiEncoder(temp,year,Longitude,Latitude)
                   except IndexError as i:
                      IndexErrorCount = IndexErrorCount + 1
                      print("IndexError: ", i)
                      continue
                   myCollection.insert_one(json.loads(x))
            fieldSizeDict = {x: fieldSizeCount.count(x) for x in fieldSizeCount}
            print("===================================",file=summary)
            print('Year: %s, State: %s' %(year, state),file=summary)
            print("Valid Coordinates:", RowCount - cvc, file=summary) #valid coordinates includes coordinates which have longitude latitude with in proper range.
            print("Invalid Coordinates:", cvc, file=summary) #Invalid coordinates includes coordinates which have value'0' or ' '
            print("Total Records:", RowCount, file=summary)
            print('Index Error Count: ', IndexErrorCount)
            print('Year: %s, State: %s' %(year, state))
            print(fieldSizeDict)
    validation.close()
    missingGeo.close()
    summary.close()




#driver function
def main():
    if (fillMongoDB == True):
        processFilesMongo(files)
    else:
        processFilesJSON(files)


#main function
if __name__ == "__main__":
    main()
