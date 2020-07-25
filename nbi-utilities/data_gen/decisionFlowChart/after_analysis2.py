"""
description: This file contains functions that integrate
bridge scores to NDOT identified maintenance bridges
author: Akshay Kale
"""

import os
import csv
from collections import defaultdict
from collections import namedtuple
import numpy as np


__author__ = 'Akshay Kale'
__copyright__='GPL'


def read_structure_numbers(csvfilename):
    listOfRecords = list()
    with open(csvfilename, 'r') as csvfile:
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            listOfRecords.append(row[0])
        return listOfRecords


def read_nbi_records(csvfilename):
    listOfRecords = list()
    with open(csvfilename, 'r') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        header = next(csvReader)
        if header[0] == '':
            header[0] = 'id'
        Record = namedtuple('Record', header)
        for row in csvReader:
            record = Record(*row)
            listOfRecords.append(record)
        return listOfRecords


def record_summary(listOfRecords):
    summaryRecords = defaultdict()
    count = 0
    age = defaultdict(int)
    adt = 0
    material = defaultdict(int)

    for record in listOfRecords:
        try:
            year = record.year
            county = record.countyCode
            yearReconstructed = record.yearReconstructed
            deck = record.deck
            adt = record.averageDailyTraffic
            structType = record.structureType
        except:
            pass
    return listOfRecords


def to_csv(output, filename):

    outputNew = list()
    #output = [item._asdict() for item in output]
    for item in output:
        try:
            outputNew.append(item._asdict())
        except:
            outputNew.append(None)

        output = outputNew

        fieldnames = ['year',
                      'stateCode',
                      'structureNumber',
                      'countyCode',
                      'yearBuilt',
                      'averageDailyTraffic',
                      'deck',
                      'yearReconstructed',
                      'avgDailyTruckTraffic',
                      'material',
                      'structureType'
                     ]

        with open(filename, 'w') as csvFile:
            csvWriter = csv.DictWriter(csvFile, delimiter=',', fieldnames=fieldnames)
            csvWriter.writeheader()
            for row in output:
                if row == None:
                    #NoneDict = dict(zip(fieldnames, [None]*len(fieldnames)))
                    #csvWriter.writerow(NoneDict)
                    pass
                else:
                    csvWriter.writerow(row)

def main():
    path = '../../../../data/nbi/'
    os.chdir(path)

    rfBridges = 'bridgesRf.csv'
    rfNBridges = 'bridgesRfNegative.csv'

    flBridges = 'bridgesFl.csv'
    flNBridges = 'bridgesFlNegative.csv'

    nbiFile = 'nebraska1992-2019.csv'

    #######
    rfList = read_structure_numbers(rfBridges)
    rfNList = read_structure_numbers(rfNBridges)

    flList = read_structure_numbers(flBridges)
    flNList = read_structure_numbers(flNBridges)

    nbiList = read_nbi_records(nbiFile)

    structNumbers =  list()
    for nbiRecord in nbiList:
        structNumber = nbiRecord.structureNumber
        structNumbers.append(structNumber)

    nbiDict = defaultdict()
    for structNumber, nbiRecord in zip(structNumbers, nbiList):
        nbiDict[structNumber] = nbiRecord

    rfBridgeRecords = list()
    rfNBridgeRecords = list()

    flowBridgeRecords = list()
    flowNBridgeRecords = list()
    for structNum in rfList:
        rfBridgeRecords.append(nbiDict.get(structNum))

    for structNum in rfNList:
        rfNBridgeRecords.append(nbiDict.get(structNum))

    for structNum in flList:
        flowBridgeRecords.append(nbiDict.get(structNum))

    for structNum in flNList:
        flowNBridgeRecords.append(nbiDict.get(structNum))
    # Average random forest age, adt, adtt, year of resconstruction
    outputRf = record_summary(rfBridgeRecords)
    to_csv(outputRf, 'TrueRfFalseFl.csv')

    outputRfN = record_summary(rfNBridgeRecords)
    to_csv(outputRfN, 'TrueRfNFalseFlN.csv')

    outputFlow = record_summary(flowBridgeRecords)
    to_csv(outputFlow, 'TrueFlFalseRf.csv')

    outputFlowN = record_summary(flowNBridgeRecords)
    to_csv(outputFlowN, 'TrueFlNFalseRfN.csv')

if __name__== "__main__":
    main()


