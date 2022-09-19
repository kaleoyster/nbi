'''
Program: Download.py
Version: 1
Purpose: Downloads zip files and csvfiles from NBI and extracts them
'''

# Import libraries
import requests
import zipfile
import io
import os
from tqdm import tqdm
from urllib.request import urlopen

# Years
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
         2016,
         2017,
         2018,
         2019,
         2020,
         2021
        ]

# States 
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

# Dictionary - for rename function
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

def rename_old(fileNameDict):
    """
    Description:
        Renames all downloaded files by using the above dictionary

    Args:
        fileNameDict
    """
    for root, dirs, filenames in os.walk('NBIDATA'):
        for f in filenames:
            try:

               oldFileName, year = f[:7], f[10:14]
               if(oldFileName =='stfluna'):
                  os.remove(root + os.sep + f)

               else:
                  print('Renamed...', f)
                  os.rename(root+os.sep+f,root+os.sep+fileNameDict[oldFileName]+year+'.txt')

            except:
               pass

def rename(fileNameDict):
    """
    Description:
        Renames all downloaded files by using the above dictionary

    Args:
        fileNameDict
    """
    for root, dirs, filenames in os.walk('NBIDATA'):
        for filename in tqdm(filenames, desc='Renaming files'):
            year = filename[:-4][2:]
            if int(year) < 2010:
               state, year, extention = filename[:2], filename[2:4], filename[-4:]
               if year[0] == '0':
                   year = '20' + year
                   new_filename = state + year + extention
               else:
                   year = '19' + year
                   new_filename = state + year + extention
            else:
                new_filename = filename
            old_filename = root + os.sep + filename
            new_filename = root + os.sep + new_filename
            os.rename(old_filename, new_filename)

def createURL(year, state):
    """
    Description:
        Creates URL for csv files from year 2010 to currently available dataset

    Args:
        year: A list of years
        state: A list of states
    """
    yr = year
    yr = str(yr)
    ste = state
    filename = ste + yr[2:] + ".txt"
    fname = ste + yr + ".txt"
    name , extention = os.path.splitext(fname)
    csvName = name + '.txt'
    link ="https://www.fhwa.dot.gov/bridge/nbi/"+yr+"/delimited/"+filename
    return (link, csvName)

def createZipUrl(year):
    """
    Description:
        Creates URL for zip file downloads from year 1992 to 2009

    Args:
        year [String]: year of data that needs to be fetched.

    Note:
        With the new update. Perhaps this function may
        become dead code.
    """
    year = str(year)
    return 'https://www.fhwa.dot.gov/bridge/nbi/'+ year + 'del.zip'

def downloadZipfile(zipUrl):
    """
    Description:
        Uses zip url to download and extract csv files
    """
    r = requests.get(zipUrl,stream = True)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('NBIDATA')

def main():
    """
    Driver function
    Note:
        With the new update to the FHWA NBI data source
        the data can be downloaded without using CreateZipUrl.
        Which suggest that even the data before 2010 can be used
        through same (url) naming convention.
    """
    for year in years:
        if (year < 2010):
           zipUrl = createZipUrl(year)
           print('Downloading Zip file for ', year)
           downloadZipfile(zipUrl)
        else:
           log = open("log.txt",'w')
           for state in states:
               y = year
               s = state
               url, filename = createURL(y,s)
               print("getting ...", filename)
               f = open(os.path.join('NBIDATA', filename),'w', newline='')
               with urlopen(url) as response:
                   for line in response:
                       try:
                          line = line.decode('utf-8')
                       except UnicodeDecodeError:
                           print("Unicode error in", filename, file=log)
                           print(line, file = log)
                           continue
                       f.write(line)
               f.close()
           log.close()

    rename(fileNameDict)

# main function
if __name__ == "__main__":
    main()
