"""
title: This file contains functions that integrate
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


def to_csv(listOfNewRecords, csvfile, fieldnames):
    with open(csvfile, 'w') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=',')
        csvWriter.writerow(fieldnames)
        for record in listOfNewRecords:
            csvWriter.writerow(record)
    return True


def calc_bds_cat(newRecords):
    bsdScores = [rec[-1] for rec in newRecords]
    listOfCat = list()
    tempScores = list()

    for score in bsdScores:
        try:
            tempScores.append(float(score))
        except:
            tempScores.append(None)

    mean = np.mean(list(filter(None, tempScores)))
    std = np.std(list(filter(None, tempScores)))

    for rec, score in zip(newRecords, tempScores):
        if score != None:
            if score > (mean + std):
                rec.append('Good')
            elif score > (mean - std):
                rec.append('Bad')
            else:
                rec.append('Average')
        else:
            rec.append(None)
        listOfCat.append(rec)
    return listOfCat


def fetch_BSD_score(listOfBSDRecords):
    bridgeBDSDict = defaultdict()
    for record in listOfBSDRecords:
        structNum = record.StructureNumber[:-2]
        bsdScore = record.BaselineDifferenceScore
        bridgeBDSDict[structNum] = bsdScore
    return bridgeBDSDict


def update_record(listOfNDOTRecords, bridgeBDSDict):
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
    csvNewFile = 'intervention_bds.csv'

    listOfNDOTRecords = read_csv(path, csvNDOTFile)
    listOfBSDRecords = read_csv(path, csvBSDFile)

    bridgeBDSDict = fetch_BSD_score(listOfBSDRecords)
    newRecords = update_record(listOfNDOTRecords, bridgeBDSDict)
    newRecords = calc_bds_cat(newRecords)

    fieldnames = ['structureNumber', 'intervention', 'score', 'category']
    csvWrite = to_csv(newRecords, csvNewFile, fieldnames)


if __name__=='__main__':
    main()
