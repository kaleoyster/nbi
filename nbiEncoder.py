'''
Program Title: NBI BRIDGE JSON ENCODER
VERSION: 1
TEMPLATE: NBI Record Format

Author: Akshay Kale
'''

import json
from validationFunctions import *
'''
   FUNCTION NAME: def nbi_encoder()
   The purpose of this function to return a JSON formattd strings from a CSV file.
   
   INPUT PARAMETER: input parameters for this function are 1. data is a list of rows containing NBI data.
                                                           2. year integer is an integer.
                                                           3. Longitude is an intger.
                                                           4. Latitude is an integer.

   OUTPUT: The function returns a JSON formatred string using the schema described in json.dumps() function.
'''

def nbiEncoder(data,year,Longitude,Latitude):
   x = json.dumps({ 
  
   "year" : year,                                                                                                               #item No:0  YEAR      
   "stateCode":convertToString(data[0]),                                                                                        #item No:1   3  /  N  State Code
   "structureNumber":convertToString(data[1]),                                                                                  #item No:8  15  / AN  Structure Number
   "inventoryRoute": {                                                                                                          #item No:5   9  / AN  Inventory Route
                        "recordType":convertToString(data[2]),                                                                  #item No:5A  1  / AN  Record Type
                        "routeSigningPrefix":convertToString(data[3]),                                                          #item No:5B  1  /  N  Route Signing Prefix
                        "designatedLevelOfService":convertToString(data[4]),                                                    #item No:5C  1  /  N  Designated Level of Service
                        "routeNumber":convertToString(data[5]),                                                                 #item No:5D  AN  / 5  Route Number
                        "directionalSuffix":convertToString(data[6])                                                            #item No:5E  1  /  N  Directional Suffi
                     }, 
   "highwayAgencyDistrict":convertToString(data[7]),                                                                            #item No:2   2  / AN  Highway Agency District
   "countyCode":convertNumeric(data[8]),                                                                                        #item No:3   3  /  N  Count (Parish) Code
   "placeCode":convertNumeric(data[9]),                                                                                         #item No:4   4  /  N  Place Code
   "featuresIntersected": {                                                                                                     #item No:6  25  / AN  Features Intersected
                             "featuresIntersected":convertToString(data[10]),                                                   #item No:6A 25  / AN  Features Intersected (NO LONGER CODE .. Has to be BLANK)
                             "criticalFacilityIndicator":convertToString(data[11])                                              #item No:6B  1  / AN  Critical Facility Indicator
                            },                                                                                                                                        
   "facilityCarriedByStructure":convertToString(data[12]),                                                                      #item No:7  AN Facility Carried By Structure
   "location":convertToString(data[13]),                                                                                        #item No:9  AN Location
   "InventoryRTeMinVertClearance":convertToString(data[14]),                                                                     #item No:10 N Inventory RTe, Min Vert Clearance
                                                                                   
   "kilometerpoint":convertToString(data[15]),                                                                                   #item No:11 N Kilometerpoint
   "baseHighwayPoint":convertNumeric(data[16]),                                                                                 #item No:12 N Base Highway Point
   "inventoryRouteSubrouteNumber": {                                                                                            #item No:13  AN Inventory Route, Subroute Number
                                         "LRSInventoryRoute":convertToString(data[17]),                                         #item No:13A AN LRS Inventory Route
                                        },                                              
   "latitude":convertToString(data[19]),                                                                                         #item No:16 N Latitude
   "longitude":convertToString(data[20]),                                                                                        #item No:17 N Longitude
   "bypassDetourLength":convertToString(data[21]),                                                                               #item No:19 N Bypass/Detour Length (should be string)
   "toll":convertNumeric(data[22]),                                                                                             #item No:20 N Toll 
   "maintenanceReponsibility":convertNumeric(data[23]),                                                                         #item No:21 N Maintenance Reponsibility(Not Available, values not in bounds of acceptable bounds)
   "owner":convertNumeric(data[24]),                                                                                            #item No:22 N Owner (Not Available, values not in bounds of acceptable bounds)
   "functionalClassOfInventoryRte":convertToString(data[25]),                                                                    #item No:26 N Functional Class Of Inventory Rte.
   "yearBuilt":convertNumeric(data[26]),                                                                                        #item No:27 N Year Built
   "lanesOnUnderStructure": {                                                                                                   #item No:28 N Lanes On/Under Structure
                                  "lanesOnStructure":convertToString(data[27]),                                                 #item No:28A N Lanes On Structure (Doubt )
                                  "lanesUnderStructure":convertToString(data[28])                                               #item No:28B N Lanes Under Structure (Doubt )
                                },  
   "averageDailyTraffic":convertNumeric(data[29]),                                                                              #item No:29  N Average Daily Traffic
                                                
   "yearOfAverageDailyTraffic":convertNumeric(data[30]),                                                                        #item No:30  N Year Of Average Daily Traffic
   "designLoad":convertToString(data[31]),                                                                                       #item No:31  N Design Load
   "approachRoadwayWidth":convertToString(data[32]),                                                                             #item No:32  N Approach Roadway Width
   "bridgeMedian":convertNumeric(data[33]),                                                                                     #item No:33  N Bridge Median
   "skew":convertToString(data[34]),                                                                                             #item No:34  N Skew (Need Conversion, but can work without it)
   "structureFlared":convertNumeric(data[35]),                                                                                  #item No:35  N Structure Flared
   "trafficSafetyFeatures": {                                                                                                   #item No:36  AN  Traffic safety Features
                                "bridgeRailings":convertToString(data[36]),                                                   #item No:36A AN Bridge Railings
                                "transitions":convertToString(data[37]),                                                      #item No:36B AN Transitions
                                "approachGuardrail":convertToString(data[38]),                                                #item No:36C AN Approach Guardrail
                                "approachGuardrailEnds":convertToString(data[39])                                             #item No:36D AN Approach Guardrail Ends
                               },

   "historicalSignificance":convertNumeric(data[40]),                                                                           #item No:37  N Historical significance
   "navigationControl":convertToString(data[41]),                                                                             #item No:38  AN Navigation Control
   "navigationVeriticalClearance":convertToString(data[42]),                                                                     #item No:39  N Navigation Veritical Clearance (Need Conversion)
   "navigationHorizontalClearance":convertToString(data[43]),                                                                    #item No:40  N Navigation Horizontal Clearance (Need Conversion)
   "strucutreOpenPostedClosed":convertToString(data[44]),                                                                     #item No:41  AN Strucutre Open/Posted/Closed
   "typeOfService":{                                                                                                          #item No:42  N Type of Service
                       "typeOfServiceOnBridge":convertToString(data[45]),                                                        #item No:42A N Type of Service On Bridge"
                       "typeOfServiceUnderBridge":convertToString(data[46])                                                      #item No:42B N Type of Service Under Bridge
                     }, 
 
   "structureTypeMain":{                                                                                                      #item No:43  N Structure Type, Main
                          "kindOfMaterialDesign":convertToString(data[47]),                                                      #item No:43A N Kind of Material/Design   
                          "typeOfDesignConstruction":convertToString(data[48])                                                   #item No:43B N Type of Design/Construction
                          },
   "structureTypeApproachSpans":{                                                                                             #item No:44  N Structure Type, Approach Spans
                                     "kindOMaterialDesign":convertToString(data[49]),                                            #item No:44A N Kind of Material/Design
                                     "typeOfDesignContruction":convertToString(data[50]),                                        #item No:44B N Type of Design/Contruction
                                     },                                           
                    
   "numberOfSpansInMainUnit":convertNumeric(data[51]),                                                                          #item No:45  N Number of Spans in Main unit
   "numberOfApproachSpans":convertNumeric(data[52]),                                                                            #item No:46  N Number of Approach Spans
   "InventoryRteTotalHorzClearance":convertNumeric(data[53]),                                                                   #item No:47  N Inventory Rte Total Horz Clearance
   "lengthOfMaximumSpan":convertToString(data[54]),                                                                              #item No:48  N Length Of Maximum Span (Need comversiom)
   "structureLength":convertToString(data[55]),                                                                                  #item No:49  N Structure Length
   "curbSidewalk Width": {                                                                                                    #item No:50  N Curb/Sidewalk Width
                            "leftCurbSidewalkWidth":convertToString(data[56]),                                                   #item No:50A N Left Curb/Sidewalk Width
                            "rightCurbSidewalkWidth":convertToString(data[57])                                                   #item No:50B N Right Curb/Sidewalk Width
                           },
 
   "bridgeRoadwayWithCurbToCurb":convertNumeric(data[58]),                                                                      #item No:51  N Bridge Roadway with Curb-To-Curb
   "deckWidthOutToOut":convertNumeric(data[59]),                                                                                #item No:52  N Deck Width, Out-To-Out
   "minVertClearOverBridgeRoadway":convertNumeric(data[60]),                                                                    #item No:53  N Min Vert Clear Over Bridge Roadway
   "minimumVeriticalUnderclearance": {                                                                                        #item No:54  AN Minimum Veritical Underclearance
                                        "referenceFeature":convertToString(data[61]),                                         #item No:54A AN Reference Feature
                                        "minimumVeriticalUnderclearance":convertToString(data[62])                               #item No:54B N Minimum Veritical Underclearance
                                       },     
   "minLateralUnderclearOnRight":{                                                                                            #item No:55 AN Min Lateral underclear On Right
                                       "referenceFeature":convertToString(data[63]),                                          #item No:55A AN Reference Feature
                                       "minimumLateralUnderclearance":convertToString(data[64]),                                 #item No:55B N Minimum Lateral Underclearance
                                     },
    
   "minLateralUnderclearOnLeft":convertToString(data[65]),                                                                       #item No:56 N Min Lateral Underclear On Left
   "deck":convertToString(data[66]),                                                                                            #item No:58 AN Deck
   "superstructure":convertToString(data[67]),                                                                                  #item No:59 AN Superstructure
   "substructure":convertToString(data[68]),                                                                                    #item No:60 AN Substructure
   "channelChannelProtection":convertToString(data[69]),                                                                        #item No:61 AN Channel/Channel Protection
   "culverts":convertToString(data[70]),                                                                                        #item No:62 AN culverts
   "methodUsedToDetermineOperatingRating":convertNumeric(data[71]),                                                             #item No:63 N Method Used to Determine Operating Rating
   "operatingRating":convertToString(data[72]),                                                                                  #item No:64 N Operating Rating
   "methodUsedToDetermineInventoryRating":convertNumeric(data[73]),                                                             #item No:65 N Method Used To Determine Inventory Rating
   "inventoryRating":convertToString(data[74]),                                                                                  #item No:66 AN Inventory Rating
   "structuralEvaluation":convertToString(data[75]),                                                                            #item No:67 AN Structural Evaluation
   "deckGeometry":convertToString(data[76]),                                                                                    #item No:68 AN Deck Geometry
   "underclearVerticalHorizontal":convertToString(data[77]),                                                                    #item No:69 AN Underclear, Vertical & Horizontal
   "bridgePosting":convertNumeric(data[78]),                                                                                    #item No:70 N Bridge Posting
   "waterwayAdequacy":convertToString(data[79]),                                                                              #item No:71 AN Waterway Adequacy
   "approachRoadwayAlignment":convertToString(data[80]),                                                                      #item No:72 AN Approach Roadway Alignment
   "typeOfWork": {                                                                                                            #item No:75 AN Type of Work
                      "typeOfWorkProposed":convertToString(data[81]),                                                            #item No:75A N Type of Work Proposed
                      "WorkDoneBy":convertToString(data[82])                                                                  #item No:75B AN Work Done By
                   },  
   "lengthOfStructureImprovement":convertToString(data[83]),                                                                     #item No:76  N Length Of Structure Improvement
   "inspectionDate":convertNumeric(data[84]),                                                                                   #item No:90  N Inspection Date
   "designatedInspectionFrequency":convertNumeric(data[85]),                                                                    #item No:91  N Designated Inspection Frequency
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

   "bridgeImprovementCost":convertToString(data[92]),                                                                          #item No:94  N Bridge Improvement Cost
   "roadwayImprovementCost":convertToString(data[93]),                                                                         #item No:95  N Roadway Improvement Cost
   "totalProjectCost":convertToString(data[94]),                                                                               #item No:96  N Total Project Cost
   "yearOfImprovementCost":convertNumeric(data[95]),                                                                          #item No:97 N  Year Of Improvement Cost
   "borderBridge": {                                                                                                          #item No:98   Border Bridge
                       "neighboringStateCode":convertToString(data[96]),                                                      #item No:98A AN Neighboring State Code
                       "percentReponsibility":convertToString(data[97])                                                       #item No:98B N Percent Reponsibility
                    }, 
   "borderBridgeStructureNumber":convertNumeric(data[98]),                                                                    #item No:99  N Border Bridge Structure Number
   "STRAHNETHighwayDesignation":convertToString(data[99]),                                                                    #item No:100  STRAHNETHighwayDesignation  
   "parallelStructureDesignation":convertToString(data[100]),                                                                 #item No:101  Parallel Structure Designation
   "directionOfTraffic":convertNumeric(data[101]),                                                                            #item No:102  N Direction Of Traffic                    
   "temporaryStructureDesignation":convertToString(data[102]),                                                                #item No:103  Federal Lands Highways
   "highwaySystemOfInventoryRoute":convertNumeric(data[103]),                                                                 #item No:104  N Temporary Structure Designation
   "federalLandsHighways":convertNumeric(data[104]),                                                                          #item No:105  N Highway System of Inventory Route
   "yearReconstructed":convertNumeric(data[105]),                                                                             #item No:106  N Year Reconstructed
   "deckStructureType":convertToString(data[106]),                                                                            #item No:107  AN  Deck Strucuture Type
   "wearingSurface/ProtectiveSystem": {                                                                                       #item No:108  AN Wearing Surface/Protective System
                                           "typeOfWearingSurface":convertToString(data[107]),                                 #item No:108A AN Type of Wearing Surface
                                           "typeOfMembrane" :convertToString(data[108]),                                      #item No:108B AN Type of Membrane
                                           "deckProtection" :convertToString(data[109])                                       #item No:108C AN Deck Protection
                                         },
   "avgDailyTruckTraffic":convertNumeric(data[110]),                                                                          #item No:109 N AVERAGE DAILY TRUCK TRAFFIC
   "designatedNationalNetwork":convertNumeric(data[111]),                                                                     #item No:110 N  DESIGNATED NATIONAL NETWORK  
   "pier/abutmentProtection":convertNumeric(data[112]),                                                                       #item No:111 N PIER/ABUTMENT PROTECTION 
   "nbisBridgeLength":convertToString(data[113]),                                                                             #item No:112  NBI BRIDGE LENGTH                        
   "scourCriticalBridges":convertToString(data[114]),                                                                         #item No:113  SCOUR CRITICAL BRIDGE
   "futureAvgDailyTraffic":convertToString(data[115]),                                                                         #item No:114  N FUTURE AVERAGE DAILY TRAFFIC
   "yearOfFutureAvgDailyTraffic":convertNumeric(data[116]),                                                                   #item No:115  N YEAR OF FUTURE AAVG DAILY TRAFFIC
   "minimumNavigationVerticalClearanceVerricalLiftBridge":convertToString(data[117]),                                          #item No:116  N MINIMUM NAVIGATION VERTICAL CLEARANCE VERTICAL LIFT BRIDGE
   "federalAgencyIndicator":convertToString(data[118]),                                                                       #item No:117  FEDERAL AGENCY INDICATOR
   "dateLastUpdate":convertToString(data[119]),
   "typeLastUpdate":convertToString(data[120]),
   "deductCode":convertToString(data[121]),
   
   "status with 10 year rule":convertToString(data[130]),                                                                     #item No:118  Status with 10 Year Rule
   "sufficiencyRatingAsteriskField":convertToString(data[131]),                                                               #item No:119  Sufficiency Rating Asterisk field
   "sufficiencyRating":convertToString(data[132]),                                                                            #item No:120  Sufficiency Rating
   "status without 10 year rule":convertToString(data[133]),                                                                  #item No:121  Status Without 10 Year Rule
    #"CAT 10":convertToString(data[134]), 
    #TYPE_LAST_UPDATE[119],
    #DEDUCT_CODE[120],
    #REMARKS[121],
    #PROGRAM_CODE[122], 
    #PROJ_NO[123],
    #PROJ_SUFFIX[124],
    #NBI_TYPE_OF_IMP[125],
    #DTL_TYPE_OF_IMP[126],
    #SPECIAL_CODE[127],
    #STEP_CODE[128],
    #STATUS_WITH_10YR_RULE[129],
    #SUFFICIENCY_ASTERC[130],
    #SUFFICIENCY_RATING[131],
    #STATUS_NO_10YR_RULE[132]
           
   "loc":{
           "type": "Point",
           "coordinates":[
                          Longitude,
                          Latitude
                          ] 
    #Programming guide: we wont be able tp consistent with guide 
            }  
             })
   return x


