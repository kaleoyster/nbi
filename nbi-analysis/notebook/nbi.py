from pymongo import MongoClient
import pandas as pd
import csv

code_state_mapping = {'25':'MA',
                            '04':'AZ',
                            '08':'CO',
                            '38':'ND',
                            '09':'CT',
                            '19':'IA',
                            '26':'MI',
                            '48':'TX',
                            '35':'NM',
                            '17':'IL',
                            '51':'VA',
                            '23':'ME',
                            '16':'ID',
                            '36':'NY',
                            '56':'WY',
                            '29':'MO',
                            '39':'OH',
                            '28':'MS',
                            '11':'DC',
                            '21':'KY',
                            '18':'IN',
                            '06':'CA',
                            '47':'TN',
                            '12':'FL',
                            '24':'MD',
                            '34':'NJ',
                            '46':'SD',
                            '13':'GA',
                            '55':'WI',
                            '30':'MT',
                            '54':'WV',
                            '15':'HI',
                            '32':'NV',
                            '37':'NC',
                            '10':'DE',
                            '33':'NH',
                            '44':'RI',
                            '50':'VT',
                            '42':'PA',
                            '05':'AR',
                            '20':'KS',
                            '45':'SC',
                            '22':'LA',
                            '40':'OK',
                            '72':'PR',
                            '41':'OR',
                            '27':'MN',
                            '53':'WA',
                            '01':'AL',
                            '31':'NE',
                            '02':'AK',
                            '49':'UT'
                   }

def connectToNBI(collection_name,connection_string):
    """
       description: connects to NBI mongodb instance and returns a collection 
       input type: collection_name - [string], connection_string - [string]
       return type: collection - [string]
       
    """

    Client = MongoClient(connection_string)
    db = Client.nbi
    collection = db[collection_name]
    return collection


def getSurveyRecords(states, years, fields, db, connection_string):
    """  
       
        description: returns survey records of provided states, years from the collection.
        input type:  states - [list], year - [list], db - [string], connection_string - [string]
        return type: survey_records - [dataframe] 
 
    """
    collection = connectToNBI(db,connection_string)
    masterdec = []
    for yr in years:
        for state in states:
            pipeline = [{"$match":{"$and":[{"year":yr},{"stateCode":state}]}},
                        {"$project":fields}]
            dec = collection.aggregate(pipeline)
            for i in list(dec):
                masterdec.append(i)
    survey_records = pd.DataFrame(masterdec)
    return survey_records


def filterSurveyData(survey_records):
    """ 
    decription: filters missing and 'NA' values from condition rating: deck, substructure, and superstructure. And, discrards structure type = 19 and type of wearing surface = '6'
    
    return type:
    :dataframe: filtred survey records, length of survey records before filteration and after filteration 
    :list: before_filtr : before_filter - length of the survey records 
    :list: after_filtr  : after_filter - length of the survey records
    
    """   
    
    before_filtr = len(survey_records) ## Length of survey record before filtering

    
    ## Filtring Criteria for  deck, substructure and superstructure
    survey_records = survey_records.loc[~survey_records['deck'].isin(['N','NA'])]
    survey_records = survey_records.loc[~survey_records['substructure'].isin(['N','NA'])]
    survey_records = survey_records.loc[~survey_records['superstructure'].isin(['N','NA'])]
    
    ## discards survey records of Structure type - 19  and Type of Wearing Surface - 6
    survey_records = survey_records.loc[~survey_records['Structure Type'].isin([19])]
    survey_records = survey_records.loc[~survey_records['Type of Wearing Surface'].isin(['6'])]
  

    after_filtr = len(survey_records) ## Length of survey record before filtering
    
    return survey_records, before_filtr, after_filtr


def same_elements(elements):
    """
     description: Checks if all the elements of the list are equal
     
     return type:
     :Boolean: returns True if the all the elements of the list are equal 
     
    """
    if not elements:
        return True
    return [elements[0]*len(elements) == elements]


def createTimeseries(survey_records):
    """Create time series data from the loose records"""
    survey_timeseries = [[key]+[col for col in value] for key, value in {k:[g['Age'].tolist(),g['ADT Type'].tolist(),g['superstructure'].tolist(),g['Avg. Daily Precipitation (mm)'].tolist(), g['stateCode'].tolist(), g['averageDailyTraffic'].tolist(),g["owner"].tolist()] for k, g in survey_records.groupby('structureNumber')}.items()]
    # for key, value in {k:[g['Age'].tolist(),g['ADT Type'].tolist(),g['Category'],g['superstructure'].tolist()] for k, g in survey_records.groupby('structureNumber')}.items():
    return survey_timeseries


