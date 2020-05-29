"""
The scripts provide functions to extract, read, and parse XML files.
"""
import os
import csv
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
    for zfile in tqdm(os.listdir(directory), desc='Extracting XML'):
        if zfile.endswith(extension):
            os.chdir(directory)
            filename = directory + '/' + zfile
            filename = os.path.abspath(zfile)
            zip_ref = ZipFile(filename)
            zip_ref.extractall(directory)
            zip_ref.close()
            os.remove(filename)

def parseXml(directory):
    """
    Description:  Read and parses xml files
    Args:
        directory (string): Path of the xml files
    Returns:
        element_dictionary (dictionary)
    """
    elementDictionary = defaultdict(list)
    Record = namedtuple('Record', ['state', 'structure',
                                   'totalqty', 'elementNo',
                                   'cs1', 'cs2', 'cs3', 'c4'])
    records = list()
    for xmlfile in tqdm(os.listdir(directory), desc='Parsing XML'):
        if xmlfile.endswith('.xml'):
            os.chdir(directory)
            tree = ET.parse(xmlfile)
            root = tree.getroot()
            for element in root.findall('FHWAED'):
                state = element.find('STATE').text
                structure = element.find('STRUCNUM').text
                totalqty = element.find('TOTALQTY').text
                elementNo = element.find('EN').text
                cs1 = element.find('CS1').text
                cs2 = element.find('CS2').text
                cs3 = element.find('CS3').text
                cs4 = element.find('CS4').text
                tempRecord = Record(state,
                                     structure,
                                     totalqty,
                                     elementNo,
                                     cs1,
                                     cs2,
                                     cs3,
                                     cs4)
                elementDictionary[structure].append(tempRecord)
    return elementDictionary

def getBSD(filename):
    """
    Description: Function to read NBI file
         and, extract structurenumber and baseline difference score
    Args:
        filename (string): Path of the xml files
    Returns:
        structBsdDict (dictionary) : key (structure number)
                                     value (baseline difference score)
    """
    with open(filename, 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        header = next(csvReader)
        structBsdDict = defaultdict(list)
        for row in tqdm(csvReader, desc='Extracting Score'):
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

def main():
    directory ='/Users/AkshayKale/Documents/github/data/nbi/'
    directory_nbe ='/Users/AkshayKale/Documents/github/data/nbe/'
    csvFileName = '06-20-19-thesis-dataset_allstates_allstates.csv'
    filename = directory + csvFileName

    elementDict = parseXml(directory_nbe)
    structBsdDict = getBSD(filename)
    structBsdMeanDict = calcDictMean(structBsdDict)

    scores = structBsdMeanDict.values()
    # Combine elementDict and structureBsdMeanDict
    # To split bridges that are doing good and bad

if __name__ == '__main__':
    main()
