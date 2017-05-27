'''
Program Title: NBI BRIDGE JSON ENCODER
VERSION: 1
TEMPLATE: IA16

Author: Akshay Kale
'''
from io import BytesIO
from zipfile import ZipFile
import urllib.request
import io
import csv


encoding = 'utf-8'	

'''
   FUNCTION NAME: def downloadCSV()
   The purpose of this function to download CSV file from given url, Session
   and create a List of Data 

   INPUT PARAMETER: input parameters for this function is 1. url is a string.
                                                          2. s (session) is a string.
                                                           
   OUTPUT: The function returns list of data in CSV file. 
'''
def downloadCSV(url,year,session):
    download = session.get(url)
    print("Downloading...")
   #decode_content = download.content.decode('utf-8')
    decode_content = download.text      
    cr = csv.reader(decode_content.splitlines(),delimiter = ',')
    next(cr,None)
    DataList = list(cr)
    return DataList





'''
FUNCTION NAME: def browseZip()

 The purpose of this function to open ZIP file from downloaded zip file, Session
   and browse each file in zip and convert them into list

   
INPUT PARAMETER: input parameters for this function are 1. name is a string.
                                                        2. zfile(ZipFile) is a string
                                                        3. s (session) is a string.

OUTPUT: The function returns a list of data contained in zipfile. 
'''

def browseZip(name,zfile,session):   
    with zfile.open(name) as readfile:
         readfile = io.TextIOWrapper(readfile,encoding,errors='ignore')
         cr = csv.reader(readfile,delimiter = ',')
         ### processing of the file
         next(cr,None)
         DataList = list(cr)
         return DataList
