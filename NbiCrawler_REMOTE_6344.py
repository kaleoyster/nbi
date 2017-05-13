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
from io import BytesIO
from zipfile import ZipFile
import urllib.request
import io

encoding = 'utf-8'
years = [1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016] #Global variable
States =["AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","HI","IA","ID","IL","IN","KS","KY","MA",'MD',"ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VA","VT","WA","WI","WV","WY"]
#global array States
dEliminater = ',' #Global variable delimeter

'''
   FUNCTION NAME: def nbi_encoder()
   The purpose of this function to return a JSON formattd strings from a CSV file.

   INPUT PARAMETER: input parameters for this function are 1. data is a list of rows containing NBI data.
                                                           2. year integer is an integer.
                                                           3. Longitude is an intger.
                                                           4. Latitude is an integer.

   OUTPUT: The function returns a JSON formatred string using the schema described in json.dumps() function.
'''

def nbi_encoder(data,year,Longitude,Latitude):
    x = json.dumps({
   "year" : year,                                                                                              #item No:0  YEAR
   "stateCode":row[0],                                                                                         #item No:1   3  /  N  State Code
   "structureNumber":row[1],                                                                                   #item No:8  15  / AN  Structure Number
   "inventoryRoute": {                                                                                         #item No:5   9  / AN  Inventory Route
                        "recordType":row[2],                                                                   #item No:5A  1  / AN  Record Type
                        "routeSigningPrefix":row[3],                                                           #item No:5B  1  /  N  Route Signing Prefix
                        "designatedLevelOfService":row[4],                                                     #item No:5C  1  /  N  Designated Level of Service
                        "routeNumber":row[5],                                                                  #item No:5D  5  / AN  Route Number
                        "directionalSuffix":row[6]                                                             #item No:5E  1  /  N  Directional Suffi
                     },
   "highwayAgencyDistrict":row[7],                                                                             #item No:2   2  / AN  Highway Agency District
   "countyCode":row[8],                                                                                        #item No:3   3  /  N  Count (Parish) Code
   "placeCode":row[9],                                                                                         #item No:4   4  /  N  Place Code
   "featuresIntersected": {                                                                                    #item No:6  25  / AN  Features Intersected
                             "featuresInstersected":row[10],                                                   #item No:6A 25  / AN  Features Instersected
                             "criticalFacilityIndicator":row[11]                                               #item No:6B  1  / AN  Critical Facility Indicator
                            },
   "facilityCarriedByStructure":row[12],                                                                       #item No:7   Facility Carried By Structure
   "location":row[13],                                                                                         #item No:9   Location
   "InventoryRTeMinVertClearance":row[14],                                                                     #item No:10  Inventory RTe, Min Vert Clearance

   "kilometerpoint":row[15],                                                                                   #item No:11  Kilometerpoint
   "baseHighwayPoint":row[16],                                                                                 #item No:12  Base Highway Point
   "inventoryRouteSubrouteNumber": {                                                                           #item No:13  Inventory Route, Subroute Number
                                         "LRSInventoryRoute":row[17],                                          #item No:13A LRS Inventory Route
                                         "subrouteNumber":row[18]                                              #item No:13B Subroute Number
                                        },
   "latitude":row[19],                                                                                         #item No:16  Latitude
   "longitude":row[20],                                                                                        #item No:17  Longitude
   "bypassDetourLength":row[21],                                                                               #item No:19  Bypass/Detour Length
   "toll":row[22],                                                                                             #item No:20  Toll
   "maintenanceReponsibility":row[23],                                                                         #item No:21  Maintenance Reponsibility
   "owner":row[24],                                                                                            #item No:22  Owner
   "functionalClassOfInventoryRte": row[25],                                                                   #item No:26  Functional Class Of Inventory Rte.
   "yearBuilt":row[26],                                                                                        #item No:27  Year Built
   "lanesOnUnderStructure": {                                                                                  #item No:28  Lanes On/Under Structure
                                  "lanesOnStructure":row[27],                                                  #item No:28A Lanes On Structure
                                  "lanesUnderStructure":row[28]                                                #item No:28B Lanes Under Structure
                                },
   "averageDailyTraffic":row[29],                                                                              #item No:29   Average Daily Traffic

   "yearOfAverageDailyTraffic":row[30],                                                                        #item No:30   Year Of Average Daily Traffic
   "designLoad":row[31],                                                                                       #item No:31   Design Load
   "approachRoadwayWidth":row[32],                                                                             #item No:32   Approach Roadway Width
   "bridgeMedian":row[33],                                                                                     #item No:33   Bridge Median
   "skew":row[34],                                                                                             #item No:34   Skew
   "structureFlared":row[35],                                                                                  #item No:35   Structure Flared
   "trafficSafetyFeatures": {                                                                                  #item No:36   Traffic safety Features
                                "bridgeRailings":row[36],                                                      #item No:36A  Bridge Railings
                                "transitions":row[37],                                                         #item No:36B  Transitions
                                "approachGuardrail":row[38],                                                   #item No:36C  Approach Guardrail
                                "approachGuardrailEnds":row[39]                                                #item No:36D  Approach Guardrail Ends
                               },

   "historicalSignificance":row[40],                                                                           #item No:37  Historical significance
   "navigationControl":row[41],                                                                                #item No:38  Navigation Control
   "navigationVeriticalClearance":row[42],                                                                     #item No:39  Navigation Veritical Clearance
   "navigationHorizontalClearance":row[43],                                                                    #item No:40  Navigation Horizontal Clearance
   "strucutreOpenPostedClosed":row[44],                                                                        #item No:41  Strucutre Open/Posted/Closed
   "typeOfService":{                                                                                           #item No:42  Type of Service
                       "typeOfServiceOnBridge":row[45],                                                        #item No:42A Type of Service On Bridge"
                       "typeOfServiceUnderBridge":row[46]                                                      #item No:42B Type of Service Under Bridge
                     },

   "structureTypeMain":{                                                                                       #item No:43  Structure Type, Main
                          "kindOfMaterialDesign":row[47],                                                      #item No:43A Kind of Material/Design
                          "typeOfDesignConstruction":row[48]                                                   #item No:43B Type of Design/Construction
                          },
   "structureTypeApproachSpans":{                                                                              #item No:44  Structure Type, Approach Spans
                                     "kindOMaterialDesign":row[49],                                            #item No:44A Kind of Material/Design
                                     "typeOfDesignContruction":row[50],                                        #item No:44B Type of Design/Contruction
                                     },

   "numberOfSpansInMainUnit":row[51],                                                                          #item No:45  Number of Spans in Main unit
   "numberOfApproachSpans":row[52],                                                                            #item No:46  Number of Approach Spans
   "InventoryRteTotalHorzClearance":row[53],                                                                   #item No:47  Inventory Rte Total Horz Clearance
   "lengthOfMaximumSpan":row[54],                                                                              #item No:48  Length Of Maximum Span
   "structureLength":row[55],                                                                                  #item No:49  Structure Length
   "curbSidewalk Width": {                                                                                     #item No:50  Curb/Sidewalk Width
                            "leftCurbSidewalkWidth":row[56],                                                   #item No:50A Left Curb/Sidewalk Width
                            "rightCurbSidewalkWidth":row[57]                                                   #item No:50B Right Curb/Sidewalk Width
                           },

   "bridgeRoadwayWithCurbToCurb":row[58],                                                                      #item No:51  Bridge Roadway with Curb-To-Curb
   "deckWidthOutToOut":row[59],                                                                                #item No:52  Deck Width, Out-To-Out
   "minVertClearOverBridgeRoadway":row[60],                                                                    #item No:53  Min Vert Clear Over Bridge Roadway
   "minimumVeriticalUnderclearance": {                                                                         #item No:54  Minimum Veritical Underclearance
                                        "referenceFeature":row[61],                                            #item No:54A Reference Feature
                                        "minimumVeriticalUnderclearance":row[62]                               #item No:54B Minimum Veritical Underclearance
                                       },
   "minLateralUderclearOnRight":{                                                                               #item No:55  Min Lateral underclear On Right
                                       "referenceFeature":row[63],                                             #item No:55A Reference Feature
                                       "minimumLateralUnderclearance":row[64],                                 #item No:55B Minimum Lateral Underclearance
                                     },

   "minLateralUnderclearOnLeft":row[65],                                                                       #item No:56 Min Lateral Underclear On Left
   "deck":row[66],                                                                                             #item No:58 Deck
   "superstructure":row[67],                                                                                   #item No:59 Superstructure
   "substructure":row[68],                                                                                     #item No:60 Substructure
   "channelChannelProtection":row[69],                                                                         #item No:61 Channel/Channel Protection
   "culverts":row[70],                                                                                         #item No:62 culverts
   "methodUsedToDetermineOperatingRating":row[71],                                                             #item No:63 Method Used to Determine Operating Rating
   "operatingRating":row[72],                                                                                  #item No:64 Operating Rating
   "methodUsedToDetermineInventoryRating":row[73],                                                             #item No:65 Method Used To Determine Inventory Rating
   "inventoryRating":row[74],                                                                                  #item No:66 Inventory Rating
   "structuralEvaluation":row[75],                                                                             #item No:67 Structural Evaluation
   "deckGeometry":row[76],                                                                                     #item No:68 Deck Geometry
   "underclearVerticalHorizontal":row[77],                                                                     #item No:69 Underclear, Vertical & Horizontal
   "bridgePosting":row[78],                                                                                    #item No:70 Bridge Posting
   "waterwayAdequacy":row[79],                                                                                 #item No:71 Waterway Adequacy
   "approachRoadwayAlignment":row[80],                                                                         #item No:72 Approach Roadway Alignment

   "typeOfWork": {                                                                                             #item No:75  Type of Work
                      "typeOfWorkProposed":row[81],                                                            #item No:75A Type of Work Proposed
                      "WorkDoneBy":row[82]                                                                     #item No:75B Work Done By
                   },

   "lengthOfStructureImprovement":row[83],                                                                     #item No:76  Length Of Structure Improvement
   "inspectionDate":row[84],                                                                                   #item No:90  Inspection Date
   "designatedInspectionFrequency":row[85],                                                                    #item No:91  Designated Inspection Frequency
   "criticalFeatureInspection": {                                                                              #item No:92  Critical Feature Inspection
                                    "fractureCriticalDetails":row[86],                                         #item No:92A Fracture Critical Details
                                    "underwaterInspection":row[87],                                            #item No:92B Underwater Inspection
                                    "otherSpecialInspection":row[88]                                           #item No:92C Other Special Inspection
                                  },
   "criticalFeatureInspectionDates": {                                                                         #item No:93   Critical Feature Inspection Dates
                                          "fractureCiritcalDetailsDate":row[89],                               #item No:93A  Fracture Ciritcal Details Date
                                          "underwaterInspectionDate":row[90],                                  #item No:93B  Underwater Inspection Date
                                          "OtherSpecialInspectionDate":row[91]                                 #item No:93C  Other Special Inspection Date
                                        },
   "bridgeImprovementCost":row[92],                                                                            #item No:94   Bridge Improvement Cost
   "roadwayImprovementCost":row[93],                                                                           #item No:95   Roadway Improvement Cost
   "totalProjectCost":row[94],                                                                                 #item No:96   Total Project Cost
   "yearOfImprovementCost":row[95],                                                                            #item No:97   Year Of Improvement Cost
   "borderBridge": {                                                                                           #item No:98   Border Bridge
                       "neighboringStateCode":row[96],                                                         #item No:98A  Neighboring State Code
                       "percentReponsibility":row[97]                                                          #item No:98B  Percent Reponsibility
                    },
   "borderBridgeStructureNumber":row[98],                                                                      #item No:99   Border Bridge Structure Number
   "STRAHNETHighwayDesignation":row[99],                                                                       #item No:100  STRAHNETHighwayDesignation
   "parallelStructureDesignation":row[100],                                                                    #item No:101  Parallel Structure Designation
   "directionOfTraffic":row[101],                                                                              #item No:102  Direction Of Traffic
   "temporaryStructureDesignation":row[102],                                                                   #item No:103  Federal Lands Highways
   "highwaySystemOfInventoryRoute":row[103],                                                                   #item No:104  Temporary Structure Designation
   "federalLandsHighways":row[104],                                                                            #item No:105  Highway System of Inventory Route
   "yearReconstructed":row[105],                                                                               #item No:106  Year Reconstructed
   "deckStructureType":row[106],                                                                               #item No:107  Deck Strucuture Type
   "wearingSurface/ProtectiveSystem": {                                                                        #item No:108  Wearing Surface/Protective System
                                           "typeOfWearingSurface":row[107],                                    #item No:108A Type of Wearing Surface
                                           "typeOfMembrane" :row[108],                                         #item No:108B Type of Membrane
                                           "deckProtection" :row[109]                                          #item No:108C Deck Protection
                                         },
   "avgDailyTruckTraffic":row[110],                                                                            #item No:109  AVERAGE DAILY TRUCK TRAFFIC
   "designatedNationalNetwork":row[111],                                                                       #item No:110  DESIGNATED NATIONAL NETWORK
   "pier/abutmentProtection":row[112],                                                                         #item No:111  PIER/ABUTMENT PROTECTION
   "nbisBridgeLength":row[113],                                                                                #item No:112  NBI BRIDGE LENGTH
   "scourCriticalBridges":row[114],                                                                            #item No:113  SCOUR CRITICAL BRIDGE
   "futureAvgDailyTraffic":row[115],                                                                           #item No:114  FUTURE AVERAGE DAILY TRAFFIC
   "yearOfFutureAvgDailyTraffic":row[116],                                                                     #item No:115  YEAR OF FUTURE AAVG DAILY TRAFFIC
   "minimumNavigationVerticalClearanceVerricalLiftBridge":row[117],                                            #item No:116  MINIMUM NAVIGATION VERTICAL CLEARANCE VERTICAL LIFT BRIDGE
   "federalAgencyIndicator":row[118],                                                                          #item No:117  FEDERAL AGENCY INDICATOR
   "loc":{
           "type": "Point",
           "coordinates":[
                          Longitude,
                          Latitude
                          ]
           }
             })
    return x