def createTimeseriesLifeCycle(survey_records):
    """Create time series data from the loose records"""
    survey_timeseries = [[key]+[col for col in value] for key, value in {k:[g['Age'].tolist(),g['deck'].tolist(),g['superstructure'].tolist(),g['substructure'].tolist(), g['stateCode'].tolist(), g['yearBuilt'].tolist(),g["yearReconstructed"].tolist()] for k, g in survey_records.groupby('structureNumber')}.items()]
    # for key, value in {k:[g['Age'].tolist(),g['ADT Type'].tolist(),g['Category'],g['superstructure'].tolist()] for k, g in survey_records.groupby('structureNumber')}.items():
    return survey_timeseries


def retMaterialNames(structure_type_coding):
    """ return kind of material name of the structure type code"""
    
    kind_of_material = {
                            1:"Concrete",
                            2:"Concrete Continuous",
                            3:"Steel",
                            4:"Steel Continuous",
                            5:"Prestressed Concrete",
                            6:"Prestressed Concrete Continuous",
                            7:"Wood or Timber",
                            8:"Masonry",
                            9:"Aluminum, Wrought Iron, or Cast Iron",
                            10:"Other",
                       }
    
    material_names = structure_type_coding.map(kind_of_material)
    
    return material_names

def retDeckProctectionNames(type_of_wearing_surface_coding):
    """ return deck protection name of the type of wearing code """
    
    deck_protection = {
                        '1':'Epoxy Coated Reinforcing',
                        '2':'Galvanized Reinforcing',
                        '3':'Other Coated Reinforcing',
                        '4':'Cathodic Protection',
                        '6':'Polymer Impregnated',
                        '7':'Internally Sealed',
                        '8':'Unknown',
                        '9':'Other',
                        '0':'None',
                        'N':'Not Applicable'
        
                      }
    
    deck_protection_names = type_of_wearing_surface_coding.map(deck_protection)
    
    return deck_protection_names



def getAges(bridgeSurveyYear, builtSurveyYearBuilt):
    """ returns age of bridges """
    return bridgeSurveyYear - builtSurveyYearBuilt


def categorizeBridgesByADT(ADT): 
    """ returns A list of class of the bridge as define by Author in so and so """
    class_of_bridges_adt = []
    for adt in ADT:
        if adt < 100:
            class_of_bridges_adt.append('Very Light')     
        elif 100 <= adt < 1000:
            class_of_bridges_adt.append('Light')
        elif 1000 <= adt < 5000:
            class_of_bridges_adt.append('Moderate')
        elif 5000 <= adt:
            class_of_bridges_adt.append('Heavy')
        else:
            class_of_bridges_adt.append('IDK')
    return class_of_bridges_adt


def categorizeBridgesByADTT(ADTT): 
    """ returns A list of class of the bridge as define by Author in so and so """
    class_of_bridges_adtt = []
    for adtt in ADTT:
        if adtt < 100:
            class_of_bridges_adtt.append('Light')     
        elif 100 <= adtt < 500:
            class_of_bridges_adtt.append('Moderate')
        elif 500 <= adtt:
            class_of_bridges_adtt.append('Heavy')
        else:
            class_of_bridges_adtt.append('IDK')
    return class_of_bridges_adtt



def countCats(list_of_classes):
    """ returns a dictionary of count of all categories of the bridges """
    return {cls:list_of_classes.count(cls) for cls in set(list_of_classes)}



def codeToState(list_of_statecode):
    """return a list of name of states """
 #   Arizona, Colorado, Idaho, Montana, Nevada, New Mexico, Utah, Wyoming, Alaska, California, Hawaii, Oregon, and Washington
 #   Puerto Rico and other US territories are not part of any census region or census division.
 #   04, 08, 16, 32, 30, 35, 49, 56, 01, 06, 15, 41, 53, 72 

    code_state_mapping =   {'25':'MA',
                            '04':'AZ',
                            '08':'CO',
                            '38':'ND',
                            '09':'CT',
                            '19':'IA',
                            '26':'MI',
                            '48':'TX',
                            '35':'NM',
                            '17':'IL',
                            '51':'VA',
                            '23':'ME',
                            '16':'ID',
                            '36':'NY',
                            '56':'WY',
                            '29':'MO',
                            '39':'OH',
                            '28':'MS',
                            '11':'DC',
                            '21':'KY',
                            '18':'IN',
                            '06':'CA',
                            '47':'TN',
                            '12':'FL',
                            '24':'MD',
                            '34':'NJ',
                            '46':'SD',
                            '13':'GA',
                            '55':'WI',
                            '30':'MT',
                            '54':'WV',
                            '15':'HI',
                            '32':'NV',
                            '37':'NC',
                            '10':'DE',
                            '33':'NH',
                            '44':'RI',
                            '50':'VT',
                            '42':'PA',
                            '05':'AR',
                            '20':'KS',
                            '45':'SC',
                            '22':'LA',
                            '40':'OK',
                            '72':'PR',
                            '41':'OR',
                            '27':'MN',
                            '53':'WA',
                            '01':'AL',
                            '31':'NE',
                            '02':'AK',
                            '49':'UT'
                   }
    
    state_names = [code_state_mapping[statecode] for statecode in  list_of_statecode]
    return state_codes

