'''
Program Title: createURL.py
PURPOSE: contains functions to create custom links
VERSION: 1

TEMPLATE: IA16

Author: Akshay Kale
'''


'''
   FUNCTION NAME: def createURL()
   The purpose of this function is to create a link depending on the input year.

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