'''
   FUNCTION NAME: def handle_string
   The purpose of this function to sanitize strings of extra white spaces and converts strings
   into integer or float depending on the structure of the string. create URL to crawl on websites

   INPUT PARAMETER: input parameter 's' is a string.

   OUTPUT: the returning value could be either a string, float or int.

'''

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
   FUNCTION NAME: def createURL()
   The purpose of this function to create a link depending on the input year.
   INPUT PARAMETER: input parameters for this function is 'year' (integer).

   OUTPUT: The function returns a custom link for every year and state.
'''
def createURL(year,state):
    if (year < 2010):
        yr = year
        yr = str(yr)
        link = "https://www.fhwa.dot.gov/bridge/nbi/"+yr+"del.zip"
        return(link)
    else:
        yr = year
        yr = str(yr)
        ste = state
        filename = ste+yr[2:]+".txt"
        link ="https://www.fhwa.dot.gov/bridge/nbi/"+yr+"/delimited/"+filename
        return(link)

'''
   FUNCTION NAME: def convertLongLat()
   The purpose of this function to convert DMS format longitude and latitude strings to decimal degrees. This function helps with creating geoJSON formatted locations for every bridge record in the NBI Dataset.

   INPUT PARAMETER: input parameters for this function are 1. Longitude is an integer.
                                                           2. Latitude is an integer.

   OUTPUT: The function returns a pair of integer coordinates, longitude and latitude.
