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
    """
    description:
    args:
    return:
    """
    listOfRecords = list()
    with open(csvfilename, 'r') as csvfile:
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            listOfRecords.append(row[0])
        return listOfRecords


def read_nbi_records(csvfilename):
    """
    description:
    args:
    return:
    """
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
    """
    description:
    args:
    return:
    """
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
    """
    description:
    args:
    return:
    """

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

    ##False Positive and false negatives
    bothFalsePositive = 'bFP.csv'
    bothFalseNegative = 'bFN.csv'
    bothTruePositive ='bTP.csv'
    bothTrueNegative ='bTN.csv'

    nbiFile = 'nebraska1992-2019.csv'

    # Read structure Number
    rfList = read_structure_numbers(rfBridges)
    rfNList = read_structure_numbers(rfNBridges)

    flList = read_structure_numbers(flBridges)
    flNList = read_structure_numbers(flNBridges)

    # read structure of false positive and negative
    bFNList = read_structure_numbers(bothFalseNegative)
    bFPList = read_structure_numbers(bothFalsePositive)
    bTPList = read_structure_numbers(bothTruePositive)
    bTNList = read_structure_numbers(bothTrueNegative)

    # read nbi records
    nbiList = read_nbi_records(nbiFile)

    # gather structure number
    structNumbers =  list()
    for nbiRecord in nbiList:
        structNumber = nbiRecord.structureNumber
        structNumbers.append(structNumber)

    # create dictionary of structure numbers
    nbiDict = defaultdict()
    for structNumber, nbiRecord in zip(structNumbers, nbiList):
        nbiDict[structNumber] = nbiRecord

    rfBridgeRecords = list()
    rfNBridgeRecords = list()
    flowBridgeRecords = list()
    flowNBridgeRecords = list()

    bFNRecords = list()
    bFPRecords = list()
    bTNRecords = list()
    bTPRecords = list()

    for structNum in rfList:
        rfBridgeRecords.append(nbiDict.get(structNum))

    for structNum in rfNList:
        rfNBridgeRecords.append(nbiDict.get(structNum))

    for structNum in flList:
        flowBridgeRecords.append(nbiDict.get(structNum))

    for structNum in flNList:
        flowNBridgeRecords.append(nbiDict.get(structNum))

    # False Positive and False Negative
    for structNum in bFNList:
        bFNRecords.append(nbiDict.get(structNum))

    for structNum in bFPList:
        bFPRecords.append(nbiDict.get(structNum))

    for structNum in bTPList:
        bTPRecords.append(nbiDict.get(structNum))

    for structNum in bTNList:
        bTNRecords.append(nbiDict.get(structNum))

    # Average random forest age, adt, adtt, year of resconstruction
    outputRf = record_summary(rfBridgeRecords)
    to_csv(outputRf, 'TrueRfFalseFl.csv')

    outputRfN = record_summary(rfNBridgeRecords)
    to_csv(outputRfN, 'TrueRfNFalseFlN.csv')

    outputFlow = record_summary(flowBridgeRecords)
    to_csv(outputFlow, 'TrueFlFalseRf.csv')

    outputFlowN = record_summary(flowNBridgeRecords)
    to_csv(outputFlowN, 'TrueFlNFalseRfN.csv')

    outputbFN = record_summary(bFNRecords)
    to_csv(outputbFN, 'bFNRecords.csv')

    outputbFP = record_summary(bFPRecords)
    to_csv(outputbFP, 'bFPRecords.csv')

    outputbTP = record_summary(bTPRecords)
    to_csv(outputbTP, 'bTPRecords.csv')

    outputbTN = record_summary(bTNRecords)
    to_csv(outputbTN, 'bTNRecords.csv')

if __name__== "__main__":
    main()


