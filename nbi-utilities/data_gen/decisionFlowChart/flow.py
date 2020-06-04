"""
title: This file contains functions that emulate the conditions of
deicison flow chart by NDOT
author: Akshay Kale
"""
import csv

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


def condition1_1(records):
    """
    Description: filter all the records where pile condition < 3
    Args:
        record (list): list to the bridge attributes
    Returns:
        structures (list): a list of structures that satisfy the condition
    """
    structures = list()
    for record in records:
        if record['column'] < 3:
            structures.append(True)
        else:
            structures.append(False)
    return structures


def decision_flow_chart(csvReader):
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
    return header


def main():
    # need the raw nbi file
    csvFileName = '../../../../data/datacenterhub/NBI_text_file.csv'
    print(read_csv(csvFileName))


if __name__ == '__main__':

    main()
