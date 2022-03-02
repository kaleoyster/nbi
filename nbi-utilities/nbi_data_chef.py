""" -------------------------------------------------
description: functions to query NBI mongodb
author: Akshay Kale
Data: Nov 28, 2020
-------------------------------------------------"""

__author__ = 'Akshay Kale'
__copyright__ = 'GPL'
__email__ = 'akale@unomaha.edu'

import json
import numpy as np
from pymongo import MongoClient
from tqdm import tqdm
from datetime import date
from collections import defaultdict
from collections import Counter
#from precipitation import *
#from snowfall_freezethaw import *

def get_db():
    file = open("dbConnect.txt", 'r')
    dbConnectionString = str(file.read()).strip()
    client = MongoClient(dbConnectionString)
    db = client.bridge
    return db

def query(fields, states, years, collection):
    """
    description: query mongodb and collects result
    args:
        fields (dictionary)
        states (list)
        years (list)
    returns:
        results (list of json)
    """
    results = list()
    for year in tqdm(years, desc='Querying NBI DB'):
        for state in states:
            pipeline = [{"$match":{"$and":[
                {"year": year},
                {"stateCode":state}
            ]}},
                {"$project":fields}
            ]
            stateResults = collection.aggregate(pipeline)
            for result in stateResults:
                results.append(result)
    return results

def save_json(results, filename):
    #TODO
    with open(filename, 'w') as jsonFile:
        for result in tqdm(results, desc='Saving JSON in file'):
            #json.dump(result, jsonFile)
            jsonFile.write(json.dumps(result))

def read_json(filename):
    # TODO
    #listOfJson = list()
    listOfJson = json.load(filename)
    return listOfJson

def generate_encoding(keys):
    """
    Description: function to create empty dictionary
    with with empty list
    Args:
        keys (list):
    Returns:
        encoding (dictionary):
    """
    encoding = defaultdict(list)
    for key in keys:
        encoding[key] = []
    return encoding

def update_encoding(record, encoding):
    """
    Description: A utility function for group records
    Args:
        records (dictionary)
        encoding (empty dictionary)

    Returns:
        encoding (filled dictionary)
    """
    for key, value in zip(record.keys(), record.values()):
        encoding[key].append(value)
    return encoding

def group_records(records, fields):
    """
    Description:
    Args:
    Returns:
    """
    # instantiate  empty encoding
    keys = fields.keys()
    grouped_json = defaultdict()
    for record in records:
        groupKey = record['structureNumber']
        encoding = grouped_json.get(groupKey)
        if encoding == None:
            encoding = generate_encoding(keys)
        updatedEncoding =  update_encoding(record, encoding)
        grouped_json[groupKey] = updatedEncoding
    return grouped_json

def integrate_ext_dataset(extDict, groupedRecords, fieldname):
    """
    Description: integrate new columns to the existing group records
    Args:
        extDict (dictionary)
        groupedRecords (dictionary)
        fieldname (string)

    Return:
        groupedRecords (dictionary): An updated grouped records
    """
    for structureNumber in groupedRecords.keys():
        encoding = groupedRecords.get(structureNumber)
        if encoding != None:
            # Uncomment the below line to maintain a list of record
            #encoding[fieldname].append(extDict.get(structureNumber))
            encoding[fieldname] = extDict.get(structureNumber)
        groupedRecords[structureNumber] = encoding
    return groupedRecords

def integrate_ext_dataset_list(extDict, groupedRecords, fieldname):
    """
    Description: integrate new columns to the existing group records
    Args:
        extDict (dictionary)
        groupedRecords (dictionary)
        fieldname (string)

    Return:
        groupedRecords (dictionary): An updated grouped records
    """
    newGroupedRecords = list()
    for record in groupedRecords:
        structureNumber = record.get('structureNumber')
        record[fieldname] = extDict.get(structureNumber)
        newGroupedRecords.append(record)
    #for structureNumber in groupedRecords.keys():
    #    encoding = groupedRecords.get(structureNumber)
    #    if encoding != None:
    #        # uncomment the below line to maintain a list of record
    #        #encoding[fieldname].append(extDict.get(structureNumber))
    #        encoding[fieldname] = extDict.get(structureNumber)
    #    groupedRecords[structureNumber] = encoding
    return newGroupedRecords

