import json



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
   
   "year" : year,                                                                                               #item No:0  YEAR      
   "stateCode":data[0],                                                                                         #item No:1   3  /  N  State Code
   "structureNumber":data[1],                                                                                   #item No:8  15  / AN  Structure Number
   "inventoryRoute": {                                                                                          #item No:5   9  / AN  Inventory Route
                        "recordType":data[2],                                                                   #item No:5A  1  / AN  Record Type
                        "routeSigningPrefix":data[3],                                                           #item No:5B  1  /  N  Route Signing Prefix
                        "designatedLevelOfService":data[4],                                                     #item No:5C  1  /  N  Designated Level of Service
                        "routeNumber":data[5],                                                                  #item No:5D  5  / AN  Route Number
                        "directionalSuffix":data[6]                                                             #item No:5E  1  /  N  Directional Suffi
                     }, 
   "highwayAgencyDistrict":data[7],                                                                             #item No:2   2  / AN  Highway Agency District
   "countyCode":data[8],                                                                                        #item No:3   3  /  N  Count (Parish) Code
   "placeCode":data[9],                                                                                         #item No:4   4  /  N  Place Code
   "featuresIntersected": {                                                                                     #item No:6  25  / AN  Features Intersected
                             "featuresInstersected":data[10],                                                   #item No:6A 25  / AN  Features Instersected
                             "criticalFacilityIndicator":data[11]                                               #item No:6B  1  / AN  Critical Facility Indicator
                            },                                                                                                                                         
   "facilityCarriedByStructure":data[12],                                                                       #item No:7   Facility Carried By Structure
   "location":data[13],                                                                                         #item No:9   Location
   "InventoryRTeMinVertClearance":data[14],                                                                     #item No:10  Inventory RTe, Min Vert Clearance
                                                                                   
   "kilometerpoint":data[15],                                                                                   #item No:11  Kilometerpoint
   "baseHighwayPoint":data[16],                                                                                 #item No:12  Base Highway Point
   "inventoryRouteSubrouteNumber": {                                                                            #item No:13  Inventory Route, Subroute Number
                                         "LRSInventoryRoute":data[17],                                          #item No:13A LRS Inventory Route
                                         "subrouteNumber":data[18]                                              #item No:13B Subroute Number
                                        },                                              
   "latitude":data[19],                                                                                         #item No:16  Latitude
   "longitude":data[20],                                                                                        #item No:17  Longitude
   "bypassDetourLength":data[21],                                                                               #item No:19  Bypass/Detour Length
   "toll":data[22],                                                                                             #item No:20  Toll
   "maintenanceReponsibility":data[23],                                                                         #item No:21  Maintenance Reponsibility
   "owner":data[24],                                                                                            #item No:22  Owner
   "functionalClassOfInventoryRte": data[25],                                                                   #item No:26  Functional Class Of Inventory Rte.
   "yearBuilt":data[26],                                                                                        #item No:27  Year Built
   "lanesOnUnderStructure": {                                                                                   #item No:28  Lanes On/Under Structure
                                  "lanesOnStructure":data[27],                                                  #item No:28A Lanes On Structure
                                  "lanesUnderStructure":data[28]                                                #item No:28B Lanes Under Structure
                                },  
   "averageDailyTraffic":data[29],                                                                              #item No:29   Average Daily Traffic
                                                
   "yearOfAverageDailyTraffic":data[30],                                                                        #item No:30   Year Of Average Daily Traffic
   "designLoad":data[31],                                                                                       #item No:31   Design Load
   "approachRoadwayWidth":data[32],                                                                             #item No:32   Approach Roadway Width
   "bridgeMedian":data[33],                                                                                     #item No:33   Bridge Median
   "skew":data[34],                                                                                             #item No:34   Skew
   "structureFlared":data[35],                                                                                  #item No:35   Structure Flared
   "trafficSafetyFeatures": {                                                                                   #item No:36   Traffic safety Features
                                "bridgeRailings":data[36],                                                      #item No:36A  Bridge Railings
                                "transitions":data[37],                                                         #item No:36B  Transitions
                                "approachGuardrail":data[38],                                                   #item No:36C  Approach Guardrail
                                "approachGuardrailEnds":data[39]                                                #item No:36D  Approach Guardrail Ends
                               },

   "historicalSignificance":data[40],                                                                           #item No:37  Historical significance
   "navigationControl":data[41],                                                                                #item No:38  Navigation Control
   "navigationVeriticalClearance":data[42],                                                                     #item No:39  Navigation Veritical Clearance
   "navigationHorizontalClearance":data[43],                                                                    #item No:40  Navigation Horizontal Clearance
   "strucutreOpenPostedClosed":data[44],                                                                        #item No:41  Strucutre Open/Posted/Closed
   "typeOfService":{                                                                                           #item No:42  Type of Service
                       "typeOfServiceOnBridge":data[45],                                                        #item No:42A Type of Service On Bridge"
                       "typeOfServiceUnderBridge":data[46]                                                      #item No:42B Type of Service Under Bridge
                     }, 
 
   "structureTypeMain":{                                                                                        #item No:43  Structure Type, Main
                          "kindOfMaterialDesign":data[47],                                                      #item No:43A Kind of Material/Design   
                          "typeOfDesignConstruction":data[48]                                                   #item No:43B Type of Design/Construction
                          },
   "structureTypeApproachSpans":{                                                                               #item No:44  Structure Type, Approach Spans
                                     "kindOMaterialDesign":data[49],                                            #item No:44A Kind of Material/Design
                                     "typeOfDesignContruction":data[50],                                        #item No:44B Type of Design/Contruction
                                     },                                           
                    
   "numberOfSpansInMainUnit":data[51],                                                                          #item No:45  Number of Spans in Main unit
   "numberOfApproachSpans":data[52],                                                                            #item No:46  Number of Approach Spans
   "InventoryRteTotalHorzClearance":data[53],                                                                   #item No:47  Inventory Rte Total Horz Clearance
   "lengthOfMaximumSpan":data[54],                                                                              #item No:48  Length Of Maximum Span
   "structureLength":data[55],                                                                                  #item No:49  Structure Length
   "curbSidewalk Width": {                                                                                      #item No:50  Curb/Sidewalk Width
                            "leftCurbSidewalkWidth":data[56],                                                   #item No:50A Left Curb/Sidewalk Width
                            "rightCurbSidewalkWidth":data[57]                                                   #item No:50B Right Curb/Sidewalk Width
                           },
 
   "bridgeRoadwayWithCurbToCurb":data[58],                                                                      #item No:51  Bridge Roadway with Curb-To-Curb
   "deckWidthOutToOut":data[59],                                                                                #item No:52  Deck Width, Out-To-Out
   "minVertClearOverBridgeRoadway":data[60],                                                                    #item No:53  Min Vert Clear Over Bridge Roadway
   "minimumVeriticalUnderclearance": {                                                                          #item No:54  Minimum Veritical Underclearance
                                        "referenceFeature":data[61],                                            #item No:54A Reference Feature
                                        "minimumVeriticalUnderclearance":data[62]                               #item No:54B Minimum Veritical Underclearance
                                       },     
   "minLateralUnderclearOnRight":{                                                                               #item No:55  Min Lateral underclear On Right
                                       "referenceFeature":data[63],                                             #item No:55A Reference Feature
                                       "minimumLateralUnderclearance":data[64],                                 #item No:55B Minimum Lateral Underclearance
                                     },
    
   "minLateralUnderclearOnLeft":data[65],                                                                       #item No:56 Min Lateral Underclear On Left
   "deck":data[66],                                                                                             #item No:58 Deck
   "superstructure":data[67],                                                                                   #item No:59 Superstructure
   "substructure":data[68],                                                                                     #item No:60 Substructure
   "channelChannelProtection":data[69],                                                                         #item No:61 Channel/Channel Protection
   "culverts":data[70],                                                                                         #item No:62 culverts
   "methodUsedToDetermineOperatingRating":data[71],                                                             #item No:63 Method Used to Determine Operating Rating
   "operatingRating":data[72],                                                                                  #item No:64 Operating Rating
   "methodUsedToDetermineInventoryRating":data[73],                                                             #item No:65 Method Used To Determine Inventory Rating
   "inventoryRating":data[74],                                                                                  #item No:66 Inventory Rating
   "structuralEvaluation":data[75],                                                                             #item No:67 Structural Evaluation
   "deckGeometry":data[76],                                                                                     #item No:68 Deck Geometry
   "underclearVerticalHorizontal":data[77],                                                                     #item No:69 Underclear, Vertical & Horizontal
   "bridgePosting":data[78],                                                                                    #item No:70 Bridge Posting
   "waterwayAdequacy":data[79],                                                                                 #item No:71 Waterway Adequacy
   "approachRoadwayAlignment":data[80],                                                                         #item No:72 Approach Roadway Alignment
                                        
   "typeOfWork": {                                                                                              #item No:75  Type of Work
                      "typeOfWorkProposed":data[81],                                                            #item No:75A Type of Work Proposed
                      "WorkDoneBy":data[82]                                                                     #item No:75B Work Done By
                   },  
 
   "lengthOfStructureImprovement":data[83],                                                                     #item No:76  Length Of Structure Improvement
   "inspectionDate":data[84],                                                                                   #item No:90  Inspection Date
   "designatedInspectionFrequency":data[85],                                                                    #item No:91  Designated Inspection Frequency
   "criticalFeatureInspection": {                                                                               #item No:92  Critical Feature Inspection
                                    "fractureCriticalDetails":data[86],                                         #item No:92A Fracture Critical Details
                                    "underwaterInspection":data[87],                                            #item No:92B Underwater Inspection
                                    "otherSpecialInspection":data[88]                                           #item No:92C Other Special Inspection
                                  },
   "criticalFeatureInspectionDates": {                                                                          #item No:93   Critical Feature Inspection Dates
                                          "fractureCiritcalDetailsDate":data[89],                               #item No:93A  Fracture Ciritcal Details Date
                                          "underwaterInspectionDate":data[90],                                  #item No:93B  Underwater Inspection Date
                                          "OtherSpecialInspectionDate":data[91]                                 #item No:93C  Other Special Inspection Date
                                        }, 
   "bridgeImprovementCost":data[92],                                                                            #item No:94   Bridge Improvement Cost
   "roadwayImprovementCost":data[93],                                                                           #item No:95   Roadway Improvement Cost
   "totalProjectCost":data[94],                                                                                 #item No:96   Total Project Cost
   "yearOfImprovementCost":data[95],                                                                            #item No:97   Year Of Improvement Cost
   "borderBridge": {                                                                                            #item No:98   Border Bridge
                       "neighboringStateCode":data[96],                                                         #item No:98A  Neighboring State Code
                       "percentReponsibility":data[97]                                                          #item No:98B  Percent Reponsibility
                    }, 
   "borderBridgeStructureNumber":data[98],                                                                      #item No:99   Border Bridge Structure Number
   "STRAHNETHighwayDesignation":data[99],                                                                       #item No:100  STRAHNETHighwayDesignation  
   "parallelStructureDesignation":data[100],                                                                    #item No:101  Parallel Structure Designation
   "directionOfTraffic":data[101],                                                                              #item No:102  Direction Of Traffic                    
   "temporaryStructureDesignation":data[102],                                                                   #item No:103  Federal Lands Highways
   "highwaySystemOfInventoryRoute":data[103],                                                                   #item No:104  Temporary Structure Designation
   "federalLandsHighways":data[104],                                                                            #item No:105  Highway System of Inventory Route
   "yearReconstructed":data[105],                                                                               #item No:106  Year Reconstructed
   "deckStructureType":data[106],                                                                               #item No:107  Deck Strucuture Type
   "wearingSurface/ProtectiveSystem": {                                                                         #item No:108  Wearing Surface/Protective System
                                           "typeOfWearingSurface":data[107],                                    #item No:108A Type of Wearing Surface
                                           "typeOfMembrane" :data[108],                                         #item No:108B Type of Membrane
                                           "deckProtection" :data[109]                                          #item No:108C Deck Protection
                                         },
   "avgDailyTruckTraffic":data[110],                                                                            #item No:109  AVERAGE DAILY TRUCK TRAFFIC
   "designatedNationalNetwork":data[111],                                                                       #item No:110  DESIGNATED NATIONAL NETWORK  
   "pier/abutmentProtection":data[112],                                                                         #item No:111  PIER/ABUTMENT PROTECTION 
   "nbisBridgeLength":data[113],                                                                                #item No:112  NBI BRIDGE LENGTH                        
   "scourCriticalBridges":data[114],                                                                            #item No:113  SCOUR CRITICAL BRIDGE
   "futureAvgDailyTraffic":data[115],                                                                           #item No:114  FUTURE AVERAGE DAILY TRAFFIC
   "yearOfFutureAvgDailyTraffic":data[116],                                                                     #item No:115  YEAR OF FUTURE AAVG DAILY TRAFFIC
   "minimumNavigationVerticalClearanceVerricalLiftBridge":data[117],                                            #item No:116  MINIMUM NAVIGATION VERTICAL CLEARANCE VERTICAL LIFT BRIDGE
   "federalAgencyIndicator":data[118],                                                                          #item No:117  FEDERAL AGENCY INDICATOR            
   "loc":{
           "type": "Point",
           "coordinates":[
                          Longitude,
                          Latitude
                          ] 
           }  
             })
    return x


