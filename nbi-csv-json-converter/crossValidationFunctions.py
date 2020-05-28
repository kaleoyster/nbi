'''
Title: Validation Function for Nbi JSON Encoder
Program:
Notes:
Instructions to createa a function
'''
#from nbiEncoder import *
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

#ITEM 16 - A VALID ITEM 100 IS ENTERED -- SO ITEM 16 MUST BE > 0.
def item16CrossValidationCheck1(item16, item100, crossValidation, structNumber):
    item16 = convertToNumeric(item16)
    item100 = convertToNumeric(item100)
    if(item16 != 0 ):
       if(item100 != -1):
         if(item16 > 0):
            #print('Valid -> ITEM 16 - A VALID ITEM 100 IS ENTERED -- SO ITEM 16 MUST BE > 0 ', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') -> ITEM 16 - A VALID ITEM 100 IS ENTERED -- SO ITEM 16 MUST BE > 0.('+str(item16)+') ',file = crossValidation)
       else:
          print('Item 100 is not entered',file = crossValidation)  
    else:
       print('ITEM 16 not entered ',file = crossValidation)

#ITEM 17 - A VALID ITEM 100 IS ENTERED -- SO ITEM 17 MUST BE > 0.
def item17CrossValidationCheck1(item17, item100, crossValidation, structNumber):
    item17 = convertToNumeric(item17)
    item100 = convertToNumeric(item100)
    if(item17 != 0 ):
       if(item100 != -1 ):
         if(item17 > 0):
            #print('Valid -> ITEM 17 - A VALID ITEM 100 IS ENTERED -- SO ITEM 17 MUST BE > 0 ', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') -> ITEM 17 - A VALID ITEM 100 IS ENTERED -- SO ITEM 17 MUST BE > 0.('+str(item17)+')  ',file = crossValidation)
       else:
          print('Item 100 is not entered',file = crossValidation)  
    else:
       print('ITEM 17 not entered ',file = crossValidation)

#ITEM 39 - ITEM 38 = 1 -- SO ITEM 39 MUST BE GREATER THAN ZERO.
def item39CrossValidationCheck1(item38, item39, crossValidation, structNumber):
    item38 = item38
    if(item39 != ''):
       if(item38 == '1' ):
         item39 = convertToNumeric(item39)
         if(item39 > 0):
            #print('Valid -> ITEM 39 - A VALID ITEM 39 IS 1-- SO ITEM 39 MUST BE > 0 ', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') -> ITEM 39 - A VALID ITEM 38 IS 1 -- SO ITEM 39 MUST BE > 0. ',file = crossValidation)
       else:
         pass 
    else:
       print('ITEM 39 not entered ',file = crossValidation)

#ITEM 39 - ITEM 38 = 0 - SO ITEMS 39  MUST = 0.
def item39CrossValidationCheck2(item38, item39, crossValidation, structNumber):
    item38 = item38
    if(item39 != ''):
       if(item38 == '0' ):
         item39 = convertToNumeric(item39)
         if(item39 == 0):
            #print('Valid -> ITEM 39 - A VALID ITEM 39 IS 0 -- SO ITEM 39 MUST BE = 0 ', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') -> ITEM 39 - A VALID ITEM 38 IS 0 -- SO ITEM 39 MUST BE = 0. ',file = crossValidation)
       else:
         pass 
    else:
       print('ITEM 39 not entered ',file = crossValidation)

#ITEM 40 - ITEM 38 = 0 - SO ITEMS 40 MUST = 0.
def item40CrossValidationCheck1(item38, item40, crossValidation, structNumber):
    item38 = item38
    if(item40 != ''):
       if(item38 == '0' ):
         item40 = convertToNumeric(item40)
         if(item40 == 0):
            #print('Valid -> ITEM 40 - A VALID ITEM 40 IS 0 -- SO ITEM 39 MUST BE = 0 ', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') -> ITEM 40 - A VALID ITEM 38 IS 0 -- SO ITEM 40 MUST BE = 0. ',file = crossValidation)
       else:
         pass 
    else:
       print('ITEM 40 not entered ',file = crossValidation)