def stateToCode(list_of_statename):
    """ return a list of state code from state name """
    code_state_mapping =   {
                            '25':'MA',
                            '04':'AZ',
                            '08':'CO',
                            '38':'ND',
                            '09':'CT',
                            '19':'IA',
                            '26':'MI',
                            '48':'TX',
                            '35':'NM',
                            '17':'IL',
                            '51':'VA',
                            '23':'ME',
                            '16':'ID',
                            '36':'NY',
                            '56':'WY',
                            '29':'MO',
                            '39':'OH',
                            '28':'MS',
                            '11':'DC',
                            '21':'KY',
                            '18':'IN',
                            '06':'CA',
                            '47':'TN',
                            '12':'FL',
                            '24':'MD',
                            '34':'NJ',
                            '46':'SD',
                            '13':'GA',
                            '55':'WI',
                            '30':'MT',
                            '54':'WV',
                            '15':'HI',
                            '32':'NV',
                            '37':'NC',
                            '10':'DE',
                            '33':'NH',
                            '44':'RI',
                            '50':'VT',
                            '42':'PA',
                            '05':'AR',
                            '20':'KS',
                            '45':'SC',
                            '22':'LA',
                            '40':'OK',
                            '72':'PR',
                            '41':'OR',
                            '27':'MN',
                            '53':'WA',
                            '01':'AL',
                            '31':'NE',
                            '02':'AK',
                            '49':'UT'
                   }
    
    reverse_code_state_map = {value: key for key, value in code_state_mapping.items()}
    state_names = [code_state_mapping[statename] for statecode in  list_of_statename]
    return state_names

def getDictFipsCounty(fips, counties):
    """return a dictionary of key: fip and  value: county"""
    return {fip:county for fip, county in zip(fips,counties)}
    
def getDictFipsAdp(fips, daily_precps):
    """return a dictionary of key: fips and value: daily_precps"""
    return {fip:dlp for fip, dlp in zip(fips,daily_precps)}
    
def correctFips(stateCodes, FIPS):
    """ return a list of correctFips from FIPS"""
    return [str(stateCode) + str(fcode).zfill(3) for stateCode,fcode in zip(stateCodes,FIPS)]

def getCounty(FIPS, counties):
    """ returns a list of county from FIPS"""
    county = []
    for fip in FIPS:
        try:
            county.append(getCountyFips(FIPS, counties)[fip])
        except:
            county.append("NA")
    return county

def getAverageDailyPrecp(FIPS, daily_precps):
    """ returns a list of average daily precipitation from  FIPS"""
    avg_daily_precp = []
    for fip in FIPS:
        try:
            avg_daily_precp.append(getDailyPrecpOfFips(fips, daily_precps)[fip])
        except:
            avg_daily_precp.append(-1)
    return avg_daily_precp  


def getDict(keys, values):
    """ return a dictionary of key and value"""
    return {str(key):value for key, value in zip(keys,values)}


################################################## FUNCTIONS TO SPLIT RECORDS (INTERVENTIONS) ####################################################################
def createTimeseries(survey_records):
    """Create time series data from the loose records"""
    survey_timeseries = [[key]+[col for col in value] for key, value in {k:[g['Age'].tolist(),g['ADT Type'].tolist(),g['superstructure'].tolist(),g['Avg. Daily Precipitation (mm)'].tolist(), g['stateCode'].tolist(), g['averageDailyTraffic'].tolist(),g["owner"].tolist()] for k, g in survey_records.groupby('structureNumber')}.items()]
    # for key, value in {k:[g['Age'].tolist(),g['ADT Type'].tolist(),g['Category'],g['superstructure'].tolist()] for k, g in survey_records.groupby('structureNumber')}.items():
    return survey_timeseries
    