#utility functions


#Function to convert string into int
def convertNumeric(s):
    try:
       res = convertToNumeric(s)
    except ValueError:
       #print("Error: values is expected to be Numeric for ", s)
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
def initializeValidationArray(validationArray,size):
    for i in range(size):
        validationArray.append(0)
    return validationArray


#function to validate NBI ROWS
def validateNBIfields(temp, ErrorCheck, fieldErrorCountArray,validation,size):
    
    ErrorCheck = initializeValidationArray(ErrorCheck,size) # ErrorCheck will maintain a list of invalid error encountered in a row
    structNumber = temp[1]
    #Guide:  
    # eg: temp[0], ErrorCheck[0] = stateCodeValidate(temp[0],validation,structNumber,fieldErrorCountArray)
    #
    #    temp[0] = State Code (check nbiCoder)
    #    ErrorCheck[0] = If state code is invalid, this will mark '1' at index 0 of ErrorCheck to denote that StateCode is invalid
    #
    #    stateCodeValidate takes following as the arguments:
    # 1. temp[0], the stateCode
    # 2. validation, instance of opened log file, which will record all invalid data
    # 3. structure Number, to identify there occurs an error
    # 4. fieldErrorCountArry, to keep a Total count of invalid field through a file
 
    temp[0], ErrorCheck[0] = stateCodeValidate(temp[0],validation,structNumber,fieldErrorCountArray)
    temp[2], ErrorCheck[2] = recordTypeValidate(temp[2],validation,structNumber,fieldErrorCountArray)
    temp[3], ErrorCheck[3] = routeSigningPrefixValidate(temp[3],validation,structNumber,fieldErrorCountArray)
    temp[4], ErrorCheck[4] = DesignatedLevelServiceValidate(temp[4],validation,structNumber,fieldErrorCountArray)
    temp[6], ErrorCheck[6] = directionalSuffixValidate(temp[6],validation,structNumber,fieldErrorCountArray)
    temp[16], ErrorCheck[16] = baseHighwayNetwork(temp[16],validation,structNumber,fieldErrorCountArray)                    
    temp[20], temp[19], ErrorCheck[19] = LongitudeLatitudeValidate(temp[20],temp[19],validation,structNumber,fieldErrorCountArray)
    temp[22], ErrorCheck[22] = tollValidate(temp[22],validation,structNumber,fieldErrorCountArray)
    temp[23], ErrorCheck[23] = maintenanceReponsibilityValidate(temp[23],validation,structNumber,fieldErrorCountArray)
    temp[24], ErrorCheck[24] = OwnerValidate(temp[24],validation,structNumber,fieldErrorCountArray)
    temp[25], ErrorCheck[25] = FunctionalClassificationValidate(temp[25],validation,structNumber,fieldErrorCountArray)
    temp[26], ErrorCheck[26] = yearBuilt(temp[26],validation,structNumber,fieldErrorCountArray)
    temp[31], ErrorCheck[31] = designLoadValidate(temp[31],validation,structNumber,fieldErrorCountArray)
    temp[33], ErrorCheck[33] = bridgeMedianValidate(temp[33],validation,structNumber,fieldErrorCountArray)
    temp[35], ErrorCheck[35] = structureFlaredValidate(temp[35],validation,structNumber,fieldErrorCountArray)
    temp[36], ErrorCheck[36] = bridgeRailingsValidation(temp[36],validation,structNumber,fieldErrorCountArray)
    temp[37], ErrorCheck[37] = transitionsValidation(temp[37],validation,structNumber,fieldErrorCountArray)
    temp[38], ErrorCheck[38] = apporachGuardrailValidation(temp[38],validation,structNumber,fieldErrorCountArray)
    temp[39], ErrorCheck[39] = apporachGuardrailEndsValidation(temp[39],validation,structNumber,fieldErrorCountArray)
    temp[40], ErrorCheck[40] = historicalSigValidation(temp[40],validation,structNumber,fieldErrorCountArray)
    temp[41], ErrorCheck[41] = navControlValidation(temp[41],validation,structNumber,fieldErrorCountArray)
    temp[44], ErrorCheck[44] = structureTypeValidate(temp[44],validation,structNumber,fieldErrorCountArray)
    temp[45], ErrorCheck[45] = typeOfServiceOnBridge(temp[45],validation,structNumber,fieldErrorCountArray)
    temp[46], ErrorCheck[46] = typeOfServiceUnderBridge(temp[46],validation,structNumber,fieldErrorCountArray)
    temp[47], ErrorCheck[47] = kindOfMaterial(temp[47],validation,structNumber,fieldErrorCountArray)
    temp[48], ErrorCheck[48] = typeOfDesign(temp[48],validation,structNumber,fieldErrorCountArray)
    temp[49], ErrorCheck[49] = structureTypeAspans44A(temp[49],validation,structNumber,fieldErrorCountArray)
    temp[50], ErrorCheck[50] = structureTypeAspans44B(temp[50],validation,structNumber,fieldErrorCountArray)
    temp[61], ErrorCheck[61] = minVerticalUnderclearanceRef(temp[61],validation,structNumber,fieldErrorCountArray)
    temp[63], ErrorCheck[63] = minLateralUnderclearanceRef(temp[63],validation,structNumber,fieldErrorCountArray)
    temp[66], ErrorCheck[66] = deckRatings(temp[66],validation,structNumber,fieldErrorCountArray)
    temp[67], ErrorCheck[67] = superstructureRatings(temp[67],validation,structNumber,fieldErrorCountArray)
    temp[68], ErrorCheck[68] = substructureRatings(temp[68],validation,structNumber,fieldErrorCountArray)
    temp[69], ErrorCheck[69] = channelProtectionValidation(temp[69],validation,structNumber,fieldErrorCountArray)
    temp[70], ErrorCheck[70] = culvertsValidation(temp[70],validation,structNumber,fieldErrorCountArray)
    #temp[73], ErrorCheck[71] = methodUsedToDetermineOperatingRatingValidation(temp[71],validation,structNumber,fieldErrorCountArray)
    #temp[72], ErrorCheck[72] = operatingRatingValidation(temp[72],validation,structNumber,fieldErrorCountArray)
    #temp[73], ErrorCheck[73] = inventoryRating(temp[74],validation,structNumber,fieldErrorCountArray)
    temp[75], ErrorCheck[75] = structuralEvalValidation(temp[75],validation,structNumber,fieldErrorCountArray)
    temp[76], ErrorCheck[76] = deckGeometryValidation(temp[76],validation,structNumber,fieldErrorCountArray)
    temp[77], ErrorCheck[77] = underclearVerticalHorizontal(temp[77],validation,structNumber,fieldErrorCountArray)
    temp[78], ErrorCheck[78] = bridgePosting(temp[78],validation,structNumber,fieldErrorCountArray)
    temp[80], ErrorCheck[80] = approachRoadwayAlignValidation(temp[80],validation,structNumber,fieldErrorCountArray)
    temp[81], ErrorCheck[81] = typeofWork75A(temp[81],validation,structNumber,fieldErrorCountArray)
    temp[82], ErrorCheck[82] = typeofWork75B(temp[82],validation,structNumber,fieldErrorCountArray)
    temp[99], ErrorCheck[99] = strahnetValidation(temp[99],validation,structNumber,fieldErrorCountArray)
    temp[100], ErrorCheck[100] = parallelStructureDesignationValidation(temp[100],validation,structNumber,fieldErrorCountArray)
    temp[101], ErrorCheck[101] = directionOfTrafficValidation(temp[101],validation,structNumber,fieldErrorCountArray)
    temp[102], ErrorCheck[102] = temporaryStructureValidation(temp[102],validation,structNumber,fieldErrorCountArray)
    temp[103], ErrorCheck[103] = highwaySystemInventoryRouteValidation(temp[103],validation,structNumber,fieldErrorCountArray)
    temp[104], ErrorCheck[104] = federalLandsHighwaysValidation(temp[104],validation,structNumber,fieldErrorCountArray)
    temp[105], ErrorCheck[105] = yearReconstructed(temp[105],validation,structNumber,fieldErrorCountArray) 
    temp[106], ErrorCheck[106] = deckStructureTypeValidation(temp[106],validation,structNumber,fieldErrorCountArray)
    
    temp[107], ErrorCheck[107] = wearingSurfaceValidation(temp[107], validation,structNumber,fieldErrorCountArray)
    temp[108], ErrorCheck[108] = TypeOfMembraneValidation(temp[108], validation,structNumber, fieldErrorCountArray)
    temp[109], ErrorCheck[109] = deckProtectionValidation(temp[109], validation,structNumber, fieldErrorCountArray)
    temp[111], ErrorCheck[111] = designatedNationalNetworkValidation(temp[111], validation, structNumber, fieldErrorCountArray)
    temp[112], ErrorCheck[112] = navProtectionValidation(temp[112],validation,structNumber,fieldErrorCountArray)
    temp[113], ErrorCheck[113] = bridgeLengthNBIS(temp[113],validation,structNumber,fieldErrorCountArray)
    temp[114], ErrorCheck[114] = scourCriticalValidation(temp[114],validation,structNumber,fieldErrorCountArray)

                             
    return temp, ErrorCheck