#ITEM 40 - ITEM 38 = 1 -- SO ITEM 40 MUST BE GREATER THAN ZERO.
def item40CrossValidationCheck2(item38, item40, crossValidation, structNumber):
    item38 = item38
    if(item40 != ''):
       if(item38 == '1' ):
         item40 = convertToNumeric(item40)
         if(item40 > 0):
            #print('Valid -> ITEM 40 - ITEM 38 = 1 -- SO ITEM 40 MUST BE GREATER THAN ZERO.', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') ->ITEM 40 - ITEM 38 = 1 -- SO ITEM 40 MUST BE GREATER THAN ZERO. ',file = crossValidation)
       else:
         pass 
    else:
       print('ITEM 40 not entered ',file = crossValidation)

#ITEM 41 - ITEM 59 = 0 OR 1 --- SO ITEM 41 MUST = D E OR K.
def item41CrossValidationCheck1(item41, item59, crossValidation, structNumber):
    item59 = item59
    if(item41 != ''):
       if(item59 == '0' or item59 == '1' ):
         if(item41 == 'D' or item41 == 'E' or item41 == 'K') :
            #print('Valid -> ITEM 41 - ITEM 59 = 0 OR 1 --- SO ITEM 41 MUST = D E OR K.', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') ->ITEM 41 - ITEM 59 = 0 OR 1 --- SO ITEM 41 MUST = D E OR K. ',file = crossValidation)
       else:
         pass 
    else:
       print('ITEM 41 not entered ',file = crossValidation)

#ITEM 41 - ITEM 60 = 0 OR 1 --- SO ITEM 41 MUST = D E OR K.
def item41CrossValidationCheck2(item41, item60, crossValidation, structNumber):
    item60 = item60
    if(item41 != ''):
       if(item60 == '0' or item60 == '1' ):
         if(item41 == 'D' or item41 == 'E' or item41 == 'K') :
            #print('Valid -> ITEM 41 - ITEM 41 - ITEM 60 = 0 OR 1 --- SO ITEM 41 MUST = D E OR K.', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') ->ITEM 41 - ITEM 60 = 0 OR 1 --- SO ITEM 41 MUST = D E OR K. ',file = crossValidation)
       else:
         pass 
    else:
       print('ITEM 41 not entered ',file = crossValidation)

#ITEM 41 - ITEM 62 = 0 OR 1 --- SO ITEM 41 MUST = D E OR K.
def item41CrossValidationCheck3(item41, item62, crossValidation, structNumber):
    item62 = item62
    if(item41 != ''):
       if(item62 == '0' or item62 == '1' ):
         if(item41 == 'D' or item41 == 'E' or item41 == 'K') :
            #print('Valid -> ITEM 41 - ITEM 62 = 0 OR 1 --- SO ITEM 41 MUST = D E OR K.', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') ->ITEM 41 - ITEM 62 = 0 OR 1 --- SO ITEM 41 MUST = D E OR K.',file = crossValidation)
       else:
         pass 
    else:
       print('ITEM 41 not entered ',file = crossValidation)

#ITEM 41 - ITEM 103 IS = T AND ITEM 41 IS NOT = D E OR P.
def item41CrossValidationCheck4(item41, item103, crossValidation, structNumber):
    item103 = item103
    if(item41 != ''):
       if(item103 == 'T'):
         if(item41 != 'D' or item41 != 'E' or item41 != 'P') :
            #print('Valid -> ITEM 41 - ITEM 103 IS = T AND ITEM 41 IS NOT = D E OR P.', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') ->ITEM 41 - ITEM 59 = 0 OR 1 --- SO ITEM 41 MUST = D E OR P. ',file = crossValidation)
       else:
         pass 
    else:
       print('ITEM 41 not entered ',file = crossValidation)

#ITEM 42A - ITEM 28A > 0 -- SO ITEM 42A MUST BE 1 4 5 6 7 OR 8.
def item42ACrossValidationCheck1(item28A, item42A, crossValidation, structNumber):
    try:
       item28A = int(item28A)
    except:
       item28A = -1
    if(item42A != ''):
       if(item28A > 0 ):
         if(item42A == '1' or item42A == '4' or item42A == '5' or item42A == '6' or item42A == '7' or item42A == '8'):
            #print('Valid -> 42A - ITEM 28A > 0 -- SO ITEM 42A MUST BE 1 4 5 6 7 OR 8', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') -> ITEM 28A > 0 -- SO ITEM 42A MUST BE 1 4 5 6 7 OR 8 ',file = crossValidation)
       else:
         pass 
    else:
       print('ITEM 42A not entered ',file = crossValidation)

