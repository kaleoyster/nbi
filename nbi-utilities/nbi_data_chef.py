""" -------------------------------------------------
description: functions to query NBI mongodb
author: Akshay Kale
Data: Nov 28, 2020
-------------------------------------------------"""

__author__ = 'Akshay Kale'
__copyright__ = 'GPL'
__email__ = 'akale@unomaha.edu'

import json
import csv
import numpy as np
import pandas as pd
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

def fix_coordinates(records):
    """
    description:  return the flatten coordinates
    longitude and latitude
    args: records (list of dictionaries)
    return: newRecords (list of new records)
    """
    newRecords = []
    for record in records:
        tempDictionary = {}
        for key, value in zip(record.keys(), record.values()):
            tempDictionary[key] = value
            if key == "coordinates":
                longitude, latitude = value
                tempDictionary['longitude'] = longitude
                tempDictionary['latitude'] = latitude
        newRecords.append(tempDictionary)
    return newRecords

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
    # instantiate empty encoding
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

def create_map(groupedRecords, column='deckBDSScore'):
    """
    Description:
    Args:
    Returns:
    """
    columnMap = defaultdict()
    for structureNum, values in zip(groupedRecords.keys(),
                                    groupedRecords.values()):
        columnMap[structureNum] = values[column]
    return columnMap

def grouped_to_csv(records, name):
    # TODO
    """
    Description:
        This function listify the existing grouped records
    TODO:
            Does not work!
    Args:
        records
        name
    Returns:
    """
    listOfRecords = list()
    keys = records.keys()
    values = records.values()
    dictionary = defaultdict(list)
    for key, value in zip(keys, values):
        for column, val in zip(value.keys(),
                                 value.values()):
            if column != '_id':
                for valInt in list(val):
                    dictionary[column].append(val)
    df = pd.Dataframe(data=dictionary)
    df.to_csv(name, index=False)

def integrate_ext_dataset(extDict,
                          groupedRecords,
                          fieldname):
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
            # Uncomment the below line to maintain a list of records
            # encoding[fieldname].append(extDict.get(structureNumber))
            encoding[fieldname] = extDict.get(structureNumber)
        groupedRecords[structureNumber] = encoding
    return groupedRecords

def integrate_ext_dataset_list(extDict,
                               groupedRecords,
                               fieldname):
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
    #        # encoding[fieldname].append(extDict.get(structureNumber))
    #        encoding[fieldname] = extDict.get(structureNumber)
    #    groupedRecords[structureNumber] = encoding
    return newGroupedRecords

