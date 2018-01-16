'''
Program: Download.py
Version: 1
Purpose: Downloads zip files and csvfiles from NBI and extracts them

'''
#Importing Modules
import requests 
import zipfile
import io
import os
from urllib.request import urlopen

# years global variable 
years = [
        1992,
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
        2016]

#states global variable
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

#Dictionary - for rename function
fileNameDict = {'25fluna':'MA',
                '04fluna':'AZ', 
                '08fluna':'CO', 
                '38fluna':'ND', 
                '09fluna':'CT', 
                '19fluna':'IA', 
                '26fluna':'MI', 
                '48fluna':'TX',
                '35fluna':'NM', 
                '17fluna':'IL', 
                '51fluna':'VA', 
                '23fluna':'ME',
                '16fluna':'ID',
                '36fluna':'NY',
                '56fluna':'WY',
                '29fluna':'MO',
                '39fluna':'OH',
                '28fluna':'MS', 
                '11fluna':'DC',
                '21fluna':'KY', 
                '18fluna':'IN',
                '06fluna':'CA',
                '47fluna':'TN', 
                '12fluna':'FL',
                '24fluna':'MD',
                '34fluna':'NJ', 
                '46fluna':'SD',
                '13fluna':'GA',
                '55fluna':'WI',
                '30fluna':'MT',
                '54fluna':'WV',
                '15fluna':'HI', 
                '32fluna':'NV', 
                '37fluna':'NC',
                '10fluna':'DE', 
                '33fluna':'NH', 
                '44fluna':'RI', 
                '50fluna':'VT', 
                '42fluna':'PA', 
                '05fluna':'AR', 
                '20fluna':'KS', 
                '45fluna':'SC',
                '22fluna':'LA',
                '40fluna':'OK', 
                '72fluna':'PR', 
                '41fluna':'OR', 
                '27fluna':'MN', 
                '53fluna':'WA', 
                '01fluna':'AL', 
                '31fluna':'NE',
                '02fluna':'AK', 
                '49fluna':'UT'
               }

#renames all downloaded files by using the above dictionary
def rename(fileNameDict):
    for root,dirs,filenames in os.walk('NBIDATA'):
        for f in filenames:
            try:
               oldFileName, year = f[:7],f[10:14]
               if(oldFileName =='stfluna'):
                  os.remove(root+os.sep+f)
               else:
                  print('Renamed...',f)
                  os.rename(root+os.sep+f,root+os.sep+fileNameDict[oldFileName]+year+'.txt')
            except:
               pass
#creates URL for csv files from year 2010 to 2016
def createURL(year,state):
    yr = year
    yr = str(yr)
    ste = state
    filename = ste+yr[2:]+".txt"
    fname = ste+yr+".txt"
    name , extention = os.path.splitext(fname)
    csvName = name + '.txt'
    link ="https://www.fhwa.dot.gov/bridge/nbi/"+yr+"/delimited/"+filename
    return(link, csvName)

#creates URL for zip file downloads from year 1992 to 2009
def createZipUrl(year):
    year = str(year)
    return 'https://www.fhwa.dot.gov/bridge/nbi/'+year+'del.zip'

#uses zip url to download and extract csv files
def downloadZipfile(zipUrl):
    r = requests.get(zipUrl,stream = True)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('NBIDATA')
 
#driver function
def main():
    for year in years:
        if (year<2010):        
           zipUrl = createZipUrl(year)
           print('Downloading Zip file for ', year)
           downloadZipfile(zipUrl)
        else:
           log = open("log.txt",'w')
           for state in states:
               y = year
               s = state
               url , filename = createURL(y,s)
               print("getting ...", filename)
               f = open(os.path.join('NBIDATA',filename),'w')
               with urlopen(url) as response:
                   for line in response:
                       try:
                          line = line.decode('utf-8')
                       except UnicodeDecodeError:
                           print("Unicode error in", filename, file=log)
                           print(line,file = log)
                           continue
                       f.write(line)
               f.close()
           log.close()
    rename(fileNameDict)   
#main function
if __name__ == "__main__":
    main()