#ITEM 42B - ITEM 28B > 0 -- SO ITEM 42B MUST BE 1 4 6 OR 8.
def item42BCrossValidationCheck1(item28B, item42B, crossValidation, structNumber):
    try:
       item28B = int(item28A)
    except:
       item28B = -1
    if(item42B != ''):
       if(item28B > 0 ):
         if(item42B == '1' or item42B == '4' or item42B == '6' or  item42B == '8'):
            #print('Valid -> ITEM 42B - ITEM 28B = 0 -- SO ITEM 42B MUST BE 0 2 3 5 7 OR 9.', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') -> ITEM 42B - ITEM 28B = 0 -- SO ITEM 42B MUST BE 0 2 3 5 7 OR 9. ',file = crossValidation)
       else:
         pass 
    else:
       print('ITEM 42B not entered ',file = crossValidation)

#ITEM 42B - ITEM 28B = 0 -- SO ITEM 42B MUST BE 0 2 3 5 7 OR 9.
def item42BCrossValidationCheck2(item28B, item42B, crossValidation, structNumber):
    try:
       item28B = int(item28A)
    except:
       item28B = -1
    if(item42B != ''):
       if(item28B == 0 ):
         if(item42B == '0' or item42B == '2' or item42B == '3' or  item42B == '5' or item42B == '7' or item42B == '9'):
            #print('Valid -> ITEM 42B - ITEM 28B = 0 -- SO ITEM 42B MUST BE 0 2 3 5 7 OR 9.', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') -> ITEM 42B - ITEM 28B = 0 -- SO ITEM 42B MUST BE 0 2 3 5 7 OR 9. ',file = crossValidation)
       else:
         pass 
    else:
       print('ITEM 42B not entered ',file = crossValidation)


#ITEM 42B - ITEM 69 IS NUMERIC - 42B MUST BE = 1 2 4 6 7 OR 8
def item42BCrossValidationCheck3(item42B, item69, crossValidation, structNumber):
    isNumericFlag = False
    try:
       item69 = int(item69)
       isNumericFlag = True     
    except:
       isNumericFlag = False
  
    if(item42B != ''):
        if(isNumericFlag == True ):
            if(item42B == '1' or item42B == '2' or item42B == '4' or  item42B == '6' or item42B == '7' or item42B == '8'):
                #print('Valid -> ITEM 42B - ITEM 28B = 0 -- SO ITEM 42B MUST BE 0 2 3 5 7 OR 9.', file = crossValidation)
                pass
            else:
                print('Invalid in structure Number('+structNumber+') -> ITEM 42B - ITEM 69 IS NUMERIC - 42B MUST BE = 1 2 4 6 7 OR 8 ',file = crossValidation)
        else:
            pass 
    else:
        print('ITEM 42B not entered ',file = crossValidation)
   

#ITEM 42B - ITEM 71 IS NUMERIC - 42B MUST BE = 5 6 7 8 9 OR 0
def item42BCrossValidationCheck4(item42B, item71, crossValidation, structNumber):
    isNumericFlag = False
    try:
       item71 = int(item71)
       isNumericFlag = True     
    except:
       isNumericFlag = False
  
    if(item42B != ''):
        if(isNumericFlag == True ):
            if(item42B == '5' or item42B == '6' or item42B == '7' or  item42B == '8' or item42B == '9' or item42B == '0'):
                #print('Valid -> ITEM 71 IS NUMERIC - 42B MUST BE = 5 6 7 8 9 OR 0.', file = crossValidation)
                pass
            else:
                print('Invalid in structure Number('+structNumber+') -> ITEM 71 IS NUMERIC - 42B MUST BE = 5 6 7 8 9 OR 0',file = crossValidation)
        else:
            pass 
    else:
        print('ITEM 42B not entered ',file = crossValidation)



#ITEM 43B - ITEM 62 IS NUMERIC -- SO ITEM 43B MUST BE 19.
def item43BCrossValidationCheck1(item43B, item62, crossValidation, structNumber):
    isNumericFlag = False
    try:
       item62 = int(item62)
       isNumericFlag = True     
    except:
       isNumericFlag = False

    if(item43B != ''):
        if(isNumericFlag == True ):
            if(item43B == '19'):
                #print('Valid -> ITEM 43B - ITEM 62 IS NUMERIC -- SO ITEM 43B MUST BE 19', file = crossValidation)
                pass
            else:
                print('Invalid in structure Number('+structNumber+') -> ITEM 43B - ITEM 62  ('+str(item62 )+') IS NUMERIC -- SO ITEM 43B MUST BE 19 ('+str(item43B)+') ',file = crossValidation)
        else:
            pass 
    else:
        print('ITEM 43B not entered ',file = crossValidation)


