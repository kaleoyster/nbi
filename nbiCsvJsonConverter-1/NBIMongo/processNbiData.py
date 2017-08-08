'''
Program Title: NBI BRIDGE JSON ENCODER
VERSION: 1
TEMPLATE: IA16

Author: Akshay Kale
''' 	


import json
from nbiEncoder import nbiEncoder
'''
FUNCTION NAME: def processNbiRecord()

The purpose of this function is to return a JSON formatted strings from a CSV file.
   
INPUT PARAMETER: input parameters for this function are 1. my_list is an integer.
                                                        2. year is an integer.
                                                        3. RowCount
                                                        4. File
OUTPUT: The function returns count of Rows
'''          

def processNbiRecord(Datalist,Year,RowCount,myDb):  
    RowC = RowCount
    arr = []
    #f = File
    for row in Datalist:
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
           x = nbiEncoder(temp,Year,Longitude,Latitude)
           #print(type(x))
           myDb.mytable2.insert_one(json.loads(x))  
           #print(json.loads(x))
           #f.write(x+'\n')
           RowC = RowC + 1
        else:
            continue
    #         
    return RowC 


