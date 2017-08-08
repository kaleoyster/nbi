#import modules
import csv

#global variable
filename = 'structureGeoCoordinates.csv'
#open csv file and find missing values
missingValue = open('MissingGeoCoordinates.txt','w')
count = 0
with open(filename,'r') as csvfile:
     reader = csv.reader(csvfile,delimiter=',')
     for row in reader:
         structure_number = row[0]
         longitude = row[1]
         latitude = row[2]
         if(longitude == '-0.0' and latitude == '0.0'):
            count = count + 1 
            print(structure_number,file = missingValue)
     print(count)
