'''
Program Title: NBI BRIDGE JSON ENCODER
VERSION: 2



Author: Akshay Kale
'''
import json
import csv
import pprint

#missing : 14,15,18,23,24,25,57,73,74,77-89
#Data

dEliminater = ','

SampleFileName = input('Enter NBI filename: ') or 'Sample.csv' #Ask for filename or choose default
#Function either uses handleString or convertToString  
def nbiEncoder(data):
    x = json.dumps({	
  
   #"year" : year,                                                                                                            #item No:0  YEAR      
   "stateCode":handleString(data[0]),                                                                                         #item No:1   3  /  N  State Code
   "structureNumber":convertToString(data[1]),                                                                                #item No:8  15  / AN  Structure Number
   "inventoryRoute": {                                                                                                        #item No:5   9  / AN  Inventory Route
                        "recordType":convertToString(data[2]),                                                                #item No:5A  1  / AN  Record Type
                        "routeSigningPrefix":handleString(data[3]),                                                           #item No:5B  1  /  N  Route Signing Prefix
                        "designatedLevelOfService":handleString(data[4]),                                                     #item No:5C  1  /  N  Designated Level of Service
                        "routeNumber":convertToString(data[5]),                                                               #item No:5D  AN  / 5  Route Number
                        "directionalSuffix":handleString(data[6])                                                             #item No:5E  1  /  N  Directional Suffi
                     }, 
   "highwayAgencyDistrict":convertToString(data[7]),                                                                          #item No:2   2  / AN  Highway Agency District
   "countyCode":handleString(data[8]),                                                                                        #item No:3   3  /  N  Count (Parish) Code
   "placeCode":handleString(data[9]),                                                                                         #item No:4   4  /  N  Place Code
   "featuresIntersected": {                                                                                                   #item No:6  25  / AN  Features Intersected
                             "featuresIntersected":convertToString(data[10]),                                                 #item No:6A 25  / AN  Features Intersected (NO LONGER CODE .. Has to be BLANK)
                             "criticalFacilityIndicator":convertToString(data[11])                                            #item No:6B  1  / AN  Critical Facility Indicator
                            },                                                                                                                                        
   "facilityCarriedByStructure":convertToString(data[12]),                                                                    #item No:7  AN Facility Carried By Structure
   "location":convertToString(data[13]),                                                                                      #item No:9  AN Location
   "InventoryRTeMinVertClearance": handleString(data[14]),                                                                    #item No:10 N Inventory RTe, Min Vert Clearance
                                                                                   
   "kilometerpoint":handleString(data[15]),                                                                                   #item No:11 N Kilometerpoint
   "baseHighwayPoint":handleString(data[16]),                                                                                 #item No:12 N Base Highway Point
   "inventoryRouteSubrouteNumber": {                                                                                          #item No:13  AN Inventory Route, Subroute Number
                                         "LRSInventoryRoute":convertToString(data[17]),                                       #item No:13A AN LRS Inventory Route
                                         "subrouteNumber":handleString(data[18])                                              #item No:13B N Subroute Number (Should be string)
                                        },                                              
   "latitude":handleString(data[19]),                                                                                         #item No:16 N Latitude
   "longitude":handleString(data[20]),                                                                                        #item No:17 N Longitude
   "bypassDetourLength":handleString(data[21]),                                                                               #item No:19 N Bypass/Detour Length (should be string)
   "toll":handleString(data[22]),                                                                                             #item No:20 N Toll 
   "maintenanceReponsibility":handleString(data[23]),                                                                         #item No:21 N Maintenance Reponsibility(Not Available, values not in bounds of acceptable bounds)
   "owner":handleString(data[24]),                                                                                            #item No:22 N Owner (Not Available, values not in bounds of acceptable bounds)
   "functionalClassOfInventoryRte": handleString(data[25]),                                                                   #item No:26 N Functional Class Of Inventory Rte.
   "yearBuilt":handleString(data[26]),                                                                                        #item No:27 N Year Built
   "lanesOnUnderStructure": {                                                                                                 #item No:28 N Lanes On/Under Structure
                                  "lanesOnStructure":handleString(data[27]),                                                  #item No:28A N Lanes On Structure (Doubt )
                                  "lanesUnderStructure":handleString(data[28])                                                #item No:28B N Lanes Under Structure (Doubt )
                                },  
   "averageDailyTraffic":handleString(data[29]),                                                                              #item No:29  N Average Daily Traffic
                                                
   "yearOfAverageDailyTraffic":handleString(data[30]),                                                                        #item No:30  N Year Of Average Daily Traffic
   "designLoad":handleString(data[31]),                                                                                       #item No:31  N Design Load
   "approachRoadwayWidth":handleString(data[32]),                                                                             #item No:32  N Approach Roadway Width
   "bridgeMedian":handleString(data[33]),                                                                                     #item No:33  N Bridge Median
   "skew":handleString(data[34]),                                                                                             #item No:34  N Skew (Need Conversion, but can work without it)
   "structureFlared":handleString(data[35]),                                                                                  #item No:35  N Structure Flared
   "trafficSafetyFeatures": {                                                                                                 #item No:36  AN  Traffic safety Features
                                "bridgeRailings":convertToString(data[36]),                                                   #item No:36A AN Bridge Railings
                                "transitions":convertToString(data[37]),                                                      #item No:36B AN Transitions
                                "approachGuardrail":convertToString(data[38]),                                                #item No:36C AN Approach Guardrail
                                "approachGuardrailEnds":convertToString(data[39])                                             #item No:36D AN Approach Guardrail Ends
                               },

   "historicalSignificance":handleString(data[40]),                                                                           #item No:37  N Historical significance
   "navigationControl":convertToString(data[41]),                                                                             #item No:38  AN Navigation Control
   "navigationVeriticalClearance":handleString(data[42]),                                                                     #item No:39  N Navigation Veritical Clearance (Need Conversion)
   "navigationHorizontalClearance":handleString(data[43]),                                                                    #item No:40  N Navigation Horizontal Clearance (Need Conversion)
   "strucutreOpenPostedClosed":convertToString(data[44]),                                                                     #item No:41  AN Strucutre Open/Posted/Closed
   "typeOfService":{                                                                                                          #item No:42  N Type of Service
                       "typeOfServiceOnBridge":handleString(data[45]),                                                        #item No:42A N Type of Service On Bridge"
                       "typeOfServiceUnderBridge":handleString(data[46])                                                      #item No:42B N Type of Service Under Bridge
                     }, 
 
   "structureTypeMain":{                                                                                                      #item No:43  N Structure Type, Main
                          "kindOfMaterialDesign":handleString(data[47]),                                                      #item No:43A N Kind of Material/Design   
                          "typeOfDesignConstruction":handleString(data[48])                                                   #item No:43B N Type of Design/Construction
                          },
   "structureTypeApproachSpans":{                                                                                             #item No:44  N Structure Type, Approach Spans
                                     "kindOMaterialDesign":handleString(data[49]),                                            #item No:44A N Kind of Material/Design
                                     "typeOfDesignContruction":handleString(data[50]),                                        #item No:44B N Type of Design/Contruction
                                     },                                           
                    
   "numberOfSpansInMainUnit":handleString(data[51]),                                                                          #item No:45  N Number of Spans in Main unit
   "numberOfApproachSpans":handleString(data[52]),                                                                            #item No:46  N Number of Approach Spans
   "InventoryRteTotalHorzClearance":handleString(data[53]),                                                                   #item No:47  N Inventory Rte Total Horz Clearance
   "lengthOfMaximumSpan":handleString(data[54]),                                                                              #item No:48  N Length Of Maximum Span (Need comversiom)
   "structureLength":handleString(data[55]),                                                                                  #item No:49  N Structure Length
   "curbSidewalk Width": {                                                                                                    #item No:50  N Curb/Sidewalk Width
                            "leftCurbSidewalkWidth":handleString(data[56]),                                                   #item No:50A N Left Curb/Sidewalk Width
                            "rightCurbSidewalkWidth":handleString(data[57])                                                   #item No:50B N Right Curb/Sidewalk Width
                           },
 
   "bridgeRoadwayWithCurbToCurb":handleString(data[58]),                                                                      #item No:51  N Bridge Roadway with Curb-To-Curb
   "deckWidthOutToOut":handleString(data[59]),                                                                                #item No:52  N Deck Width, Out-To-Out
   "minVertClearOverBridgeRoadway":handleString(data[60]),                                                                    #item No:53  N Min Vert Clear Over Bridge Roadway
   "minimumVeriticalUnderclearance": {                                                                                        #item No:54  AN Minimum Veritical Underclearance
                                        "referenceFeature":convertToString(data[61]),                                         #item No:54A AN Reference Feature
                                        "minimumVeriticalUnderclearance":handleString(data[62])                               #item No:54B N Minimum Veritical Underclearance
                                       },     
   "minLateralUnderclearOnRight":{                                                                                            #item No:55 AN Min Lateral underclear On Right
                                       "referenceFeature":convertToString(data[63]),                                          #item No:55A AN Reference Feature
                                       "minimumLateralUnderclearance":handleString(data[64]),                                 #item No:55B N Minimum Lateral Underclearance
                                     },
    
   "minLateralUnderclearOnLeft":handleString(data[65]),                                                                       #item No:56 N Min Lateral Underclear On Left
   "deck":convertToString(data[66]),                                                                                          #item No:58 AN Deck
   "superstructure":convertToString(data[67]),                                                                                #item No:59 AN Superstructure
   "substructure":convertToString(data[68]),                                                                                  #item No:60 AN Substructure
   "channelChannelProtection":convertToString(data[69]),                                                                      #item No:61 AN Channel/Channel Protection
   "culverts":convertToString(data[70]),                                                                                      #item No:62 AN culverts
   "methodUsedToDetermineOperatingRating":handleString(data[71]),                                                             #item No:63 N Method Used to Determine Operating Rating
   "operatingRating":handleString(data[72]),                                                                                  #item No:64 N Operating Rating
   "methodUsedToDetermineInventoryRating":handleString(data[73]),                                                             #item No:65 N Method Used To Determine Inventory Rating
   "inventoryRating":handleString(data[74]),                                                                                  #item No:66 N Inventory Rating
   "structuralEvaluation":convertToString(data[75]),                                                                          #item No:67 AN Structural Evaluation
   "deckGeometry":convertToString(data[76]),                                                                                  #item No:68 AN Deck Geometry
   "underclearVerticalHorizontal":data[77],                                                                                   #item No:69 AN Underclear, Vertical & Horizontal
   "bridgePosting":handleString(data[78]),                                                                                    #item No:70 N Bridge Posting
   "waterwayAdequacy":convertToString(data[79]),                                                                              #item No:71 AN Waterway Adequacy
   "approachRoadwayAlignment":convertToString(data[80]),                                                                      #item No:72 AN Approach Roadway Alignment
   "typeOfWork": {                                                                                                            #item No:75  N Type of Work
                      "typeOfWorkProposed":handleString(data[81]),                                                            #item No:75A N Type of Work Proposed
                      "WorkDoneBy":convertToString(data[82])                                                                  #item No:75B AN Work Done By
                   },  
   "lengthOfStructureImprovement":handleString(data[83]),                                                                     #item No:76  N Length Of Structure Improvement
   "inspectionDate":handleString(data[84]),                                                                                   #item No:90  N Inspection Date
   "designatedInspectionFrequency":handleString(data[85]),                                                                    #item No:91  N Designated Inspection Frequency
   "criticalFeatureInspection": {                                                                                             #item No:92  AN Critical Feature Inspection
                                    "fractureCriticalDetails":convertToString(data[86]),                                      #item No:92A AN Fracture Critical Details
                                    "underwaterInspection":convertToString(data[87]),                                         #item No:92B AN Underwater Inspection
                                    "otherSpecialInspection":convertToString(data[88])                                        #item No:92C AN Other Special Inspection
                                  },
   "criticalFeatureInspectionDates": {                                                                                        #item No:93  AN Critical Feature Inspection Dates
                                          "fractureCiritcalDetailsDate":convertToString(data[89]),                            #item No:93A AN Fracture Ciritcal Details Date
                                          "underwaterInspectionDate":convertToString(data[90]),                               #item No:93B AN Underwater Inspection Date
                                          "OtherSpecialInspectionDate":convertToString(data[91])                              #item No:93C AN Other Special Inspection Date
                                        }, 

   "bridgeImprovementCost":handleString(data[92]),                                                                            #item No:94  N Bridge Improvement Cost
   "roadwayImprovementCost":handleString(data[93]),                                                                           #item No:95  N Roadway Improvement Cost
   "totalProjectCost":handleString(data[94]),                                                                                 #item No:96  N Total Project Cost
   "yearOfImprovementCost":handleString(data[95]),                                                                            #item No:97 N  Year Of Improvement Cost
   "borderBridge": {                                                                                                          #item No:98   Border Bridge
                       "neighboringStateCode":convertToString(data[96]),                                                      #item No:98A AN Neighboring State Code
                       "percentReponsibility":handleString(data[97])                                                          #item No:98B N Percent Reponsibility
                    }, 
   "borderBridgeStructureNumber":handleString(data[98]),                                                                      #item No:99  N Border Bridge Structure Number
   "STRAHNETHighwayDesignation":convertToString(data[99]),                                                                    #item No:100  STRAHNETHighwayDesignation  
   "parallelStructureDesignation":convertToString(data[100]),                                                                 #item No:101  Parallel Structure Designation
   "directionOfTraffic":handleString(data[101]),                                                                              #item No:102  N Direction Of Traffic                    
   "temporaryStructureDesignation":convertToString(data[102]),                                                                #item No:103  Federal Lands Highways
   "highwaySystemOfInventoryRoute":handleString(data[103]),                                                                   #item No:104  N Temporary Structure Designation
   "federalLandsHighways":handleString(data[104]),                                                                            #item No:105  N Highway System of Inventory Route
   "yearReconstructed":handleString(data[105]),                                                                               #item No:106  N Year Reconstructed
   "deckStructureType":convertToString(data[106]),                                                                            #item No:107  AN  Deck Strucuture Type
   "wearingSurface/ProtectiveSystem": {                                                                                       #item No:108  AN Wearing Surface/Protective System
                                           "typeOfWearingSurface":convertToString(data[107]),                                 #item No:108A AN Type of Wearing Surface
                                           "typeOfMembrane" :convertToString(data[108]),                                      #item No:108B AN Type of Membrane
                                           "deckProtection" :convertToString(data[109])                                       #item No:108C AN Deck Protection
                                         },
   "avgDailyTruckTraffic":handleString(data[110]),                                                                            #item No:109 N AVERAGE DAILY TRUCK TRAFFIC
   "designatedNationalNetwork":handleString(data[111]),                                                                       #item No:110 N  DESIGNATED NATIONAL NETWORK  
   "pier/abutmentProtection":handleString(data[112]),                                                                         #item No:111 N PIER/ABUTMENT PROTECTION 
   "nbisBridgeLength":convertToString(data[113]),                                                                             #item No:112  NBI BRIDGE LENGTH                        
   "scourCriticalBridges":convertToString(data[114]),                                                                         #item No:113  SCOUR CRITICAL BRIDGE
   "futureAvgDailyTraffic":handleString(data[115]),                                                                           #item No:114  N FUTURE AVERAGE DAILY TRAFFIC
   "yearOfFutureAvgDailyTraffic":handleString(data[116]),                                                                     #item No:115  N YEAR OF FUTURE AAVG DAILY TRAFFIC
   "minimumNavigationVerticalClearanceVerricalLiftBridge":handleString(data[117]),                                            #item No:116  N MINIMUM NAVIGATION VERTICAL CLEARANCE VERTICAL LIFT BRIDGE
   "federalAgencyIndicator":convertToString(data[118]),                                                                       #item No:117  FEDERAL AGENCY INDICATOR            
   #"loc":{
   #        "type": "Point",
   #        "coordinates":[
   #                       Longitude,
   #                       Latitude
   #                       ] 
   # Programming guide: we wont be able tp consistent with guide 
   #         }  
             })
    return x



#Function to convert string into int
def handleString(s):
    try:
       res = convertToNumeric(s)
    except ValueError:
       print("Error: values is expected to be Numeric for ", s)
       res = s
    return res     
       
#Function to handle blank values by replacing it with "NA" 
def convertToString(s):
    if(s ==""):
       s = 'NA'
    else:
       pass
    return s

def convertToNumeric(s):
    if(s==""):
       s = -1
       result = s
    else:
       try:
         result = int(s)
       except ValueError:
         result = float(s)
    return result 

with open(SampleFileName, 'r') as f:
    reader = csv.reader(f, delimiter = dEliminater)
    next(reader,None) #skips header
    for row in reader:
       print("=" * 50 + 'Line break' + "=" * 50) #Enhance print
       temp = []
       for r in row:
           r = r.strip("'")
           r = r.strip(" ")
           temp.append(r)
       try:
          x = nbiEncoder(temp)
       #print(str(x))
       except IndexError as i:
          print("Error: " , i)
          pass

       

