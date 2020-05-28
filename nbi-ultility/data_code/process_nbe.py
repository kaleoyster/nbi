from zipfile import ZipFile
from collections import defaultdict
from collections import namedtuple
import xml.etree.ElementTree as ET
import os

def readXml(zipFile):
    """
    Description: function reads xml file from the zipfile,
    and returns a xml object.
    args: zipfile (string)
    returns: xml (xml file object)
    """
    arch = ZipFile(zipFile, 'r')
    zfile = zipFile[-22:]
    xmlfile = zfile[:-3] + 'xml'
    xml = arch.read(xmlfile)
    return xml

def parseSubroutine(tree):
    """
    """
    pass

def parseXml(directory):
    """
    Description:  Read and parses xml files and parses
    """
    # Dictionary  Key: structure number, values: element numbers
    # Dictionary Key: structure number, value:
    element_dictionary = defaultdict(list)
    # list all the xmlfiles in the directory
    Record = namedtuple('Record', ['state', 'structure',
                                   'totalqty', 'elementNo',
                                   'cs1', 'cs2', 'cs3', 'c4'])
    records = list()
    for xmlfile in os.listdir(directory):
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
                temp_record = Record(state,
                                     structure,
                                     totalqty,
                                     elementNo,
                                     cs1,
                                     cs2,
                                     cs3,
                                     cs4)
                print(temp_record)
                element_dictionary[structure] = temp_record
        break
    return element_dictionary


def extractXml(directory):
    extension = ".zip"
    for zfile in os.listdir(directory):
        if zfile.endswith(extension):
            os.chdir(directory)
            filename = directory + '/' + zfile
            filename = os.path.abspath(zfile)
            zip_ref = ZipFile(filename)
            zip_ref.extractall(directory)
            zip_ref.close()
            os.remove(filename)

def main():
    # Get all the file names in the directory
    # Directory relative directory
    directory ='/Users/AkshayKale/Documents/github/data/nbe'
    # extractXml(directory)
    print(len(parseXml(directory)))
    # parse xml file 

    # convert it to json dump 
    # append it into a list
    # push into mongodb


if __name__ == '__main__':
    main()
