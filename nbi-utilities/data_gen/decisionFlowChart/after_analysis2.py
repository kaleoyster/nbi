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
            year = record.YEAR_BUILT_027
            deck = record.DECK_COND_058
            adt = record.ADT_029
            structType = record.STRUCTURE_TYPE_043B
            structKind = record.STRUCTURE_KIND_043A
        except:
            pass
    return material, age


def main():
    path = '../../../../data/nbi/'
    os.chdir(path)
    rfBridges = 'bridgesRf.csv'
    flBridges = 'bridgesFl.csv'
    nbiFile = 'nbi.csv'

    rfList = read_structure_numbers(rfBridges)
    flList = read_structure_numbers(flBridges)
    nbiList = read_nbi_records(nbiFile)

    structNumbers =  list()
    for nbiRecord in nbiList:
        structNumber = nbiRecord.STRUCTURE_NUMBER_008
        structNumbers.append(structNumber)

    nbiDict = defaultdict()
    for structNumber, nbiRecord in zip(structNumbers, nbiList):
        nbiDict[structNumber] = nbiRecord

    rfBridgeRecords = list()
    flowBridgeRecords = list()

    for structNum in rfList:
        rfBridgeRecords.append(nbiDict.get(structNum))

    for structNum in flList:
        flowBridgeRecords.append(nbiDict.get(structNum))

    # Average random forest age, adt, adtt, year of resconstruction
    print(record_summary(rfBridgeRecords))
    print(rfBridgeRecords)

if __name__== "__main__":
    main()


