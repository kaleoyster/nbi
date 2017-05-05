'''
Program Title: NBI BRIDGE JSON ENCODER
VERSION: 1
TEMPLATE: IA16

Author: Akshay Kale
'''

import requests
import csv
import json
import pprint

years = [2010]
dEliminater = ','
## years: 1992,1993,1994,1995,1996
## runs for YEAR 2010 - 2016

 
    # with open(filename,'w') as fp:
    #fp.write(r.text)

def nbi_encoder(data,year):
    x = json.dumps({
   "year" : year,
   "State Code":row[0],                                                                                            #item No:1   3  /  N
   "Structure Number":row[1],                                                                                      #item No:8  15  / AN
   "Inventory Route": {                                                                                            #item No:5   9  / AN
                        "Record Type":row[2],                                                                      #item No:5A  1  / AN
                        "Route Signing Prefix":row[3],                                                             #item No:5B  1  /  N
                        "Designated Level of Service":row[4],                                                      #item No:5C  1  /  N
                        "Route Number":row[5],                                                                     #item No:5D  5  / AN
                        "Directional Suffix":row[6]                                                                #item No:5E  1  /  N
                     }, 

   "Highway Agency District":row[7],                                                                               #item No:2   2  / AN
   "County (Parish) Code":row[8],                                                                                  #item No:3   3  /  N
   "Place Code":row[9],                                                                                            #item No:4   4  /  N
   "Features Intersected": {                                                                                       #item No:6  25  / AN
                             "Features Instersected":row[10],                                                      #item No:6A 25  / AN
                             "Critical Facility Indicator":row[11]                                                 #item No:6B  1  / AN  
                            },                                                       
                                                                                     
   "Facility Carried By Structure":row[12],                                                                        #item No:7  
   "Location":row[13],                                                                                             #item No:8  
   "Inventory RTe, Min Vert Clearance":row[14],                                                                    #item No:9
                                                                                   
   "Kilometerpoint":row[15],                                                                                       #item No:10      
   "Base Highway Point":row[16],                                                                                   #item No:11
   "Inventory Route, Subroute Number": {                                                                           #item No:12
                                         "LRS Inventory Route":row[17],                                            #item No:13A
                                         "Subroute Number":row[18]                                                 #item No:13B 
                                        },                                              
   "Latitude":row[19],                                                                                             #item No:16
   "Longitude":row[20],                                                                                            #item No:17  
   "Bypass/Detour Length":row[21],                                                                                 #item No:19
   "Toll":row[22],                                                                                                 #item No:20  
   "Maintenance Reponsibility":row[23],                                                                            #item No:21  
   "Owner":row[24],                                                                                                #item No:22
   "Functional Class Of Inventory Rte.": row[25],                                                                  #item No:26
   "Year Built":row[26],                                                                                           #item No:27
   "Lanes On/Under Structure": {                                                                                   #item No:28  
                                  "Lanes On Structure":row[27],                                                    #item No:28A  
                                  "Lanes Under Structure":row[28]                                                  #item No:28B
                                },  
   "Average Daily Traffic":row[29],                                                                                #item No:29                                                    
   "Year Of Average Daily Traffic":row[30],                                                                        #item No:30
   "Design Load":row[31],                                                                                          #item No:31   
   "Approach Roadway Width":row[32],                                                                               #item No:32
   "Bridge Median":row[33],                                                                                        #item No:33 
   "Skew":row[34],                                                                                                 #item No:34
   "Structure Flared":row[35],                                                                                     #item No:35 
   "Traffic safety Features": {                                                                                    #item No:36 
                                "Bridge Railings":row[36],                                                         #item No:36A 
                                "Transitions":row[37],                                                             #item No:36B
                                "Approach Guardrail":row[38],                                                      #item No:36C
                                "Approach Guardrail Ends":row[39]                                                  #item No:36D  
                               },

   "Historical significance":row[40],                                                                              #item No:37 
   "Navigation Control":row[41],                                                                                   #item No:38 
   "Navigation Veritical Clearance":row[42],                                                                       #item No:39
   "Navigation Horizontal Clearance":row[43],                                                                      #item No:40
   "Strucutre Open/Posted/Closed":row[44],                                                                         #item No:41 
   "Type of Service":{                                                                                             #item No:42 
                       "Type of Service On Bridge":row[45],                                                        #item No:42A
                       "Type of Service Under Bridge":row[46]                                                      #item No:42B  
                     },
 
   "Structure Type, Main":{                                                                                       #item No:43
                          "Kind of Material/Design":row[47],                                                      #item No:43A     
                          "Type of Design/Construction":row[48]                                                   #item No:43B
                          },
   "Structure Type, Approach Spans":{                                                                             #item No:44
                                     "Kind of Material/Design":row[49],                                           #item No:44A
                                     "Type of Design/Contruction":row[50],                                        #item No:44B
                                     },                                           
                    
   "Number of Spans in Main unit":row[51],                                                                        #item No:45
   "Number of Approach Spans":row[52],                                                                            #item No:46 
   "Inventory Rte Total Horz Clearance":row[53],                                                                  #item No:47 
   "Length Of Maximum Span":row[54],                                                                              #item No:48
   "Structure Length":row[55],                                                                                    #item No:49
   "Curb/Sidewalk Width": {                                                                                       #item No:50
                            "Left Curb/Sidewalk Width":row[56],                                                   #item No:50A 
                            "Right Curb/Sidewalk Width":row[57]                                                   #item No:50B
                           },
 
   "Bridge Roadway with Curb-To-Curb":row[58],                                                                    #item No:51
   "Deck Width, Out-To-Out":row[59],                                                                              #item No:52 
   "Min Vert Clear Over Bridge Roadway":row[60],                                                                  #item No:53
   "Minimum Veritical Underclearance": {                                                                          #item No:54  
                                         "Reference Feature":row[61],                                             #item No:54A
                                         "Minimum Veritical Underclearance":row[62]                               #item No:54B
                                       },    
   "Min Lateral underclear On Right":{                                                                            #item No:55
                                       "Reference Feature":row[63],                                               #item No:55A
                                       "Minimum Lateral Underclearance":row[64],                                  #item No:55B
                                     },
   
   "Min Lateral Underclear On Left":row[65],                                                                      #item No:56  
   "Deck":row[66],                                                                                                #item No:58
   "Superstructure":row[67],                                                                                      #item No:59
   "Substructure":row[68],                                                                                        #item No:60
   "Channel/Channel Protection":row[69],                                                                          #item No:61
   "Culverts":row[70],                                                                                            #item No:62
   "Method Used to Determine Operating Rating":row[71],                                                           #item No:63
   "Operating Rating":row[72],                                                                                    #item No:64
   "Method Used To Determine Inventory Rating":row[73],                                                           #item No:65
   "Inventory Rating":row[74],                                                                                    #item No:66
   "Structural Evaluation":row[75],                                                                               #item No:67
   "Deck Geometry":row[76],                                                                                       #item No:68
   "Underclear, Vertical & Horizontal":row[77],                                                                   #item No:69
   "Bridge Posting":row[78],                                                                                      #item No:70
   "Waterway Adequacy":row[79],                                                                                   #item No:71
   "Approach Roadway Alignment":row[80],                                                                          #item No:72
                                        
   "Type of Work": {                                                                                              #item No:75
                      "Type of Work Proposed":row[81],                                                            #item No:75A
                      "Work Done By":row[82]                                                                      #item No:75B
                   },  
 
   "Length Of Structure Improvement":row[83],                                                                     #item No:76
   "Inspection Date":row[84],                                                                                     #item No:90
   "Designated Inspection Frequency":row[85],                                                                     #item No:91
   "Critical Feature Inspection": {                                                                               #item No:92
                                    "Fracture Critical Details":row[86],                                          #item No:92A
                                    "Underwater Inspection":row[87],                                              #item No:92B
                                    "Other Special Inspection":row[88]                                            #item No:92C
                                  },
   "Critical Feature Inspection Dates": {                                                                         #item No:93
                                          "Fracture Ciritcal Details Date":row[89],                               #item No:93A
                                          "Underwater Inspection Date":row[90],                                   #item No:93B
                                          "Other Special Inspection Date":row[91]                                 #item No:93C
                                        }, 
   "Bridge Improvement Cost":row[92],                                                                             #item No:94
   "Roadway Improvement Cost":row[93],                                                                            #item No:95
   "Total Project Cost":row[94],                                                                                  #item No:96
   "Year Of Improvement Cost":row[95],                                                                            #item No:97
   "Border Bridge": {                                                                                             #item No:98
                       "Neighboring State Code":row[96],                                                          #item No:98A
                       "Percent Reponsibility":row[97]                                                            #item No:98B
                    }, 
   "Border Bridge Structure Number":row[98],                                                                      #item No:99 
   "STRAHNET Highway Designation":row[99],                                                                        #item No:100    
   "Parallel Structure Designation":row[100],                                                                     #item No:101    
   "Direction Of Traffic":row[101],                                                                               #item No:102                             
   "Temporary Structure Designation":row[102],                                                                    #item No:103 
   "Highway System of Inventory Route":row[103],                                                                  #item No:104
   "Federal Lands Highways":row[104],                                                                             #item No:105 
   "Year Reconstructed":row[105],                                                                                 #item No:106
   "Deck Strucuture Type":row[106],                                                                               #item No:107  
   "Wearing Surface/Protective System": {                                                                         #item No:108 
                                           "Type of Wearing Surface":row[107],                                    #item No:108A
                                           "Type of Membrane":row[108],                                           #item No:108B
                                           "Deck Protection":row[109]                                             #item No:108C
                                         },
   "AVERAGE DAILY TRUCK TRAFFIC":row[110],                                                                        #item No:109    
   "DESIGNATED NATIONAL NETWORK":row[111],                                                                        #item No:110   
   "PIER/ABUTMENT PROTECTION":row[112],                                                                           #item No:111 
   "NBIS BRIDGE LENGTH":row[113],                                                                                 #item No:112                          
   "SCOUR CRITICAL BRIDGES":row[114],                                                                             #item No:113
   "FUTURE AVERAGE DAILY TRAFFIC":row[115],                                                                       #item No:114
   "YEAR OF FUTURE AVG DAILY TRAFFIC":row[116],                                                                   #item No:115 
   "MINIMUM NAVIGATION VERTICAL CLEARANCE VERTICAL LIFT BRIDGE":row[117],                                         #item No:116  
   "FEDERAL AGENCY INDICATOR":row[118]
             })
    return x

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
   Function to create URL to crawl on websites
   Input: Year
   Output: will return created link
