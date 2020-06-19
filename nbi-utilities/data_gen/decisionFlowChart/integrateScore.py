"""
title: This file contains functions that integrate
bridge scores to NDOT identified maintenance bridges
author: Akshay Kale
"""

import os
import csv
from collections import defaultdict
from collections import namedtuple


__author__ = 'Akshay Kale'
__copyright__='GPL'

def read_csv(path, csvfile):
    listOfRecords = list()
    with open(csvfile, 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        header = next(csvReader)
        if header[0] == '':
            header[0] = 'id'
        header = [col.replace(" ", "") for col in header]
        header = [col.replace(".", "") for col in header]
        Record = namedtuple('Record', header)
        for row in csvReader:
            record = Record(*row)
            listOfRecords.append(record)
    return listOfRecords


def to_csv(listOfNewRecords):
    with open(csvfile, 'w') as csvFile:
        csvWriter = csv.writer()
        csvWriter.writerow(fieldnames)
        for record in listOfNewRecords:
            csvWriter.writerow(record)
    return True


def fetchBSDScore(listOfBSDRecords):
    bridgeBDSDict = defaultdict()
    for record in listOfBSDRecords:
        structNum = record.StructureNumber[:-2]
        bsdScore = record.BaselineDifferenceScore
        bridgeBDSDict[structNum] = bsdScore
    return bridgeBDSDict


def updateRecord(listOfNDOTRecords, bridgeBDSDict):
    structureNumbers = list()
    listOfBDS = list()
    listOfNewRecords = list()

    for record in listOfNDOTRecords:
        structureNumbers.append(record.structureNumber)

    for structNum in structureNumbers:
        bridgeBDS = bridgeBDSDict.get(structNum)
        listOfBDS.append(bridgeBDS)

    for record, bds in zip(listOfNDOTRecords, listOfBDS):
        record = list(record)
        record.append(bds)
        listOfNewRecords.append(record)
    return listOfNewRecords


def main():
    path = '../../../../data/nbi/'
    os.chdir(path)
    csvNDOTFile = 'intervention.csv'
    csvBSDFile = '06-20-19-thesis-dataset_allstates_allstates.csv'
    listOfNDOTRecords = read_csv(path, csvNDOTFile)
    listOfBSDRecords = read_csv(path, csvBSDFile)

    bridgeBDSDict = fetchBSDScore(listOfBSDRecords)
    newRecords = updateRecord(listOfNDOTRecords, bridgeBDSDict)
    print(newRecords)
    #to_csv(newRecords)
    # integrate newRecord with the Yes or No
if __name__=='__main__':
    main()
