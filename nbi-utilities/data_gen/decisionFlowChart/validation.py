"""
description: Validation of the decision tree outputs
"""
import csv
import os
from collections import namedtuple
from collections import defaultdict


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


def read_rf_results(csvRfFile):
    listOfRfIntervention = list()
    with open(csvRfFile, 'r') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        header = next(csvReader)
        record = namedtuple('Record', header)
        for row in csvReader:
            rec = record(*row)
            structNum = rec.structureNumber
            intervention = rec.intervention
            listOfRfIntervention.append([structNum, intervention])
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


def main():
    path = '../../../../data/trees/decision-tree-dataset/'
    csvFile = 'decision_tree.csv'
    os.chdir(path)

    pathIntervention = '../../nbi/'
    csvRfFile = 'intervention_bds.csv'

    listOfRecords = read_main_dataset(csvFile)
    os.chdir(pathIntervention)
    listOfRfIntervention = read_rf_results(csvRfFile)
    structDeck, structSub, structSup = create_dict(listOfRecords)
    print(listOfRfIntervention)
    #print(listOfRecords)




if __name__ == '__main__':
    main()