'''
def createURL(year):
    yr = year
    yr = str(yr)
    filename = "NE"+yr[2:]+".txt"
    link ="https://www.fhwa.dot.gov/bridge/nbi/"+yr+"/delimited/"+filename
    return(link)

'''
         
'''
with requests.Session() as s:
     for i in years:
         csv_url = createURL(i)
         download = s.get(csv_url)
         decode_content = download.content.decode('utf-8')
         cr = csv.reader(decode_content.splitlines(),delimiter = ',')
         my_list = list(cr)
         for row in my_list:
             print("======================================================= Line Break ===================================================")
             temp = []
             for r in row:
                 r = r.strip("'")
                 r = r.strip(" ")
                 temp.append(r)
                 #print(temp)
                 x = nbi_encoder(temp,i)
                 print(str(x))
 
             
'''
with open("Sample1.csv",'r') as r:
     reader = csv.reader(r)
     next(reader) #skips header
     for row in reader: 
         print("============================================================== Line break===================================================")
         temp = []
         for r in row:
            r = r.strip("'")
            r = r.strip(" ")
            temp.append(r)
         #print(temp)
            x = nbi_encoder(temp)
            print(str(x))
'''
       



#for i in years:
#    url = createURL(i)
#   r = requests.get(url)
   #year = str(i)
   #filename = "NE"+year+".csv"
#    rfile = r.text  
#   for row in rfile:
#      print(row)
     
     
#   return D
 