## 2nd in sequence
def createProfile(data):
    """ this function creates a profile to split records ## Renamed backward difference"""
    counter = 0
    profile = [True]
    while counter+1 < len(data):
        if data[counter] < data[counter+1]:
            profile.append(True)
        else:
            profile.append(False)
            profile.append(True)
        counter = counter + 1
    return profile

###

def createBackwardProfile(data):
    """ this function creates a profile to split records ## Renamed backward difference"""
    counter = 0
    profile = [True]
    while counter+1 < len(data):
        if data[counter+1] - data[counter] < 26 :
            profile.append(True)
        else:
            profile.append(False)
            profile.append(True)
        counter = counter + 1
    return profile


def utilitySplitBridgeRecords(data, profile):
    """ The ultility function to split records by intervention
     Takes a 1xn list returns 2xn list"""
    """Modify here"""
    counter = 0
    main_list = []
    temp_list = []
    for bval in profile:
        if bval == True:
            temp_list.append(data[counter])
            counter  = counter + 1 
        else:
            main_list.append(temp_list)
            temp_list = []        
    main_list.append(temp_list)
    return main_list


def splitSurveyRecords(survey_timeseries):
    """return split records of bridge to account intervention like Rebuilt, Reconstruction, and Rehabilitation"""
    temp = []
    for i in survey_timeseries:
        profile = createProfile((i[1]))
        #print("Create Profile:",i[1])
        temp_list = []
        temp_list.append(i[0])
        for row in i[1:]:
            split_records = utilitySplitBridgeRecords(row, profile)
#             #print(split_records)
#             split_again = []
#             for sp_record in split_records:
#                 #print("Create B Profile:",sp_record)
#                 bp = createBackwardProfile(sp_record)
#                 for record in utilitySplitBridgeRecords(sp_record,bp):
#                     split_again.append(record)
            
            temp_list.append(split_records)
        temp.append(temp_list)
        
    return temp




# data = [2,3,4,5,6,78,1,2,79,80,1,2,3,4,5]
# p = createProfile(data)
# d = utilitySplitBridgeRecords(data,p)
# #print(d)
# split_front = []
# for i in d:
#     bp = createBackwardProfile(i)
#     #split_front.append(utilitySplitBridgeRecords(i,bp)[0])
#     for j in utilitySplitBridgeRecords(i,bp):
#         split_front.append(j)
# #




## combine function:
def combinedStructureNumberWithRecords(structure_numbers_split_records, s):
    """Combine function of split structure numbers with the rest of the records"""
    combined_records = []
    for h,j in zip(structure_numbers_split_records, s):
        combined_records.append([h]+j[1:])
    return combined_records

def splitStructureNumbers(s):
    structure_numbers_split_records = []
    for i in s:
        len_K = len(i[1])
        structureNumber = i[0]
        structureNumbers = []
        for k in range(len_K):
            stNumber=(str(structureNumber)+'_'+str(k+1))
            structureNumbers.append(stNumber)
        structure_numbers_split_records.append(structureNumbers)
    return structure_numbers_split_records

def createIndividualRecords(survey_records):
    """ create split records from individual records """
    split_by_intervention_survey_records = []
    length_i = len(survey_records[0])
    for i in survey_records:
        length = len(i[1])
        for j in range(length):
            split_temp1 = []
            for k in range(0,length_i):
                split_temp1.append(i[k][j])
            split_by_intervention_survey_records.append(split_temp1)
    return split_by_intervention_survey_records



def createSplitProfiles(survey_timeseries):
    split_profiles = []
    for record in survey_timeseries:
        temp = []
        for ages in record[1]:
            temp.append(createBackwardProfile(ages))
        split_profiles.append(temp)
    return split_profiles

# ####### IN EDIT #######

# def createCRProfile(ConditionRatings):
#     """ this function creates a profile to split records using Condition Rating"""
#     counter = 0
#     profile = [True]
#     while counter+1 < len(data):
#         # Save data[Counter 1]
#         # Save data[Counter 2]
#         counter1
        
#         if int(data[counter+1]) - int(data[counter]) : [9,8,7]
            
#             profile.append(True)
#         else:
#             profile.append(False)
#             profile.append(True)
#         counter = counter + 1
#     return profile

# ######## IN EDIT ########


# #### IN EDIT ####

# def createCRSplitProfiles(survey_timeseries, ConditionRatingIndex):
#     split_profiles = []
#     for record in survey_timeseries:
#         temp = []
#         for ages in record[ConditionRatingIndex]:
#             temp.append(createCProfile(ConditionRatings))
#         split_profiles.append(temp)
#     return split_profiles