#ITEM 47 - A VALID ITEM 100 IS ENTERED -- SO ITEM 47 MUST BE > 0.
def item47CrossValidationCheck1(item47, item100, crossValidation, structNumber):
    item47 = convertToNumeric(item47)
    item100 = item100
    if(item47 != -1 ):
       if(item100 != ''):
         if(item47 > 0):
            #print('Valid -> ITEM 47 - A VALID ITEM 100 IS ENTERED -- SO ITEM 47 MUST BE > 0 ', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') -> ITEM 47 - A VALID ITEM 100 IS ENTERED -- SO ITEM 47 MUST BE > 0 ',file = crossValidation)
       else:
          print('Item 100 is not entered',file = crossValidation)  
    else:
       print('ITEM 47 not entered ',file = crossValidation)


#ITEM 49 - ITEM 48 MUST NOT BE GREATER THAN ITEM 49.
def item49CrossValidationCheck1(item48, item49, crossValidation, structNumber):
    item48 = convertToNumeric(item48)
    item49 = convertToNumeric(item49)
    if(item48 != -1 and item49 != -1):
       if(item48 <= item49):
          #print('Valid -> ITEM 49 - ITEM 48 MUST NOT BE GREATER THAN ITEM 49.', file = crossValidation)
          pass
       else:
          print('Invalid in structure Number('+structNumber+') -> ITEM 49 - ITEM 48 MUST NOT BE GREATER THAN ITEM 49.', file = crossValidation)
    else:
       print('ITEM 48 or ITEM 49 is not entered ',file = crossValidation)



#ITEM 49 - ITEM 112 = Y -- SO ITEM 49 MUST BE > OR = 6.1 METERS
def item49CrossValidationCheck2(item49, item112, crossValidation, structNumber):
    item49 = convertToNumeric(item49)
    item112 = item112
    if(item49 != -1):
       if(item112 == 'Y'):
          if(item49 >= 6.1):
             #print('Valid -> ITEM 49 - ITEM 48 MUST NOT BE GREATER THAN ITEM 49.', file = crossValidation)
             pass
          else:
             print('Invalid in structure Number('+structNumber+') -> ITEM 49 - ITEM 48 MUST NOT BE GREATER THAN ITEM 49.',file = crossValidation)
    else:
       print('ITEM 49 is not entered ',file = crossValidation)


#ITEM 58 - ITEM 43B = 19 -- SO ITEM 58 MUST BE N.
def item58CrossValidationCheck1(item43B, item58, crossValidation, structNumber):
    try:
       item43B = convertToNumeric(item43B)    #item No:43B N Type of Design/Construction
       item58 = item58  #item No:58 AN Deck
     
    except:
       item43B = -1
       item58 = ''

    if(item43B != -1):
       if(item43B == 19):
          if(item58 == 'N'):
             #print('Valid -> ITEM 49 - ITEM 48 MUST NOT BE GREATER THAN ITEM 49.', file = crossValidation)
             pass
          else:
             print('Invalid in structure Number('+structNumber+') -> ITEM 58 - ITEM 43B = 19 -- SO ITEM 58 MUST BE N.',file = crossValidation)
    else:
       print('ITEM 43B is not entered ',file = crossValidation)

#ITEM 59 - ITEM 43B = 19 -- SO ITEM 59 MUST BE N.
def item59CrossValidationCheck1(item43B, item59, crossValidation, structNumber):
    try:
       item43B = convertToNumeric(item43B)    #item No:43B N Type of Design/Construction
       item59 = item59  #item No:59 AN Superstructure
     
    except:
       item43B = -1
       item59 = ''

    if(item43B != -1):
       if(item43B == 19):
          if(item59 == 'N'):
             #print('Valid -> ITEM 49 - ITEM 48 MUST NOT BE GREATER THAN ITEM 49.', file = crossValidation)
             pass
          else:
             print('Invalid in structure Number('+structNumber+') -> ITEM 59 - ITEM 43B = 19 -- SO ITEM 59 MUST BE N.',file = crossValidation)
    else:
       print('ITEM 43B is not entered ',file = crossValidation)