def divide_record_utility(fields, record, startIndex, endIndex):
    """
    Description: A utility function to divide the timeline of the records
    Args:
        fields:
        record:
        startIndex:
        endIndex:
    Return:
        records
    """
    # newRecord = defaultdict(list)
    for field in record.keys():
        if field != '_id':
            if field in fields:
                value = record[field]
                value = value[startIndex:endIndex]
                # update:
                record[field] = value
        else:
            value = record[field]
            # update:
            record[field] = value
        #record[field] = value
    # Need to fix this line
    record['deck 2'] = record['deck'][endIndex-1:]
    return record

def divide_grouped_records(groupedRecords, fields, fr, to):
    """
    Description:
        The function divides the timeline of the
    bridge life cycle, defined by fr (year) and to (year)

    Args:
        groupedRecords (list of json format)
        fields (json format)
        fr (string)
        to (string)

    Returns:
       updatedRecords (dictionary)
    """
    updatedRecords = defaultdict()
    for key, groupRecord in zip(groupedRecords.keys(), groupedRecords.values()):
        year = groupRecord['year']
        try:
            startIndex = year.index(fr)
        except:
            startIndex = 0
        try:
            endIndex = year.index(to)
            endIndex = endIndex + 1
        except:
            endIndex = len(year)
        updatedFields = divide_record_utility(fields, groupRecord, startIndex, endIndex)
        updatedRecords[key] = updatedFields
    return updatedRecords

def compute_intervention_utility(conditionRatings, interventionMap):
    """
    Description:
        A utility function for computing possible intervention
    by taking into consideration changes in condition rating. The function implemented is based on Bridge Intervention Matrix by Tariq et al.

    Note:
         Check for the representation of condition ratings.
         Often the condition ratings are defined as a string,
         Then, these condition rating have to be transformed into interger
    Args:
        conditionRatings (list)
        interventionMap (dictionary)

    Returns:
        interventions (list)
        count (int)
    """
    i = 0
    interventions = list()
    interventions.append(None)
    for i in range(len(conditionRatings)-1):
       j = i + 1
       interv = interventionMap.get((conditionRatings[i], conditionRatings[j]))
       interventions.append(interv)
    count = len([count for count in interventions if count !=None ])
    return interventions, count

def compute_intervention(groupedRecords, interventionMap, component='deck'):
    """
    Description:
    Args:
    Returns:
    """
    updatedGroupedRecords = defaultdict()
    labelIntervention = component + 'Intervention'
    labelNum = component + 'NumberOfInterventions'
    for key, groupedRecord in zip(groupedRecords.keys(), groupedRecords.values()):
       conditionRatings = groupedRecord[component]
       interventions, number = compute_intervention_utility(conditionRatings,
                                                            interventionMap)
       groupedRecord[labelIntervention] = interventions
       groupedRecord[labelNum] = number
       updatedGroupedRecords[key] = groupedRecord
    return updatedGroupedRecords

def compute_intervention_deck(groupedRecords, interventionMap, component='deck 2'):
    """
    What is the difference between the compute intervention deck
    and compute intervention?
    """
    updatedGroupedRecords = defaultdict()
    for key, groupedRecord in zip(groupedRecords.keys(), groupedRecords.values()):
       conditionRatings = groupedRecord[component]
       interventions, number = compute_intervention_utility(conditionRatings,
                                                            interventionMap)
       groupedRecord['futureInterventions'] = interventions
       groupedRecord['numberFutureOfInterventions'] = number
       updatedGroupedRecords[key] = groupedRecord
    return updatedGroupedRecords


