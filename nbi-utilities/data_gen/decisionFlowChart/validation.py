"""
description: Validation of the decision tree outputs
"""
import csv
import os
from sklearn.metrics import confusion_matrix, classification_report
from collections import namedtuple
from collections import defaultdict
from collections import Counter

__author__ = 'Akshay Kale'
__copyright__ = 'GPL'

#  Year: 2019 ( output )
#  Requires: 1992 - 2019 dataset to create the timeseries data format  
#  Random Forest:  
#  Decision Trees:
    # Fir the random forest: 
        # For all the bridges in the nebraska:
            # 
def read_main_dataset(csvFile):
    listOfRecords = list()
    with open(csvFile, 'r') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        header = next(csvReader)
        header = [word.replace(" ", "_") for word in header]
        header = ["id" if word == '' else word for word in header]
        header[1] = 'unamed'
        Record = namedtuple('Record', header)
        for row in csvReader:
            record = Record(*row)
            structNum = record.structure_number
            deckInt = record.deck_intervention_in_next_3_years
            subInt = record.sub_intervention_in_next_3_years
            superInt = record.super_intervention_in_next_3_years
            listOfRecords.append([structNum, deckInt, superInt, subInt])
    return listOfRecords


def read_gt_results(csvRfFile):
    listOfRfIntervention = list()
    with open(csvRfFile, 'r') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        header = next(csvReader)
        record = namedtuple('Record', header)
        for row in csvReader:
            rec = record(*row)
            structNum = rec.structureNumber
            intervention = rec.intervention
            rfIntervention =  rec.rfIntervention
            listOfRfIntervention.append([structNum, intervention, rfIntervention])
    return listOfRfIntervention


def create_dict(listOfRecords):
    structDeck = defaultdict()
    structSub = defaultdict()
    structSup = defaultdict()

    for record in listOfRecords:
        struct = record[0]
        deck = record[1]
        sub = record[2]
        sup = record[3]
        structDeck[struct] = deck
        structSub[struct] = sub
        structSup[struct] = sup
    return structDeck, structSub, structSup


def both_correct_positive(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]

    if intervention == 'Yes' and rfResult == 'Yes' and groundTruth == 'Yes':
        return True
    else:
        return False


def rf_correct_positive(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]

    if rfResult == 'No' and groundTruth == 'No':
        return True
    else:
        return False


def rf_incorrect_positive(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]

    if rfResult == 'Yes' and groundTruth == 'No':
        return True
    else:
        return False


def flow_correct_positive(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]
    if intervention == 'Yes' and groundTruth == 'Yes':
        return True
    else:
        return False


def flow_incorrect_positive(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]
    if intervention == 'No' and groundTruth == 'Yes':
        return True
    else:
        return False


def both_incorrect_negative(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]

    if intervention == 'No' and rfResult == 'No' and groundTruth == 'Yes':
        return True
    else:
        return False


def both_correct_negative(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]

    if intervention == 'No' and rfResult == 'No' and groundTruth == 'No':
        return True
    else:
        return False


def count_ground_truth(lists):
    yesList = list()
    noList = list()
    for record in lists:
        yesRecord = record[3]
        if yesRecord == 'Yes':
            yesList.append(record)
        noList.append(record)
    return yesList, noList


def integrate(listOfRfIntervention, structDeck):
    bothPositiveList = list()
    rfCorrectList = list()
    rfIncorrectList = list()
    flowCorrectList = list()
    flowIncorrectList = list()
    bothNegativeList = list()
    for record in listOfRfIntervention:
        structNum = record[0]
        record.append(structDeck.get(structNum))
        # Recoding flow chart intervention
        if record[1][:4] == 'None':
            record[1] = 'No'
        else:
            record[1] = 'Yes'
        # Recoding random forest results
        if record[2] == '':
            record[2] = None
        elif record[2] == 'yes':
            record[2] = 'Yes'
        else:
            record[2] = 'No'

        # Record both positive
        if both_correct_positive(record):
            bothPositiveList.append(record)

        if rf_correct_positive(record):
            rfCorrectList.append(record)

        if flow_correct_positive(record):
            flowCorrectList.append(record)

        if both_incorrect_negative(record):
            bothNegativeList.append(record)

        if rf_incorrect_positive(record):
            rfIncorrectList.append(record)

        if flow_incorrect_positive(record):
            flowIncorrectList.append(record)

        if both_correct_negative(record):
            bothNegativeList.append(record)

    return bothPositiveList, rfCorrectList, rfIncorrectList, flowCorrectList, flowIncorrectList, bothNegativeList



def main():
    path = '../../../../data/trees/decision-tree-dataset/'
    csvFile = 'decision_tree.csv'
    os.chdir(path)

    pathIntervention = '../../nbi/'
    csvGtFile = 'intervention_bds.csv'

    listOfRecords = read_main_dataset(csvFile)
    os.chdir(pathIntervention)
    listOfGtIntervention = read_gt_results(csvGtFile)
    # listOfRecords -  deck, superstructure, substructure
    structDeck, structSub, structSup = create_dict(listOfRecords)

    ## RF intervention
    #Structure Number, Flow Chart, Random Forest, label
    pos, rf, rfi, fl, fli, neg = integrate(listOfGtIntervention, structDeck)
    yes, no = count_ground_truth(listOfGtIntervention)

    # Print results
    print('Number of records with Yes', len(yes))
    print('Number of records with No', len(no))
    print('Number of records with correct Yes', len(pos))
    print('Number of records with correct No', len(neg))
    print('Number of records with correct Flowchart',len(fl))
    print('Number of records with incorrect Flowchart',len(fli))
    print('Number of records with correct Rf', len(rf))
    print('Number of records with incorrect Rf', len(rfi))


if __name__ == '__main__':
    main()