'''


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

'''
FUNCTION NAME: def find_all()

PURPOSE: __TODO__

INPUT PARAMETER: __TODO__

OUTPUT: __TODO__
'''

def find_all(name):
    if(name[:2] == '31'):
        return name

'''
FUNCTION NAME:  driverProgram

'''

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
                    fname = find_all(name)
                    with zfile.open(name) as readfile:
                        readfile = io.TextIOWrapper(readfile,encoding,errors='ignore')
                        cr = csv.reader(readfile,delimiter = ',')
                        next(cr,None)
                        my_list = list(cr)
                        for row in my_list:
                        #print("======================================================= Line Break ===================================================")
                           temp = []
                           for r in row:
                                r = r.strip("'")
                                r = r.strip(" ")
                                temp.append(r)
                           try:
                               Longitude, Latitude = convertLongLat(temp[20],temp[19])
                               x = nbi_encoder(temp,year,Longitude,Latitude)
                               f.write(x+'\n')
                           except:
                               print("Skipping Record")

                    print("[ + ] " + name + " CSV file DONE..")
           print("[ + ]"+ csv_url + " Zip file DONE...")

        if(year > 2009):
           for state in States:
               csv_url = createURL(year,state)
               print("CRAWLING..: " + csv_url)
               download = s.get(csv_url)
               print("Downloading...")
               #decode_content = download.content.decode('utf-8')
               decode_content = download.text
               cr = csv.reader(decode_content.splitlines(),delimiter = ',')
               next(cr,None)
               my_list = list(cr)

               for row in my_list:
                #print("======================================================= Line Break ===================================================")
                   temp = []
                   for r in row:
                       r = r.strip("'")
                       r = r.strip(" ")
                       temp.append(r)
                   try:
                       Longitude, Latitude = convertLongLat(temp[20],temp[19])
                       x = nbi_encoder(temp,year,Longitude,Latitude)
                       f.write(x+'\n')
                   except:
                       print("Skipping Record")
           print("[ + ] " + csv_url+ " DONE..")
    f.close()