def split_condition_ratings(conditionRatings, ages):
    """
    Description: A utility function for computing possible
    monotonous deteriorating condition ratings.
    The splitting criteria is condition ratings

    Args:
        conditionRatings (list)
        ages (dictionary)

    Returns:
        splitConditionRatings (list)
        splitAges (list)
    """
    splitConditionRatings = list()
    tempConditionRatings = list()

    splitAges = list()
    tempAges = list()
    for rating, age in zip(conditionRatings, ages):
        if rating not in ['N', 'NA', '']:
            if len(tempConditionRatings) == 0:
                tempConditionRatings.append(int(rating))
                tempAges.append(int(age))

            elif tempConditionRatings[-1] >= int(rating):
                tempConditionRatings.append(int(rating))
                tempAges.append(int(age))
            else:
                splitConditionRatings.append(tempConditionRatings)
                tempConditionRatings = list()
                tempConditionRatings.append(int(rating))

                splitAges.append(tempAges)
                tempAges = list()
                tempAges.append(int(age))

    splitConditionRatings.append(tempConditionRatings)
    splitAges.append(tempAges)

    return splitConditionRatings, splitAges

def compute_age(yearBuilts, years):
    """
    Description: compute ages from the list of yearBuilt

    Args:
        years (list)

    Returns:
        ages (list)
    """
    ages = list()
    for year, yearBuilt in zip(years, yearBuilts):
        age = int(year) - int(yearBuilt)
        ages.append(age)
    return ages

def compute_det_score_utility(splitConditionRatings, splitAges):
    """
    Description: A utility function for computing possible
    monotonous deteriorating condition ratings.

    Args:
        splitConditionRatings (list)
        splitAges (dictionary)

    Returns:
        averageScore (int)
    """
    scores = list()
    for conditionRatings, ages in zip(splitConditionRatings, splitAges):
        if len(conditionRatings) > 1:
            firstConditionRating = conditionRatings[0]
            lastConditionRating = conditionRatings[-1]

            firstAge = ages[0]
            lastAge = ages[-1]

            try:
                slope = (lastConditionRating - firstConditionRating) \
                     /  (lastAge - firstAge)
            except:
                # To avoid division by zero
                slope = 0
            #print("\n first age and conditionRating: ", firstAge, firstConditionRating)
            #print("\n last age and conditionRating: ", lastAge, lastConditionRating)
            #print("\n printing slope :", slope)
            scores.append(slope)

    if len(scores) > 0:
        averageScore = np.mean(scores)
    else:
       averageScore = 0

    return averageScore

def compute_deterioration_slope(groupedRecords, component='deck'):
    """
    Description: For each of the records split the condition ratings
        into monotonously decreasing segements, by age
        Compute average deterioration slope or score for each segement

    Args:
        groupedRecords(dictionary)

    Returns:
        coponents (string)
    """
    componentName = component + 'DeteriorationScore'
    updatedGroupedRecords = defaultdict()

    # Key:  structure number of the bridges
    # groupedRecords: json format bridges records (timeseries) 
    for key, groupedRecord in zip(groupedRecords.keys(), groupedRecords.values()):
        conditionRatings = groupedRecord[component]
        ages = compute_age(groupedRecord['yearBuilt'], groupedRecord['year'])
        splitConditionRatings, splitAges = split_condition_ratings(conditionRatings, ages)
        averageScore = compute_det_score_utility(splitConditionRatings, splitAges)
        groupedRecord[componentName] = averageScore
        updatedGroupedRecords[key] = groupedRecord
        # print("Printing the average score: ", updatedGroupedRecords)
    return updatedGroupedRecords

def convert_to_int(listOfStrings):
    """
    Description:
            For each of the list of strings, convert each
            item into list of integer
    """
    listOfInteger = list()
    for listOfItems in listOfStrings:
        for item in listOfItems:
            try:
                item = int(item)
                listOfInteger.append(item)
            except:
                listOfInteger.append(np.nan)
    return listOfInteger

