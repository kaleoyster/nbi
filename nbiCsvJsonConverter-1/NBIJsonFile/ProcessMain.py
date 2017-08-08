'''
Python
Program ProcessMain.py
This program will convert CSV files to JSON file

'''
#Importing Modules
import csv
import os


from nbiEncoder import *
from validationFunctions import *

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
       ]

###### SELECT STATES #######



states = ["AK",
          "AL",
          "AR",
          "AZ",
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
    client = MongoClient('localhost',27017)
    db = client.testDB1
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
    mergedFile = open('mergedJSON.json','w')
    summary = open('Summary.txt','w')
    missingGeo = open('missingeo.txt','w')
    for f in files:
        state , year = f[:2] , int(f[2:6])
        with open(os.path.join('NBIDATA',f),'r') as csvfile:
            reader = csv.reader(csvfile,delimiter = ',')
            headerRow = next(reader,None)
            validationFileName = f[:6] + 'validationLog.txt'
            validation = open(validationFileName,'w')
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
                temp, ErrorCheck = validateNBIfields(temp, ErrorCheck, fieldErrorCountArray,validation,size)
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
                      #print(str(x))
                   except:
                      IndexErrorCount = IndexErrorCount + 1
                      #print("IndexError: ", i)
                      continue
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


'''
with open(SampleFileName, 'r') as f:
    reader = csv.reader(f, delimiter = dEliminater)
    next(reader,None) #skips header
    validation = open('validationLog.txt','w')
    fieldErrorCountArray = []
    size = 150
    fieldErrorCountArray = initializeValidationArray(fieldErrorCountArray,size)
    count = 0  
    for row in reader:
       #print("=" * 50 + 'Line break' + "=" * 50) #Enhance print
       temp = []
       for r in row:
           r = r.strip("'")
           r = r.strip(" ")
           temp.append(r)
       ErrorCheck = []
       #validate
       temp, ErrorCheck = validateNBIfields(temp, ErrorCheck, size)
       if 1 in ErrorCheck:
          pass
       else:
           Longitude, Latitude = convertLongLat(temp[20],temp[19])       
           try:
              count = count + 1
              x = nbiEncoder(temp)
              print(str(x))
           except IndexError as i:
              #print("Error: " , i)
              pass
   
    validation.close() 
''' 

'''
def processFilesMongo(files):
    for f in files:
        state , year = f[:2] , int(f[2:6])
        with open(os.path.join('NBIDATA',f),'r') as csvfile:
            reader = csv.reader(csvfile,delimiter = ',')
            next(reader,None)
            cvc = 0
            RowCount = 0
            for row in reader:
                temp = []
                RowCount = RowCount + 1                
                for r in row:
                    r = r.strip("'")
                    r = r.strip(" ")
                    temp.append(r)
                structureNumber = temp[1]
                Longitude, Latitude = convertLongLat(temp[20],temp[19])
                cvc = countValidCoordinates(Longitude, Latitude, cvc,structureNumber,year)
                x = nbiEncoder(temp,year,Longitude,Latitude)
                mergedFile.write(x)               
            print("================Link==============")
            print('Year: %s, State: %s' %(year, state))                               
            print("Valid Coordinates:", RowCount - cvc)
            print("Invalid Coordinates:", cvc)
            print("Total Records:", RowCount)

'''
#driver function
def main():
    if (fillMongoDB == True):
        processFilesMongo(files)
    else:
        processFilesJSON(files)  


#main function
if __name__ == "__main__":
    main()