# #### IN EDIT #####


def splitBackward(survey_timeseries, split_profiles):
    final_records = []
    for record, profile in zip(survey_timeseries,split_profiles):
        length_of_subrecords = len(record[1])
        survey_records = []
        survey_records.append(record[0])
        for col in record[1:]: 
            cols_temp = []
            for i in range(0,length_of_subrecords):
                for j in (utilitySplitBridgeRecords(col[i],profile[i])):
                    cols_temp.append(j)

            survey_records.append(cols_temp)
        final_records.append(survey_records)
    return final_records



################################### SLOPES ##########################################################
def computeSlope(AgeFlatList,subsRatingsFlatList):
    """ compute slope of the bridge from its condition rating and age"""
    ## the code goes here
    Slopes = []
    averageSlopes = []
    temp = []

    ## Note subs  = ConditionRatings
    for age, subs in zip(AgeFlatList, subsRatingsFlatList):
        j = 0
        first_pointer = 0
        second_pointer = 1
        temp_1 = []
        finalList = []
        intervention = []
        for i in range(0,len(subs)):
            if second_pointer < len(subs): 
                # if the first pointer Condition Ratings is less that the second Condition Rating number
                if subs[first_pointer] <  subs[second_pointer]:
                    ## split points
        #             print(conditionRating[first_pointer])
                    temp.append(subs[first_pointer])
                    finalList.append(temp_1)
                    temp_1 = []
                    #print(from_to_matrix[str(conditionRating[first_pointer])+'-'+str(conditionRating[second_pointer])])
                    #intervention.append(from_to_matrix[str(subs[first_pointer])+'-'+str(subs[second_pointer])])

                else:
                    temp_1.append(subs[first_pointer])

                first_pointer = first_pointer + 1
                second_pointer = second_pointer + 1

            else:

                temp_1.append(subs[first_pointer])

                finalList.append(temp_1)

        slopes_of_the_bridges = []
        for rating in finalList:
            if len(rating) != 0:
                try:
                    slopes_of_the_bridges.append(((int(rating[-1]) - int(rating[0])) / len(rating))*len(rating))
                except:
                    pass
            else:
                pass
        #print(slopes_of_the_bridges)
        count = 0
        for i in finalList:
            for j in i:
                count = count + 1
        Slopes.append(sum(slopes_of_the_bridges) / count)
    return Slopes



############################## COMPUTATION OF BASELINE DIFFERENCE SCORE ########################

def getListOfAvgs(AgeFlatList, subsRatingsFlatList):
    """ returns average condition rating of the bridges at a age"""
    sum_by_age = {}
    counts_of_aba = {}
    
    for i in range(0,150,1):
        sum_by_age[i] = 0
        counts_of_aba[i] = 0


    for i,j in zip(subsRatingsFlatList,AgeFlatList):
        for rating, age in zip(i,j):
            try:
                counts_of_aba[age]= counts_of_aba[age] + 1
                sum_by_age[age] = sum_by_age[int(age)] + int(rating)
            except:
                pass

    list_of_avgs = [sums/count for sums, count in zip(sum_by_age.values(), counts_of_aba.values()) if count !=0 ]
    ages = [age for age in range(1,101,1)]
    dict_of_avgs = {age:avg for age, avg in zip(ages,list_of_avgs)}
    return list_of_avgs, dict_of_avgs, counts_of_aba


def computeBaselineScore(ages, condition_ratings, dict_of_avgs):
    """Computation of Baseline Score"""
   
    
    scores_temp = []
    for ratings, age in zip(condition_ratings, ages):
        temp_list = []
        for rating, a in zip(ratings,age):
            try:
                temp_list.append(int(rating) -  dict_of_avgs[a])
            except:
                pass
        scores_temp.append(temp_list)
    return scores_temp

#def computeSlope(AgeFlatList,subsRatingsFlatList):
#    """ compute slope of the bridge from its condition rating and age"""
#    Slopes = []
#    ## Note subs  = ConditionRatings
#    for age, subs in zip(AgeFlatList, subsRatingsFlatList):
#        #j = 0
#        first_pointer = 0
#        second_pointer = 1
#        temp_1 = []
#        finalList = []
#        ages = []
#        age_temp = []
#        
#        for i in range(0,len(subs)):
#            if second_pointer < len(subs): 
#                # if the first pointer Condition Ratings is less that the second Condition Rating number
#                if subs[first_pointer] <  subs[second_pointer]:
#                    ## split points
#                    # temp.append(subs[first_pointer])
# 