def compute_bds_score(groupedRecords, component='deck'):
    """
    Description:
        For each of the records split the condition ratings into monotonously decreasing segements, by age, and ompute baseline difference score.

    Args:
        groupedRecords(dictionary)

    Returns:
        coponents (string)
    """
    componentName = component + 'BDSScore'
    updatedGroupedRecords = defaultdict()

    print("Printing the number of the condition ratings", len(groupedRecords))
    # Key:  structure number of the bridges
    # groupedRecords: json format bridges records (timeseries) 
    for key, groupedRecord in zip(groupedRecords.keys(), groupedRecords.values()):
        conditionRatings = groupedRecord[component]
        ages = compute_age(groupedRecord['yearBuilt'], groupedRecord['year'])

        # Compute baseline
        # Convert condition rating 

        conditionRatingsR = convert_to_int(conditionRatings)
        print(ages, conditionRatings)
        print(ages, conditionRatingsR)
        print("-----"*8)
        #print(ages, conditionRatings)
        #splitConditionRatings, splitAges = split_condition_ratings(conditionRatings,
        #                                                           ages)
        #averageScore = compute_det_score_utility(splitConditionRatings,
        #                                         splitAges)
        #groupedRecord[componentName] = averageScore
        #updatedGroupedRecords[key] = groupedRecord
        # print("Printing the average score: ", updatedGroupedRecords)
    return updatedGroupedRecords

def clean_individual_records(records):
    """
    Should be named convert dictionary into list

    Description: Convert list of dictionaries to
        individual lists for records and header.

    Args:
        records (list): A list of dictionaries

    Returns:
        cleanedRecord
    """
    cleanedRecords = list()
    for record in records:
        header = list(record.keys())
        values = list(record.values())
        cleanedRecords.append(values)
    return cleanedRecords, header

def remove_records(individualRecords, yearFirst, yearSecond):
    """
    Description: Remove dictionary in the records that fall between
        yearFirst and yearSecond

    Args:
        individualRecords(list):
        yearFirst (int):
        yearSecond (int):

    Returns:
        individual records(list)
    """
    newIndividualRecords = list()
    for record in individualRecords:
        if record['year'] < (yearFirst):
            newIndividualRecords.append(record)
    return newIndividualRecords


def clean_grouped_records(groupedrecords):
    # todo:
        # not all the fields are covered in the redudant fields
            # try with temp field
            # keep a track of groupedrecords fields
    redundantfields = ['structurenumber',
                       'yearbuilt',
                       'statecode',
                       'countycode',
                       'material',
                       'deck',
                       'substructure',
                       'superstructure',
                       'owner',
                       'structuretype',
                       'wearingsurface',
                       'averagedailytraffic',
                       'avgdailytrucktraffic',
                       'designload',
                       'structurelength',
                       'recordtype',
                       'typeofserviceon',
                       'typeofserviceunder',
                       'precipitation',
                       'snowfall',
                       'freezethaw'
                      ]

    updatedgroupedrecords = list()
    for groupedrecord in groupedrecords.values():
        for field in redundantfields:
            value = groupedrecord.get(field)
            if value == none:
                value = none
            elif value == []:
                value = none
            else:
                value = value[-1]
            groupedrecord[field] = value
        updatedgroupedrecords.append(groupedrecord)
    return updatedgroupedrecords

def create_deterioration_dict(groupedRecords,
                              initYear,
                              column='deckDeteriorationScore'):
    """
    Description: Creates a dictionary of structure number and deterioration
    This function is incomplete, because it contains a lot
    dependency and hard coding

    Args:
    Returns:
    """
    dictionary = defaultdict()
    for key, value in zip(groupedRecords.keys(), groupedRecords.values()):
        years = value['year']
        #print("\n Printing : ", column)
        if years[0] == initYear:
            # Replace the year with from variable
            structureNumber = key
            deteriorationScore = value[column]
            dictionary[structureNumber] = deteriorationScore
    return dictionary


