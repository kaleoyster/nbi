"""
description: Validation of the decision tree outputs
"""
import csv
import os
from collections import namedtuple
from collections import defaultdict
from collections import Counter

__author__ = 'Akshay Kale'
__copyrigth__ = 'GPL'


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

def both_positive(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]

    if intervention == 'Yes' and rfResult == 'Yes' and groundTruth == 'Yes':
        return True
    else:
        return False

def rf_correct(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]

    if intervention == 'No' and rfResult == 'Yes' and groundTruth == 'Yes':
        return True
    else:
        return False

def flow_correct(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]

    if intervention == 'Yes' and rfResult == 'No' and groundTruth == 'Yes':
        return True
    else:
        return False


def both_negative(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]

    if intervention == 'No' and rfResult == 'No' and groundTruth == 'Yes':
        return True
    else:
        return False

def integrate(listOfRfIntervention, structDeck):
    bothPositiveList = list()
    rfCorrectList = list()
    flowCorrectList = list()
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
        if both_positive(record):
            bothPositiveList.append(record)

        elif rf_correct(record):
            rfCorrectList.append(record)

        elif flow_correct(record):
            flowCorrectList.append(record)

        elif both_negative(record):
            bothNegativeList.append(record)

        else:
            continue

    return bothPositiveList, rfCorrectList, flowCorrectList, bothNegativeList



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
    #- Structure Number, Flow Chart, Random Forest, label
    #print(listOfGtIntervention)
    pos, rf, fl, neg = integrate(listOfGtIntervention, structDeck)
    print(neg)
    #print(listOfRecords)




if __name__ == '__main__':
    main()