#ITEM 60 - ITEM 43B = 19 -- SO ITEM 60 MUST BE N.
def item60CrossValidationCheck1(item43B, item60, crossValidation, structNumber):
    try:
       item43B = convertToNumeric(item43B)    #item No:43B N Type of Design/Construction
       item60 = item60 #item No:60 AN Substructure
     
    except:
       item43B = -1
       item60 = ''

    if(item43B != -1):
       if(item43B == 19):
          if(item60 == 'N'):
             #print('Valid -> ITEM 49 - ITEM 48 MUST NOT BE GREATER THAN ITEM 49.', file = crossValidation)
             pass
          else:
             print('Invalid in structure Number('+structNumber+') -> ITEM 60 - ITEM 43B = 19 -- SO ITEM 60 MUST BE N.',file = crossValidation)
    else:
       print('ITEM 43B is not entered ',file = crossValidation)

#ITEM 62 - ITEM 43B = 19 -- SO ITEM 62 MUST BE NUMERIC.
def item62CrossValidationCheck1(item43B, item62, crossValidation, structNumber):
    if(item43B != ''):
       if(item43B  == '19'):
           try:
              intItem62 = int(item62)
              conFlag = True
           except:
              conFlag = False
           if(conFlag == True):
              #print('')
              pass
           else:
              print('Invalid in structure Number('+structNumber+') -> ITEM 62 - ITEM 43B = 19 -- SO ITEM 62 MUST BE NUMERIC.',file = crossValidation)  
    else:
       print('Item 43B is not entered ', file = crossValidation) 
     
 
#ITEM 64 - ITEM 41 = E -- SO ITEM 64 MUST BE = 0.
def item64CrossValidationCheck1(item41, item64, crossValidation, structNumber):
    if(item41 != ''):
       if(item41 == 'E'):
          item64 = convertToNumeric(item64)
          if(item64 == 0):
             #print('Valid -> ITEM 64 - ITEM 41 = E -- SO ITEM 64 MUST BE = 0.', file = crossValidation)
             pass
          else:
             print('Invalid in structure Number('+structNumber+') -> ITEM 64 - ITEM 41 = E -- SO ITEM 64 MUST BE = 0.',file = crossValidation)
    else:
       print('ITEM 41 is not entered ',file = crossValidation)

#ITEM 64 - ITEM 66 MUST NOT BE GREATER THAN ITEM 64.
def item64CrossValidationCheck2(item64, item66, crossValidation, structNumber):
    item64 = convertToNumeric(item64)
    item66 = convertToNumeric(item66)
    if(item64 != -1 and item66 != -1):
       if(item64 >= item66):
          #print('Valid ->ITEM 64 - ITEM 66 MUST NOT BE GREATER THAN ITEM 64.', file = crossValidation)
          pass
       else:
          print('Invalid in structure Number('+structNumber+') -> ITEM 64 - ITEM 66('+str(item66)+') MUST NOT BE GREATER THAN ITEM 64('+str(item64)+').', file = crossValidation)
    else:
       print('ITEM 64 - ITEM 66 MUST NOT BE GREATER THAN ITEM 64.',file = crossValidation)

#ITEM 66 - ITEM 41 = E -- SO ITEM 66 MUST BE = 0.
def item64CrossValidationCheck1(item41, item66, crossValidation, structNumber):
    if(item41 != ''):
       if(item41 == 'E'):
          item66 = convertToNumeric(item66)
          if(item66 == 0):
             #print('Valid -> ITEM 66 - ITEM 41 = E -- SO ITEM 66 MUST BE = 0.', file = crossValidation)
             pass
          else:
             print('Invalid in structure Number('+structNumber+') -> ITEM 66 - ITEM 41 = E -- SO ITEM 66 MUST BE = 0.',file = crossValidation)
    else:
       print('ITEM 41 is not entered ',file = crossValidation)