def tocsv(groupedRecords, csvfile, header=None):
    """
    Description: Given header create a csv file out
    of groupedRecords
    """
    header = ['structureNumber',
              'stateCode',
              'countyCode',
              'yearBuilt',
              'owner',
              'designLoad',
              'wearingSurface',
              'material',
              'snowfall',
              'freezethaw',
              'precipitation',
              'structureType',
              'recordType',
              'typeOfServiceOn',
              'typeOfServiceUnder',
              'deck',
              'superstructure',
              'substructure',
              'averageDailyTraffic',
              'avgDailyTruckTraffic',
              'numberOfInterventions',
              'numberFutureOfInterventions',
              'deteriorationScore'
             ]

    with open(csvfile,'w') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=",")
        csvWriter.writerow(header)
        for record in groupedRecords:
            temp = list()
            for field in header:
                temp.append(record[field])
            csvWriter.writerow(temp)


def tocsv_list(groupedRecords, csvfile, header=None):
    """
    Description: Given header create a csv file out
    of groupedRecords
    """
    if header == None:
        header = groupedRecords[0].keys()

    with open(csvfile,'w') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=",")
        csvWriter.writerow(header)
        for record in groupedRecords:
            csvWriter.writerow(record.values())

def sample_records():
    """
    Description: provide a sample records for testing
    """
    temp = [
                 {'year': 1992, 'structureNumber': 'C000100305', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1935, 'averageDailyTraffic': 30, 'designLoad': 0, 'structureLength': 10.1, 'deck': '6', 'superstructure': '7', 'substructure': '5', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 7, 'wearingSurface': 7, 'structureType': 2},
                  {'year': 1993, 'structureNumber': 'C000100305', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1935, 'averageDailyTraffic': 20, 'designLoad': 0, 'structureLength': 7, 'deck': '7', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 1},
                 {'year': 1994, 'structureNumber': 'C000100305', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1935, 'averageDailyTraffic': 20, 'designLoad': 0, 'structureLength': 7, 'deck': '7', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 1},
                {'year': 1995, 'structureNumber': 'C000100305', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1935, 'averageDailyTraffic': 20, 'designLoad': 0, 'structureLength': 7, 'deck': '7', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 1},
                 {'year': 1996, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '5', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 1997, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '5', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 1998, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '5', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2000, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '6', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2001, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '6', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2002, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '6', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2003, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '7', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2004, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '7', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2005, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '7', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2006, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '8', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2007, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '8', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2008, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '8', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2009, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '8', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2010, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '8', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2011, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '7', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2012, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '5', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2013, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '5', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2014, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '5', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2015, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '6', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2016, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '6', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 2017, 'structureNumber': 'C000100405', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1925, 'averageDailyTraffic': 65, 'designLoad': 0, 'structureLength': 9.1, 'deck': '6', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 1, 'wearingSurface': 1, 'structureType': 11},
                 {'year': 1995, 'structureNumber': 'C000100305', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1974, 'averageDailyTraffic': 60, 'designLoad': 4, 'structureLength': 24.7, 'deck': '8', 'superstructure': '7', 'substructure': '8', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 0, 'material': 3, 'wearingSurface': 3, 'structureType': 2},
                 {'year': 1996, 'structureNumber': 'C000100305', 'countyCode': 1, 'owner': 2, 'yearBuilt': 1962, 'averageDailyTraffic': 170, 'designLoad': 2, 'structureLength': 27.4, 'deck': '7', 'superstructure': '7', 'substructure': '7', 'highwaySystemOfInventoryRoute': -1, 'avgDailyTruckTraffic': 10, 'material': 1, 'wearingSurface': 1, 'structureType': 1}
                ]
    return temp