def divide_record_utility(fields,
                          record,
                          startIndex,
                          endIndex):
    """
    Description:
        A utility function to
        divide the timeline of the records

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

def create_individual_records(grouped_records):
    """
    Description:
        create a list of individual
        records from a dictionary
    args: grouped_records(dict)
    return: individual_records (list)
    """
    individual_records = []
    for key, value in grouped_records.items():
        total_len = len(value['structureNumber'])
        structure_numbers = [key]*total_len
        # Error checking here
        temp_val = defaultdict()
        for v_key, v_val in value.items():
            if len(v_val) != total_len:
                temp_val[v_key] = ['None']*total_len
            else:
                temp_val[v_key] = v_val
        temp_df = pd.DataFrame(temp_val)
        temp_df['structureNumberSegement'] = structure_numbers
        individual_records.append(temp_df)
    individual_records = pd.concat(individual_records)
    individual_records = [individual_records.columns.values.tolist()] \
                      + individual_records.values.tolist()
    return individual_records

def divide_grouped_records(groupedRecords,
                           fields,
                           fr,
                           to):
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

def segmentize_index_utility(conditionRatings):
    """
    Description:
        returns segments of condition ratings,
        by identifying the increase in subsequent
        condition ratings
    Returns:
        return indexes to segment further data
    """
    listOfSegments = list()
    indexes = list()
    for index in range(0, len(conditionRatings)-1):
        if conditionRatings[index] < conditionRatings[index + 1]:
            listOfSegments.append(conditionRatings[index])
            indexes.append(index)
        else:
            listOfSegments = list()
            listOfSegments.append(conditionRatings[index])
    return indexes

def segmentize_column(data, indexes):
    """
    Description:
        return the segmented data by the column
    Return:
        segmentedData (list)
    """
    segmentedData = list()
    startP = 0
    if len(indexes) != 0:
        for indx in indexes:
            tempList = list()
            endP = indx + 1
            segment = data[startP:endP]
            remainder = data[endP:]
            startP = endP
            segmentedData.append(segment)
        segmentedData.append(remainder)
    else:
        segmentedData.append(data)
    return segmentedData

def segmentize(groupedRecords, component="deck"):
    """
    Description:
        Return the records by segmenting them into several parts
        marked by the improvement in the conditin ratings
    Args:
        groupedRecords
    Returns:
        return new Record
    """
    updatedGroupedRecords = defaultdict()
    for structureNum, record in zip(groupedRecords.keys(),
                                    groupedRecords.values()):
        newRecord = defaultdict()
        # TODO: May be we don't have condition ratings
        # create a condition that calculates the following step
        # only for the condition ratings
        conditionRatings = record[component]
        indexes = list()
        indexes = segmentize_index_utility(conditionRatings)
        for key, col in zip(record.keys(),
                            record.values()):
            if len(col) > 0 or len(indexes) != 0:
                segmentedData = segmentize_column(col, indexes)
            else:
                segmentedData = col
            newRecord[key] = segmentedData
        updatedGroupedRecords[structureNum] = newRecord
    return updatedGroupedRecords

def reorganize_segmented_data(grouped_records):
    """
    Description:
        Returns a dictionary, that contains seperate
    records for each identified segments.

    Args:
        grouped_records

    returns:
        updated_grouped_records
    """
    updated_grouped_records = defaultdict()
    for record in grouped_records.items():
        structure_no, val_dict = record
        total_segments = len(val_dict['structureNumber'])
        new_structure_numbers = []
        for segment in range(0, total_segments):
            new_structure_no = structure_no \
                            + '_' \
                            + str(segment + 1)
            updated_grouped_records[new_structure_no] = defaultdict()
            new_structure_numbers.append(new_structure_no)

        for col, values in val_dict.items():
            val_length = len(values)
            key_length = len(new_structure_numbers)
            if val_length == key_length:
                for index in range(val_length):
                    value = values[index]
                    struct_no = new_structure_numbers[index]
                    temp_dict = updated_grouped_records[struct_no]
                    temp_dict[col] = value
                    updated_grouped_records[struct_no] = temp_dict
    return updated_grouped_records

def compute_intervention_utility(conditionRatings, interventionMap):
    """
    Description:
        A utility function for computing possible intervention
    by taking into consideration changes in condition rating.
        The function implemented is based on
        Bridge Intervention Matrix by Tariq et al.

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

def compute_intervention(groupedRecords,
                         interventionMap,
                         component='deck'):
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

def compute_intervention_deck(groupedRecords,
                              interventionMap,
                              component='deck 2'):
    """
    What is the difference between the compute intervention deck
    and compute intervention?
    """
    updatedGroupedRecords = defaultdict()
    for key, groupedRecord in zip(groupedRecords.keys(), groupedRecords.values()):
       conditionRatings = groupedRecord[component]
       interventions, number = compute_intervention_utility(conditionRatings, interventionMap)
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
    Description:
        A utility function for computing a score possible
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
        component (string)

    Returns:
        updatedGroupedRecords (list)
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
    return updatedGroupedRecords

def convert_to_int(listOfStrings):
    """
    Description:
            For each of the list of strings, convert each
            item into list of integer
    """
    listOfInteger = list()
    for listOfItems in listOfStrings:
        for items in listOfItems:
            for item in items:
                try:
                    item = int(item)
                    listOfInteger.append(item)
                except:
                    listOfInteger.append(np.nan)
    return listOfInteger

