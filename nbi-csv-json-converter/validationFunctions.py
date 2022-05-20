'''
Title: Validation Function for Nbi JSON Encoder
Program:
Notes:
Instructions to createa a function
'''

# Item No 1 (State Code)
def stateCodeValidate(data,validation,structNumber,fieldErrorCountArray):
       validValues = ['25',
                      '04',
                      '08',
                      '38',
                      '09',
                      '19',
                      '26',
                      '48',
                      '35',
                      '17',
                      '51',
                      '23',
                      '16',
                      '36',
                      '56',
                      '29',
                      '39',
                      '28',
                      '11',
                      '21',
                      '18',
                      '06',
                      '47',
                      '12',
                      '24',
                      '34',
                      '46',
                      '13',
                      '55',
                      '30',
                      '54',
                      '15',
                      '32',
                      '37',
                      '10',
                      '33',
                      '44',
                      '50',
                      '42',
                      '05',
                      '20',
                      '45',
                      '22',
                      '40',
                      '72',
                      '41',
                      '27',
                      '53',
                      '01',
                      '31',
                      '02',
                      '49',
                      ]

       if data in validValues:
          error = 0
          return data, error
       else:
          fieldErrorCountArray[0] = fieldErrorCountArray[0] + 1
          print('StateCode Value ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
          error = 0
          return data , error


#Item No:5A (Inventory Route)(Fatal ERROR)
def recordTypeValidate(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['1',
                   '2',
                   'A',
                   'B',
                   'C',
                   'D',
                   'E',
                   'F',
                   'G',
                   'H',
                   'I',
                   'J',
                   'K',
                   'L',
                   'M',
                   'N',
                   'O',
                   'P',
                   'Q',
                   'R',
                   'S',
                   'T',
                   'U',
                   'V',
                   'W',
                   'X',
                   'Y',
                   'Z',
                   '']

    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[2] = fieldErrorCountArray[2] + 1
        print('Record Type Validate Value ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data , error

#Item No: 5B 
def routeSigningPrefixValidate(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[3] = fieldErrorCountArray[3] + 1
        print('Routing Signing prefix Validate Value ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)         
        error = 0
        data = '-1'
        return data , error 

#Item No: 5C
def DesignatedLevelServiceValidate(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1', 
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else: 
        fieldErrorCountArray[4] = fieldErrorCountArray[4] + 1     
        print('Designated Level Service Validate Value ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)         
        error = 0
        data = '-1'
        return data , error 

#Item No: 5D (Must be 0000 if N/A )
#Route Number
def RouteNumberValidate(data,validation,structNumber,fieldErrorCountArray):
    if (data==''):
        data = '0000'
        error = 0
        return data
    else: 
        error = 0
        return data , error 
#Item No: 5E
def directionalSuffixValidate(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1', 
                   '2',
                   '3',
                   '4',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else: 
        fieldErrorCountArray[6] = fieldErrorCountArray[6] + 1     
        print('Directional Suffix Validate Value ('+ data +') Invalid in Structure Number: ' + structNumber,file = validation)         
        error = 0
        data = '-1'
        return data , error 

#Item No:6A Must be entered
#Item No:7 Must be entered
#item No:8 Flaggs two structures in the input file with same #. First one loaded, second written to report
#item NO:9 Must be entered
#Item No:10 Must be numeric
#Item No:11 Must be numeric
#Item No: 12 (Base Highway Network) (No information available)

def baseHighwayNetwork(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else: 
        fieldErrorCountArray[16] = fieldErrorCountArray[16] + 1     
        print('Base Highway Network ('+ data +') Invalid in Structure Number: ' + structNumber,file = validation)         
        error = 0
        data = '-1'
        return data , error 



#item No: 17 , 16 (Longitude, Latitude) Must be entered
def LongitudeLatitudeValidate(longitude, latitude,validation,structNumber,fieldErrorCountArray): 
    try:
       Longitude, Latitude = convertLongLat(longitude,latitude)
       if((Longitude > -180 and Longitude < 180) and (Latitude > -85 and Latitude < 85)):
           error = 0
           return longitude , latitude , error
       else:
           error = 0
           fieldErrorCountArray[19] = fieldErrorCountArray[19] + 1
           longitude = str(longitude)
           latitude = str(latitude)
           print('Longitude('+ longitude +') and Latitude ('+ latitude +')  Invalid in Structure Number: ' + structNumber , file = validation)
           longitude = 0.0 
           latitude = 0.0
           return longitude, latitude, error
    except:
       error = 0
       fieldErrorCountArray[19] = fieldErrorCountArray[19] + 1
       longitude = str(longitude)
       latitude = str(latitude)
       print('Longitude('+ longitude +') and Latitude ('+ latitude +')  Invalid in Structure Number: ' + structNumber , file = validation )
       longitude = 0.0 
       latitude = 0.0
       return longitude, latitude, error

   
            
#item No: 20 Toll Data Type: Integer
def tollValidate(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1', 
                   '2',
                   '3',
                   '4',
                   '5',
                   '']

    if data in validValues:
        error = 0
        return data, error
    else: 
        fieldErrorCountArray[22] = fieldErrorCountArray[22] + 1     
        print('Toll Validate ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)         
        error = 0
        data = '-1'
        return data , error 

#item No: 21 Maintenance Responsibility and Owner Data Type: String (Must be with in range)
def maintenanceReponsibilityValidate(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['01',
                   '02',
                   '03',
                   '04',
                   '11', 
                   '12',
                   '21',
                   '25',
                   '26',
                   '27',
                   '31',
                   '32',
                   '60',
                   '61',
                   '62',
                   '63',
                   '64',
                   '66',
                   '67',
                   '68',
                   '69',
                   '70',
                   '71',
                   '72',
                   '73',
                   '74',
                   '75',
                   '76',
                   '80',
                   '' ]
    if data in validValues:
        error = 0
        return data, error
    else: 
        fieldErrorCountArray[23] = fieldErrorCountArray[23] + 1     
        print('Maintenance Responsibility  ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)         
        error = 0
        data = '-1'
        return data , error 

#item No: 22 Owner Data Type: String (must be within range)
def OwnerValidate(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['01',
                   '02',
                   '03',
                   '04',
                   '11', 
                   '12',
                   '25',
                   '21',
                   '26',
                   '27',
                   '31',
                   '32',
                   '60',
                   '61',
                   '62',
                   '63',
                   '64',
                   '66',
                   '67',
                   '68',
                   '69',
                   '70',
                   '71',
                   '72',
                   '73',
                   '74',
                   '75',
                   '76',
                   '80',
                   '' ]
    if data in validValues:
        error = 0
        return data, error
    else: 
        fieldErrorCountArray[24] = fieldErrorCountArray[24] + 1     
        print('Owner  ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)         
        error = 0
        data = '-1'
        return data , error 

#item No: 26 Functional Classification Validate Data Type: String
def FunctionalClassificationValidate(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['01',
                   '02', 
                   '06',
                   '07',
                   '08',
                   '09',
                   '11',
                   '12',
                   '14',
                   '16',
                   '17',
                   '19',
                   '']

    if data in validValues:
        error = 0
        return data, error
    else: 
        fieldErrorCountArray[25] = fieldErrorCountArray[25] + 1     
        print('Functional Classification Validate ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)         
        error = 0
        data = 'NA'
        return data , error
 
#item No: 27 Year built, Data Type: String (Must be numeric) (Note: Not necessary)
def yearBuilt(data,validation,structNumber,fieldErrorCountArray):
    try:
       date = int(data)
       if (date < 2017):
           error = 0
           return data, error
       else:
           fieldErrorCountArray[26] = fieldErrorCountArray[26] + 1
           print('Year Built ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
           error = 0
           data = '-1'
           return data, error
    except:
       print('Year Built ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
       error = 0
       data = '-1'
       return data , error 



#item 28: has variety for Lanes On/Under Structure and dependent on  Item 5
#should be numeric

#item 29: Average Daily Traffic - dependent on  Item 5 and Item 109
#should be numeric


#item 30: Year of Average Daily Traffic - dependent on  Item 5, Item 109 item 29
def yearOfAverageDailyTrafficBuilt(data,validation,structNumber,fieldErrorCountArray,year):
    try:
       date = int(data)
       year = int(year)
       if (date < year+1):
           error = 0
           return data, error
       else:
           fieldErrorCountArray[30] = fieldErrorCountArray[30] + 1
           print('Year Of Average Daily Traffic ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
           error = 0
           data = '-1'
           return data, error
    except:
       print('Year Built ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
       error = 0
       data = '-1'
       return data , error 


#item 31: Design Load - Valid Values 0-9

def designLoadValidate(data,validation,structNumber,fieldErrorCountArray):
    #validValues = list(range(0,10)) # 10 is not inclusive
    validValues = ['1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   '0',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[31] = fieldErrorCountArray[31] + 1
        print('Design Load ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data , error

#item 32: Approach Roadway Width in meters - should be numeric

#item 33: Bridge Median - Valid values 0 to 3
def bridgeMedianValidate(data,validation,structNumber,fieldErrorCountArray):
    #validValues = list(range(0,4)) # 4 is not inclusive
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[33] = fieldErrorCountArray[33] + 1
        print('Bridge Median ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data= '-1' 
        return data , error

#item 34 - Skew - XX degrees, string

#item 35: Structure Flared - Valid values 0,1

def structureFlaredValidate(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[35] = fieldErrorCountArray[35] + 1
        print('Structure Flared ('+ data +') Invalid in Structure Number: ' + structNumber,file = validation)
        error = 0
        data = '-1'
        return data , error

#item 36A - Traffic Safety Features - Bridge Railing
def bridgeRailingsValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[36] = fieldErrorCountArray[36] + 1
        print('Bridge Railing, Features 36A ('+ data +') Invalid in Structure Number: ' + structNumber,file = validation)
        error = 0
        data = 'NA'
        return data , error

#item 36B - Traffic Safety Features - Transition Validation

def transitionsValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[37] = fieldErrorCountArray[37] + 1
        print('Transition Validation, Traffic Safety Features 36B ('+ data +') Invalid in Structure Number: ' + structNumber,file = validation)
        error = 0
        data = 'NA'
        return data , error

#item 36C - Traffic Safety Features - Apporach Guardrail Validation
def apporachGuardrailValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[38] =fieldErrorCountArray[38] + 1
        print('Apporach Guardrail Validation, Traffic Safety Features 36C('+ data +') Invalid in Structure Number: ' + structNumber,file = validation)
        error = 0
        data = 'NA'
        return data , error

#item 36D - Traffic Safety Features - Apporach Guardrail Ends Validation

def apporachGuardrailEndsValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[39] =fieldErrorCountArray[39] + 1
        print('Apporach Guardrail Ends Validation, Traffic Safety Features 36D ('+ data +') Invalid in Structure Number: ' + structNumber,file = validation)
        error = 0
        data = 'NA'
        return data , error

#item 37: Historical Significance

def historicalSigValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[40] = fieldErrorCountArray[40] + 1
        print('Historical Significance ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data ='-1'
        return data , error

#item 38 - Navigation Control
def navControlValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:

        fieldErrorCountArray[41] =fieldErrorCountArray[41] + 1
        print('Navigation Control ('+ data +') Invalid in Structure Number: ' + structNumber,file = validation)
        error = 0
        data = 'NA'
        return data , error



#item 41 - Structure Open, Posted, or Closed to Traffic

def structureTypeValidate(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['A',
                   'B',
                   'D',
                   'E',
                   'G',
                   'K',
                   'P',
                   'R',
                   '']
        
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[43] = fieldErrorCountArray[43] + 1
        print('Structure Open/Posted/Closed to Traffic ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data , error

#item 42A - Type of Service
def typeOfServiceOnBridge(data,validation,structNumber,fieldErrorCountArray):
    #validValues = list(range(0,10)) # 10 is not inclusive
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[45] = fieldErrorCountArray[45] + 1
        print('Type Of Service On Bridge ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data , error

#item 42B - Type of Service
def typeOfServiceUnderBridge(data,validation,structNumber,fieldErrorCountArray):
    #validValues = list(range(0,10)) # 10 is not inclusive
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[46] = fieldErrorCountArray[46] + 1
        print('Type Of Service Under Bridge ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data , error


#item 43A - Structure Type, Main

def kindOfMaterial(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[47] = fieldErrorCountArray[47] + 1
        print('Kind of Material, Structure Type ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data , error

#item 43B - Structure Type, Main structureTypeMain43A
def typeOfDesign(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['00',
                   '01',
                   '02',
                   '03',
                   '04',
                   '05',
                   '06',
                   '07',
                   '08',
                   '09',
                   '10',
                   '11',
                   '12',
                   '13',
                   '14',
                   '15',
                   '16',
                   '17',
                   '18',
                   '19',
                   '20',
                   '21',
                   '22',
                   '']

    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[48] = fieldErrorCountArray[48] + 1
        print('Type of Design, Structure Type, Main 43B ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data , error


#item 44A - Structure Type, Approach Spans

def structureTypeAspans44A(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[49] = fieldErrorCountArray[49] + 1
        print('Structure Type, Approach Spans 44A ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data , error

#item 44B - Structure Type, Approach Spans structureTypeMain43A
def structureTypeAspans44B(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['00',
                   '01',
                   '02',
                   '03',
                   '04',
                   '05',
                   '06',
                   '07',
                   '08',
                   '09',
                   '10',
                   '11',
                   '12',
                   '13',
                   '14',
                   '15',
                   '16',
                   '17',
                   '18',
                   '19',
                   '20',
                   '21',
                   '22',
                   '']
        
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[50] = fieldErrorCountArray[50] + 1
        print('Structure Type, Approach Spans 44B ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data , error



#Item 54A -Minimum Vertical Underclearance Reference feature

def minVerticalUnderclearanceRef(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['H',
                   'R',
                   'N',
                   '']
        
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[61] = fieldErrorCountArray[61] + 1
        print('Minimum Vertical Underclearance Reference feature 54A ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data , error
#Item 54B - Minimum Vertical Underclearance Minimum Vertical Underclearance

#Item 55A - Minimum Lateral Underclearance on Right - Reference feature
def minLateralUnderclearanceRef(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['H',
                   'R',
                   'N',
                   '']
        
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[64] = fieldErrorCountArray[64] + 1
        print('Minimum Lateral Underclearance Reference feature 54A ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data , error





#Items 58 - Indicate the Condition Ratings for Deck--
def deckRatings(data,validation,structNumber,fieldErrorCountArray):
    #validValues = list(range(0,10)) # 10 is not inclusive
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[66] = fieldErrorCountArray[66] + 1
        print('Indicate the Condition Ratings Deck ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data ='NA'
        return data , error

#Items 59 - Indicate the Condition Ratings for Superstructure--
def superstructureRatings(data,validation,structNumber,fieldErrorCountArray):
    #validValues = list(range(0,10)) # 10 is not inclusive
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[67] = fieldErrorCountArray[67] + 1
        print('Indicate the Condition Ratings Superstructure('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data ='NA'
        return data , error

#Items 60 - Indicate the Condition Ratings Substructure--
def substructureRatings(data,validation,structNumber,fieldErrorCountArray):
    #validValues = list(range(0,10)) # 10 is not inclusive
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[68] = fieldErrorCountArray[68] + 1
        print('Indicate the Condition Ratings Substructure ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error

#Item 61 - Channel and Channel Protection--
def channelProtectionValidation(data,validation,structNumber,fieldErrorCountArray):
    #validValues = list(range(0,10)) # 10 is not inclusive
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[69] = fieldErrorCountArray[69] + 1  
        print('Channel and Channel Protection ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error

#Item 62 - Culverts--
def culvertsValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[70] = fieldErrorCountArray[70] + 1  
        print('Culverts ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error

#Item 63 - Method Used to Determine Operating Rating--

def methodUsedToDetermineOperatingRatingValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[71] = fieldErrorCountArray[71] + 1
        print('Method used to Operating Rating ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data, error


#Item 65 - Method Used to Determine Inventory Rating --

def methodToDetermineInventoryRating(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[73] = fieldErrorCountArray[73] + 1
        print('MethodToDetermineInventory Rating ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data, error

#Item 66 - Inventory Rating (XX.X metric tons)

#Items 67, 68, 69, 71, and 72 - Indicate the Appraisal Ratings

#Item 67 - Structural Evaluation --
def structuralEvalValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   '0',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[75] = fieldErrorCountArray[75] + 1  
        print('Structural Evaluation ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error

#Item 68 - Deck Geometry --
def deckGeometryValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   '0',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[76] = fieldErrorCountArray[76] + 1  
        print('Deck Geometry ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error

#Item 69 - Underclearances, Vertical and Horizontal
def underclearVerticalHorizontal(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   '0',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[77] = fieldErrorCountArray[77] + 1  
        print('underclearVerticalHorizontal ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error


#Item 70 - Bridge Posting --
def bridgePosting(data,validation,structNumber,fieldErrorCountArray):
    #validValues = list(range(0,4)) # 4 is not inclusive
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[78] = fieldErrorCountArray[78] + 1  
        print('Bridge Posting ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data, error

#Item 71 - Waterway Adequacy --
# issue - this is not a composite field but three different range for each digit in value
def waterwayAdequacyValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[79] = fieldErrorCountArray[79] + 1  
        print('waterwayAdequacyValidation('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error

#Item 72 - Approach Roadway Alignment --
# No specific values provided, inferrence - they will lie in between 1-8

def approachRoadwayAlignValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[80] = fieldErrorCountArray[80] + 1  
        print('Approach Roadway Alignment ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error

#Item 73 and Item 74(Reserved)

#Item 75A - Type of Work  - Type of Work Proposed --

def typeofWork75A(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['31',
                   '32',
                   '33',
                   '34',
                   '35',
                   '36',
                   '37',
                   '38',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[81] = fieldErrorCountArray[81] + 1  
        print('Type of Work 75A ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data, error

#Item 75B - Type of Work - Work Done by --
def typeofWork75B(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['1',
                   '2',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[82] = fieldErrorCountArray[82] + 1  
        print('Type of Work 75B ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data, error




#Item 90 - Inspection Date -- (NEED A FUNCTION)
#Auxilary Function
def convertInspectionDateIntoYear(slicedYear):
    try:
       intSlicedYear  = int(slicedYear)
       convertFlag  = True
    except:
       convertFlag = False

    if (convertFlag == True):  
       if (intSlicedYear > 91):
          year = '19'+slicedYear;
       else:
          year = '20'+slicedYear;
    return year

def inspectionDateValidation(data,validation,structNumber,fieldErrorCountArray):
    date = data.zfill(4)
    slicedMonth = date[:2]
    intSlicedMonth = int(slicedMonth)
    slicedYear = date[2:4]
    year = convertInspectionDateIntoYear(slicedYear)
    if (intSlicedMonth < 13 and intSlicedMonth > 0):
        error = 0
        return data, error, year
    else:
        print('Inspection Month in Inspection Date is not within valid bounds ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = -1
        return data, error, year


#Item 91 - Designated Inspection Frequency -- (NEED A FUNCTION) can not be greater than 48

def inspectionDesignatedFrequencyValidation(data,validation,structNumber,fieldErrorCountArray):
    try:
       frequency = int(data)
    except:
       frequency = -1
    #ITEM 91 - THE INSPECTION FREQUENCY MONTHS IS GREATER THAN 48. 	Frequency cannot be greater than 48 (should be coded with leading zero if it is a sigle digit)
    if (frequency > 0 and frequency < 49):
        error = 0
        return data, error
    else:
        print('Frequency of Inspection ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        return data, error

#Item 92A - Critical Feature Inspection - Fracture Critical Details 3 digit
# First digit is Y/N flag

def criticalFeatureFactureInspectionValidation(data,validation,structNumber,fieldErrorCountArray):
    
    inspectionCode = data[:1]
    inMonth = data[1:3]

    validValues = ['Y',
                   'N',
                   ]

    if inspectionCode in validValues:
        error = 0
        try:
           if (int(inMonth) < 100):
              error = 0         
           else:
              error = 0
              print('Critical Feature Inspection ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
              data = 'NA'
              return data, error
        except:
           data = 'NA'
           return data, error        
        if inspectionCode == 'N':
           if inMonth == '00':
               error = 0
           else:
               print('Critical Feature Inspection ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
               error = 0
               data = 'NA'
               return data, error
        return data, error
    else:
        #fieldErrorCountArray[100] = fieldErrorCountArray[100] + 1
        print('Critical Feature Inspection ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error


#Item 92B - Critical Feature Inspection - Underwater Inspection 3 digit 

def criticalFeatureUnderWaterInspectionValidation(data,validation,structNumber,fieldErrorCountArray):
    inspectionCode = data[:1]
    inMonth = data[1:3]

    validValues = ['Y',
                   'N',
                   ]
    if inspectionCode in validValues:
        error = 0
        try:
           if (int(inMonth) < 100):
              error = 0         
           else:
              error = 0
              print('Critical Feature Inspection ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
              data = 'NA'
              return data, error
        except:
           data = 'NA'
           return data, error        
        if inspectionCode == 'N':
           if inMonth == '00':
               error = 0
           else:
               print('Critical Feature Inspection ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
               error = 0
               data = 'NA'
               return data, error
        return data, error
    else:
        #fieldErrorCountArray[100] = fieldErrorCountArray[100] + 1
        print('Critical Feature Inspection ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error


#Item 92C - Critical Feature Inspection - Other Special Inspection 3 digit

def criticalFeatureOtherSpecialInspectionValidation(data,validation,structNumber,fieldErrorCountArray):    
    inspectionCode = data[:1]
    inMonth = data[1:3]
    validValues = ['Y',
                   'N',
                   ]
    if inspectionCode in validValues:
        error = 0
        try:
           if (int(inMonth) < 100):
              error = 0         
           else:
              error = 0
              print('Critical Feature Inspection ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
              data = 'NA'
              return data, error
        except:
           data = 'NA'
           return data, error        
        if inspectionCode == 'N':
           if inMonth == '00':
              error = 0
           else:
               print('Critical Feature Inspection ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
               error = 0
               data = 'NA'
               return data, error
        return data, error
    else:
        #fieldErrorCountArray[100] = fieldErrorCountArray[100] + 1
        print('Critical Feature Inspection ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error

#Item 93 - Critical Feature Inspection Date - Fracture Critical Details 3 digit
#Item 93 - Critical Feature Inspection Date - Underwater Inspection 3 digit
#Item 93 - Critical Feature Inspection Date - Other Special Inspection 3 digit

#Item 94 - Bridge Improvement Cost - (Cost cant be greater than 9 million) (NEED A FUNCTION) (check length, should be 6)
#Item 95 - Roadway Improvement Cost - (Cost cant be greater than 9 million) (NEED A FUNCTION) (check length, should be 6)
#Item 96 - Total Project Cost (NEED A FUNCTION) (check length, should be 6)
#Item 97 - Year of Improvement Cost Estimate - NEED A FUNCTION(cant be more than 7 years )
def yearOfImprovementCostValidation(data,validation,structNumber,fieldErrorCountArray,inspectionYear):
    try:
        inspecYear = int(inspectionYear)
        futureYear = int(data)
        convertFlag = True
    except:
        convertFlag = False
    
    if(convertFlag == True): 
       if (futureYear <= inspecYear+ 7 ):
           error = 0
           return data, error
       else:
           error = 0
           print('year of future daily Traffic Validation ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
           data = '-1'
           return data, error
    else:
        print('year of future daily Traffic Validation ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data, error
#Item 98A - Border Bridge - Neighboring State Code |  Not sure if we want to include a list of state codes | Special case State code value = CAN or MEX
#Item 98B - Border Bridge - Percent Responsibility | Percentage

#Item 99 - Border Bridge Structure Number | no NBI Structure Number in that State's inventory file, then the entire 15-digit field shall be coded zeroes.

#Item 100 - STRAHNET Highway Designation -- (Numeric Range of values checked)

def strahnetValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[99] = fieldErrorCountArray[99] + 1  
        print('STRAHNET Highway Designation ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data, error

#Item 101 - Parallel Structure Designation -- (Range of values checked)

def parallelStructureDesignationValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['R',
                   'L',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[100] = fieldErrorCountArray[100] + 1
        print('Parallel Structure Designation ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA' 
        return data, error

#Item 102 - Direction of Traffic -- (Numeric Range of values checked)

def directionOfTrafficValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[101] = fieldErrorCountArray[101] + 1  
        print('Direction of Traffic ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data, error



#Item 103 - Temporary Structure Designation -- (Numeric Range of values checked)

def temporaryStructureValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['T',
                   ''] # T or Blank
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[102] = fieldErrorCountArray[102] + 1  
        print('Temporary Structure Designation  ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error

#Item 104 - Highway System of the Inventory Route -- (Numeric Range of values checked)

def highwaySystemInventoryRouteValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[103] = fieldErrorCountArray[103] + 1  
        print('Highway System of the Inventory Route ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data, error


#Item 105 - Federal Lands Highways -- (Numeric Range of values checked)

def federalLandsHighwaysValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '9',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[104] = fieldErrorCountArray[104] + 1  
        print('Federal Lands Highways ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data  = '-1'
        return data, error

#Item 106 - Year Reconstructed  -- Must be numeric 
def yearReconstructed(data,validation,structNumber,fieldErrorCountArray):
    if (data == ''):
        data = '-1'
        error = 0    

        return data, error

    date = int(data)
    if (date < 2017):
        error = 0
        return data, error
    else:
        fieldErrorCountArray[105] = fieldErrorCountArray[105] + 1
        print('Year Reconstructed ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data, error

#Item 107 - Deck Structure Type -- ( Range of values checked)

def deckStructureTypeValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['N',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[106] = fieldErrorCountArray[106] + 1  
        print('Deck Structure Type ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error


#Item 108A - Wearing Surface/Protective System - Type of Wearing Surface --

def wearingSurfaceValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['N',
                   '0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[107] = fieldErrorCountArray[107] + 1  
        print('Type of Wearing Surface 108A ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error

#Item 108B - Wearing Surface/Protective System - Type of Membrane --

def TypeOfMembraneValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['N',
                   '0',
                   '1',
                   '2',
                   '3',
                   '8',
                   '9',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[108] = fieldErrorCountArray[108] + 1
        print('Type of Membrane 108B ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error

#Item 108C - Wearing Surface/Protective System - Deck Protection --

def deckProtectionValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['N',
                   '0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '6',
                   '7',
                   '8',
                   '9',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[109] = fieldErrorCountArray[109] + 1  
        print('Deck Protection 108C ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error

#Item 109 - Average Daily Truck Traffic (XX percent) --

#Item 110 - Designated National Network --

def designatedNationalNetworkValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['0',
                   '1',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[111] = fieldErrorCountArray[111] + 1  
        print('Designated National Network ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data, error


#Item 111 - Pier or Abutment Protection (for Navigation)

def navProtectionValidation(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['1',
                   '2',
                   '3',
                   '4',
                   '5', 
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[112] = fieldErrorCountArray[112] + 1  
        print('Pier or Abutment Protection ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data, error

#Item 112 - NBIS Bridge Length--

def bridgeLengthNBIS(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['Y',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[113] = fieldErrorCountArray[113] + 1  
        print('NBIS Bridge Length ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error

#Item 113 - Scour Critical Bridges
def scourCriticalValidation(data,validation,structNumber,fieldErrorCountArray,inspectionYear):
    validValues = ['N',
                   'U',
                   'T',
                   '0',
                   '1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',
                   '7',
                   '8',
                   '9',
                   '']
    if data in validValues:
        error = 0
        return data, error       
    else:
        fieldErrorCountArray[114] = fieldErrorCountArray[114] + 1  
        print('Scour Critical Bridges ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error

#Item 115 - Year of Future Average Daily Traffic
def yearOfFutureDailyTrafficValidation(data,validation,structNumber,fieldErrorCountArray,inspectionYear):
    try:
        inspecYear = int(inspectionYear)
        futureYear = int(data)
        convertFlag = True
    except:
        convertFlag = False
    
    if(convertFlag == True): 
       if (futureYear <= inspecYear+ 22 ):
           error = 0
           return data, error
       else:
           error = 0
           print('year of future daily Traffic Validation ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
           data = '-1'
           return data, error
    else:
        print('year of future daily Traffic Validation ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = '-1'
        return data, error

#Item 116 - Minimum Navigation Vertical Clearance, Vertical Lift Bridge (XXX.X meters) (Must be numeric) 
def bridgeLengthNBIS(data,validation,structNumber,fieldErrorCountArray):
    validValues = ['Y',
                   'N',
                   '']
    if data in validValues:
        error = 0
        return data, error
    else:
        fieldErrorCountArray[113] = fieldErrorCountArray[113] + 1
        print('NBIS Bridge Length ('+ data +') Invalid in Structure Number: ' + structNumber ,file = validation)
        error = 0
        data = 'NA'
        return data, error


## Item No 19, 20
## Function to convert Long Lat
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
