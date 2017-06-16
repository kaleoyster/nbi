import csv
import os


from nbiEncoder import nbiEncoder


###### SELECT STATES ########
states = ['NE']

###### SELECT YEARS #########  
#years = [1992,1993,1994,1995]

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

#states= ['NE']
#years = ['1992']


files = [] #global variable for Files

#return a list
def createFileList(states,years):
    files = []
    for state in states:
        for year in years:
            yr = str(year)
            f = state + yr + '.txt'
            files.append(f)
    return files
# 
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


def countValidCoordinates(Longitude, Latitude, cvc, structureNumber, year):
    if (Longitude == -0.0 and Latitude == 0.0):
        cvc = cvc + 1
        print('year: %d, Structure Number: %s' % (year, structureNumber))
    return cvc

def geoBoundaryCheck(Longitude,Latitude,validCounter,boundC):
    if((Longitude > -180 and Longitude < 180) and (Latitude > -85 and Latitude< 85)):
        validCounter = validCounter + 1
    else:
        print('InValid: ', Longitude, Latitude, file = boundC)
    return validCounter
            

def processFile(files):
    boundC = open('BoundaryCheck.txt','w')
    BoundCheckSummary = open('BoundarySummary.txt','w')
    Records = {}
    for f in files:
        state , year = f[:2] , int(f[2:6])
        with open(os.path.join('NBIDATA',f),'r') as csvfile:
            reader = csv.reader(csvfile,delimiter = ',')
            next(reader,None)
            cvc = 0
            RowCount = 0
            validCounter = 0
            for row in reader:
                temp = []
                RowCount = RowCount + 1                
                for r in row:
                    r = r.strip("'")
                    r = r.strip(" ")
                    temp.append(r)
                structureNumber = temp[1]
                Longitude, Latitude = convertLongLat(temp[20],temp[19])
                validCounter = geoBoundaryCheck(Longitude,Latitude,validCounter,boundC)
                Records[structureNumber] = [Longitude, Latitude]  
            print('=====================================================================',file =BoundCheckSummary)
            print('Year: %s, State: %s' %(year, state),file =BoundCheckSummary)
            print('Geo Coordinates within valid range: ',validCounter,file =BoundCheckSummary)
            print('Geo Coordinates not within valid range: ', RowCount - validCounter,file =BoundCheckSummary)
            print('Record size: ', len(Records),file =BoundCheckSummary)
    #convert dictionary into csv file
    with open('structureGeoCoordinates.csv','w') as csvfile:
         fieldnames = ['Structure Number','Longitude','Latitude']
         writer = csv.writer(csvfile,delimiter=',')
         writer.writerow(fieldnames)
         for r in Records.items():
             structureNumber = r[0]
             Longitude =r[1][0]
             Latitude = r[1][1]
             rlist=[structureNumber,Longitude,Latitude]
             writer.writerow(rlist)    
    boundC.close()
    BoundCheckSummary.close() 
                
def main():
    files = createFileList(states,years)
    processFile(files)  



if __name__ == "__main__":
    main()