def compute_bds_utility(listOfAges, listOfConditionRatings):
    """
    Description:
        Return the a list of averages arranged by the age
    """
    ageConditionRatings = defaultdict(list)
    baseline = defaultdict()
    baselineDifferenceScores = list()

    # Computation of baseline
    for ages, conditionRatings in zip(listOfAges,
                                      listOfConditionRatings):
        for age, rating in zip(ages, conditionRatings):
            ageConditionRatings[age].append(rating)

    maxAge = np.max(list(ageConditionRatings.keys()))
    for index in range(maxAge):
        values = ageConditionRatings.get(index)
        if values != None:
            try:
                baseline[index] = np.nanmean(values)
            except:
                baseline[index] = np.nan

    # Computation of baseline difference score
    for ages, conditionRatings in zip(listOfAges,
                                      listOfConditionRatings):
        differences = list()
        for age, conditionRating in zip(ages,
                                        conditionRatings):
            try:
                difference = conditionRating - baseline.get(age)
                differences.append(difference)
            except:
                differences.append(np.nan)
        score = np.nanmean(differences)
        baselineDifferenceScores.append(score)

    return baseline, baselineDifferenceScores

def compute_bds_score(groupedRecords, component='deck'):
    """
    Description:
        For each of the records split
        the condition ratings into monotonously
        decreasing segements, by age,
        and ompute baseline difference score.

    Args:
        groupedRecords(dictionary)

    Returns:
        coponents (string)
    """
    componentName = component + 'BDSScore'
    updatedGroupedRecords = defaultdict()

    listOfAges = list()
    listOfConditionRatings = list()

    for key, groupedRecord in zip(groupedRecords.keys(),
                                  groupedRecords.values()):
        conditionRatings = groupedRecord[component]
        ages = compute_age(groupedRecord['yearBuilt'],
                           groupedRecord['year'])

        # Convert string to integer
        conditionRatingsInt = convert_to_int(conditionRatings)
        listOfAges.append(ages)
        listOfConditionRatings.append(conditionRatingsInt)

    baseline, bds = compute_bds_utility(listOfAges, listOfConditionRatings)

    # Compute Baseline Difference Score
    for key, groupedRecord in zip(groupedRecords.keys(),
                                  groupedRecords.values()):

        differences = list()
        conditionRatings = groupedRecord[component]
        conditionRatingsInt = convert_to_int(conditionRatings)
        ages = compute_age(groupedRecord['yearBuilt'],
                           groupedRecord['year'])
        for age, conditionRating in zip(ages,
                                        conditionRatingsInt):
            try:
                difference = conditionRating - baseline.get(age)
                differences.append(difference)
            except:
                differences.append(np.nan)
        score = np.nanmean(differences)
        groupedRecord[componentName] = score
        updatedGroupedRecords[key] = groupedRecord
        #print("Printing the average score: ", updatedGroupedRecords)
    return updatedGroupedRecords, baseline

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

def remove_records(individualRecords,
                   yearFirst,
                   yearSecond):
    """
    Description:
        Remove dictionary in the records that fall between
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
    # TODO:
        # Not all the fields are covered in the redudant fields
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
    for key, value in zip(groupedRecords.keys(),
                          groupedRecords.values()):
        years = value['year']
        if years[0] == initYear:
            # Replace the year with from variable
            structureNumber = key
            deteriorationScore = value[column]
            dictionary[structureNumber] = deteriorationScore
    return dictionary


def tocsv(groupedRecords, csvfile, header=None):
    """
    Description:
        Given header create a csv file out
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
              'deteriorationScore',
              'deckBDSScore'
             ]

    with open(csvfile,'w') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=",")
        csvWriter.writerow(header)
        for record in groupedRecords:
            temp = list()
            for field in header:
                temp.append(record[field])
            csvWriter.writerow(temp)


def create_df(bDeck, bSubstructure, bSuperstructure):
    """
    Description:
        Given the dictionaries
    """
    df = pd.DataFrame()
    age = bDeck.keys()
    df['age'] = age
    df['deck'] = df['age'].map(bDeck)
    df['substructure'] = df['age'].map(bSubstructure)
    df['superstructure'] = df['age'].map(bSuperstructure)
    df.to_csv("baselines.csv", index=False)

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

def main():
    conditionRatings = ['6','6','6','6']
    segmentize_index_utility(conditionRatings)

