"""
The scripts provide functions to extract, read, and parse XML files.
"""
import os
import csv
import json
from tqdm import tqdm
import numpy as np
from zipfile import ZipFile
from collections import defaultdict
from collections import namedtuple
import xml.etree.ElementTree as ET

__author__ = 'Akshay Kale'
__copyright_ = 'GPL'
__credit__ =  []
__email__ = 'akale@unomaha.edu'

def readXml(zipFile):
    """
    Description: Function reads xml file from the zipfile,
    and returns a xml object.
    Args:
        zipfile (string)
    Returns:
        xml (xml file object)
    """
    arch = ZipFile(zipFile, 'r')
    zfile = zipFile[-22:]
    xmlfile = zfile[:-3] + 'xml'
    xml = arch.read(xmlfile)
    return xml

def extractXml(directory):
    """
    Description: Extracts XML zip files
    Args:
        directory (string): Path of the xml files
    Returns:
        None
    """
    extension = ".zip"
    for zfile in tqdm(os.listdir(directory), desc='Extracting XML files'):
        if zfile.endswith(extension):
            os.chdir(directory)
            filename = directory + '/' + zfile
            filename = os.path.abspath(zfile)
            zip_ref = ZipFile(filename)
            zip_ref.extractall(directory)
            zip_ref.close()
            os.remove(filename)

def parseXml(directory, structCatDict):
    """
    Description:  Read and parses xml files
    Args:
        directory (string): Path of the xml files
    Returns:
        elementList (List): A List of named tuples
    """
    elementList = list()
    records = list()
    Record = namedtuple('Record', ['year', 'state', 'structure',
                                   'totalQty', 'elementNo',
                                   'cs1', 'cs2', 'cs3', 'cs4',
                                   'perfCat'])

    for xmlfile in tqdm(os.listdir(directory), desc='Parsing XML files'):
        if xmlfile.endswith('.xml'):
            os.chdir(directory)
            tree = ET.parse(xmlfile)
            root = tree.getroot()
            for element in root.findall('FHWAED'):
                year = xmlfile[:4]
                state = element.find('STATE').text
                structure = element.find('STRUCNUM').text
                totalQty = element.find('TOTALQTY').text
                elementNo = element.find('EN').text
                cs1 = element.find('CS1').text
                cs2 = element.find('CS2').text
                cs3 = element.find('CS3').text
                cs4 = element.find('CS4').text
                perfCat = structCatDict.get(structure)
                tempRecord = Record( year,
                                     state,
                                     structure,
                                     totalQty,
                                     elementNo,
                                     cs1,
                                     cs2,
                                     cs3,
                                     cs4,
                                     perfCat)
                elementList.append(tempRecord)
    return elementList

def getBSD(filename):
    """
    Description: Function to read NBI file
         and, extract structurenumber and baseline difference score

    Args:
        filename (string): Path of the xml files
    Returns:
        structBsdDict (dictionary): key (structure number)
                                     value (baseline difference score)
    """
    with open(filename, 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        header = next(csvReader)
        structBsdDict = defaultdict(list)
        for row in tqdm(csvReader, desc='Extracting Bridge Score'):
            structureNumber = row[1][:-2]
            bsd = float(row[-2])
            structBsdDict[structureNumber].append(bsd)
    return structBsdDict

def calcDictMean(structBsdDict):
    """
    Description: Calculates the mean of baseline difference scores

    Args:
        structuBsDict (dictionary): key (structure number)
                                    value (baseline difference score)
    Returns:
        structBsdMeanDict (dictionary): key (structure number)
                                        value (baseline difference score)
    """
    structBsdMeanDict = {key:np.mean(val) for key, val in structBsdDict.items()}
    return structBsdMeanDict

def getCategory(scores):
    """
    Description: Classifys brideges into good, bad, and average
        standard deviation

    Args:
        scores (list): baseline difference score

    Returns:
        conditionCategory (list): baseline difference category
    """
    conditionCategory = list()
    stdDevScore = np.std(scores)
    meanScore = np.mean(scores)

    for score in tqdm(scores, desc='Computing Bridge Perf. Category'):
        if score > (meanScore + stdDevScore):
            conditionCategory.append('Good')
        elif (meanScore - stdDevScore) >= score <= (meanScore + stdDevScore) :
            conditionCategory.append('Average')
        else:
            conditionCategory.append('Bad')
    return conditionCategory

def listOftupleToDict(tups):
    """
    Description: Converts a list of named tuples into a list of dict

    Args:
        elementList (list): A list of named tuples

    Returns:
        listOfDictionary (list)
    """
    listOfDictionary = [dict(tup._asdict()) for tup in tups]
    return listOfDictionary

def toCSV(elementList, path, filename):
    """
    Description: Converts named tuples into a csv file
        and saves a csv file in the provided directory

    Args:
        elementList (list): A list of named tuples
        path (string): path to save the csv file

    Returns:
        None
    """
    filename = '2015-2019_nbe.csv'
    os.chdir(path)
    listOfDict = listOftupleToDict(elementList)

    csvFile = open(filename, 'w', newline='')
    fields = ['year', 'state', 'structure', 'totalQty',
              'elementNo', 'cs1', 'cs2', 'cs3', 'cs4',
              'perfCat']
    csvWriter = csv.DictWriter(csvFile, fieldnames=fields)
    csvWriter.writeheader()
    csvWriter.writerows(listOfDict)
    csvFile.close()

def toJSON(elementList, path, filename):
    """
    Description: Converts named tuples into a JSON file

    Args:
        elementList (list): A list of named tuples
        path (string): path to save the JSON file

    Returns:
        None
    """
    filename = '2015-2019_nbe.json'
    os.chdir(path)
    listOfDict = listOftupleToDict(elementList)
    with open(filename, 'w') as jsonFile:
        json.dump(filename, jsonFile)

def main():
    directory ='/Users/AkshayKale/Documents/github/data/nbi/'
    directory_nbe ='/Users/AkshayKale/Documents/github/data/nbe/'
    directory_nbe_pro ='/Users/AkshayKale/Documents/github/data/nbe_processed/'
    csvFileName = '06-20-19-thesis-dataset_allstates_allstates.csv'
    filename = directory + csvFileName

    structBsdDict = getBSD(filename)
    structBsdMeanDict = calcDictMean(structBsdDict)
    structNums = list(structBsdDict.keys())
    scores = list(structBsdMeanDict.values())
    categories = getCategory(scores)
    structCatDict = dict(zip(structNums, categories))
    elementList = parseXml(directory_nbe, structCatDict)

    print("Exporting files ...")
    toCSV(elementList, directory_nbe_pro, '2015-2019_nbe.csv')
    toJSON(elementList, directory_nbe_pro, '2015-2019_nbe.json')

if __name__ == '__main__':
    main()
