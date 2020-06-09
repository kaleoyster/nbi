"""
title: This file contains functions that emulate the conditions of
deicison flow chart by NDOT
author: Akshay Kale
"""
import csv
import datetime
from collections import namedtuple

__author__ = 'Akshay Kale'
__copyright__ = 'GPL'
__credit__ = []
__email__ = 'akale@unomaha.edu'

#TODO
# Preprocess (Pipeline): 
#   1. (List) Extract all the necessary attribute
#   2. Using if and else, create a pipeline, that takes in:
#               1. Args: (record, datastructure)
#               2. Returns: report (JSON datastructure)
#   3. Run decision flow chart -> Create condition Report

# Datastructure ( Report ):
#   1. {structure: {condition1: True,
#                    condition2: False,
#                    condition3: True,
#                    condition4: False,
#                    condition5: False
#      }}

# Create Decision Flow Chart:
#   1. For every record -> pipeline (preprocess) -> Report
#   2. preprocess

def is_culvert(structureType):
    """
    Description: Check if a bridge is a culvert
    Args:
        record (list): list to the bridge attributes
    Returns:
        structures (list): a list of structures that satisfy the condition
        function: record passed to a depended function
    """
    if int(structureType) == 19:
        return True
    return False


def calc_age(built_year):
    """
    Description: Check substructure condition
    Args:
        record (list): list to the bridge attributes
    Returns:
        structures (list): a list of structures that satisfy the condition
        function: record passed to a depended function
    """
    datetime_now = datetime.datetime.now()
    year = datetime_now.year
    built_year = int(built_year)

    return year - built_year


def sub_condition_check(subCondition):
    """
    Description: Check substructure condition
    Args:
        record (list): list to the bridge attributes
    Returns:
        structures (list): a list of structures that satisfy the condition
        function: record passed to a depended function
    """
    if int(subCondition) < 4:
        return 'Replace'
    return 'Continue'


def decision_flow_chart(record):
    """
    Description: Takes records can performs condition checks
    Args:
        record (list): A list of bridge attributes
    Returns:
        structures (list): a list of structures that require maintenance
        function: calls a corresponding function
    """
    # all the attribute values required by decision flow chart
    isCulvert = is_culvert(record.STRUCTURE_TYPE_043B)
    subCondition = sub_condition_check(record.SUBSTRUCTURE_COND_060)
    #scourCritical = scour_critical_check(record.SCOUR_CRITICAL_113)
    age = calc_age(record.YEAR_BUILT_027)

    print(age)
    #print(scourCritical)
    #print(subCondition)
    print(isCulvert)

    #if isCulvert is False:
    #    return sub_condition_check(subCondition)
    #return isCulvert


def decision_flow_chart_old(csvReader):
    """
    Description: takes in filename and performs conditional checks
    Args:
        filename (string): path to the nbi file
    Returns:
        structures (list): a list of structures that require maintenance
    """
    report = list()
    for record in csvReader:
        # Extract fields
        # Execute function with filed
        fieldStat1_1 = condition1_1(field)
        field1 = record[0]
        if condition1_1(fieldStat1_1) is True:
            report.append(True)
        elif condition1_2(field1) is True:
            report.append(False)
        else:
            report.append(None)
    return report


def read_csv(filename):
    """
    Description: takes in filename and performs conditional checks
    Args:
        filename (string): path to the nbi file
    Returns:
        structures (list): a list of structures that require maintenance
    """
    with open(filename, 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        header = next(csvReader)
        Record = namedtuple('Record', header)
        for row in csvReader:
            print(row)
            record = Record(*row)
            print(decision_flow_chart(record))
            break


def main():
    # need the raw nbi file
    # TODO
    # Run the model on the lastest data
    csvFileName = '/home/akshay/data/nbi/nbi.csv'
    print(read_csv(csvFileName))


if __name__ == '__main__':

    main()