#ITEM 102 - ITEM 28A EQUALS 1 SO ITEM 102 MUST EQUAL 1 OR 3.
def item102CrossValidationCheck1(item28A, item102, crossValidation, structNumber):
    item28A = item28A
    if(item102 != ''):
       if(item28A == '1'):
         if(item102 == '1' or item102 == '3'):
            #print('Valid -> ITEM 28A EQUALS 1 SO ITEM 102 MUST EQUAL 1 OR 3', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') -> ITEM 102 - ITEM 28A EQUALS 1 SO ITEM 102 MUST EQUAL 1 OR 3. ',file = crossValidation)
       else:
          pass 
    else:
       print('ITEM 102 not entered ',file = crossValidation)

#ITEM 102 - ITEM 28B = 1 -- SO ITEM 102 MUST = 1 OR 3.
def item102CrossValidationCheck2(item28B, item102, crossValidation, structNumber):
    item28B = item28B
    if(item102 != ''):
       if(item28B == '1'):
         if(item102 == '1' or item102 == '3'):
            #print('Valid -> ITEM 42B - ITEM 28B = 0 -- SO ITEM 42B MUST BE 0 2 3 5 7 OR 9.', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') -> ITEM 102 - ITEM 28A EQUALS 1 SO ITEM 102 MUST EQUAL 1 OR 3. ',file = crossValidation)
       else:
          pass 
    else:
       print('ITEM 102 not entered ',file = crossValidation)

#ITEM 103 - ITEM 41 = D OR E -- SO ITEM 103 MUST BE T.

def item103CrossValidationCheck1(item41, item103, crossValidation, structNumber):
    if(item41 != ''):
       if(item41 == 'D' or item41 == 'E'):
         if(item103 == 'T') :
            #print('Valid -> ITEM 41 - ITEM 103 - ITEM 41 = D OR E -- SO ITEM 103 MUST BE T.', file = crossValidation)
            pass
         else:
            print('Invalid in structure Number('+structNumber+') ->ITEM 103 - ITEM 41 = D OR E -- SO ITEM 103 MUST BE T..',file = crossValidation)
       else:
         pass 
    else:
       print('ITEM 41 not entered ',file = crossValidation)

#ITEM 106 - ITEM 106 > 0 SO ITEM 106 MUST BE GREATER THAN ITEM 27.
def item106CrossValidationCheck1(item27, item106, crossValidation, structNumber):
    item27 = convertToNumeric(item27)
    item106 = convertToNumeric(item106)
    if(item27 != -1 and item106 != -1):
       if(item106 > item27):
          #print('Valid ->ITEM 64 - ITEM 106 - ITEM 106 > 0 SO ITEM 106 MUST BE GREATER THAN ITEM 27.', file = crossValidation)
          pass
       else:
          print('Invalid in structure Number('+structNumber+') -> ITEM 106 - ITEM 106 > 0 ('+str(item106)+') SO ITEM 106 MUST BE GREATER THAN ITEM 27('+str(item27)+').', file = crossValidation)
    else:
      pass

#ITEM 29 - ITEM 29 IS > 100 -- SO ITEM 109 MUST BE ENTERED.
def item29CrossValidationCheck1(item29, item109, crossValidation, structNumber):
    item29 = convertToNumeric(item29)
    item109 = convertToNumeric(item109)
    if(item29 != -1):
       if(item29 > 100):
          if(item109 !=-1):
             #print('Valid ->ITEM 29 - ITEM 29 IS > 100 -- SO ITEM 109 MUST BE ENTERED.', file = crossValidation)
             pass
          else:
             print('Invalid in structure Number('+structNumber+') -> ITEM 29 - ITEM 29 IS > 100 -- SO ITEM 109 MUST BE ENTERED.', file = crossValidation)
    else:
       print('ITEM 29 ('+str(item29)+') MUST BE ENTERED.',file = crossValidation)

#ITEM 111 - ITEM 38 = 1 -- SO ITEM 111 MUST BE ENTERED.
def item111CrossValidationCheck1(item38, item111, crossValidation, structNumber):
    item111 = convertToNumeric(item111)
    if(item38 != ''):
       if(item38 == '1'):
          if(item111 != -1):
             #print('Valid ->IITEM 111 - ITEM 38 = 1 -- SO ITEM 111 MUST BE ENTERED.', file = crossValidation)
             pass
          else:
             print('Invalid in structure Number('+structNumber+') -> ITEM 111 - ITEM 38 = 1 -- SO ITEM 111 MUST BE ENTERED..', file = crossValidation)
    else:
       print('ITEM 38 ('+str(item38)+')  MUST BE ENTERED.',file = crossValidation)




