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


def sub_condition_check(record):
    """
    Description: Check substructure condition
    Args:
        record (list): list to the bridge attributes
    Returns:
        structures (list): a list of structures that satisfy the condition
        function: record passed to a depended function
    """
    try:
        subCondition = int(record.SUBSTRUCTURE_COND_060)

        if subCondition < 4:
            return 'Replace'
        elif subCondition > 3:
            return scour_critical_check(record)
    except:
        return scour_critical_check(record)


def scour_critical_check(record):
    """
    Description: Check substructure condition
    Args:
        record (list): list to the bridge attributes
    Returns:
        structures (list): a list of structures that satisfy the condition
        function: record passed to a depended function
    """
    try:
        scourRating = int(record.SCOUR_CRITICAL_113)

        if scourRating > 0 and scourRating <= 3:
            return 'Replace'
        elif scourRating == 8:
            return 'Replace'
        else:
            return sub_condition_check2(record)
    except:
        return sub_condition_check2(record)


def sub_condition_check2(record):
    """
    Description: Check substructure condition
    Args:
        record (list): list to the bridge attributes
    Returns:
        structures (list): a list of structures that satisfy the condition
        function: record passed to a depended function
    """
    try:
        subCondition = int(record.SUBSTRUCTURE_COND_060)
        age = calc_age(record.YEAR_BUILT_027)

        if subCondition == 4 and age > 75:
            return 'Replace'
        else:
            return super_condition_check(record)
    except:
        return super_condition_check(record)


def super_condition_check(record):
    """
    Description: Check substructure condition
    Args:
        record (list): list to the bridge attributes
    Returns:
        structures (list): a list of structures that satisfy the condition
        function: record passed to a depended function
    """
    try:
        superCondition = int(record.SUPERSTUCTURE_COND_059)
        age = calc_age(record.YEAR_BUILT_027)

        if superCondition > 5:
            return deck_conditon_check(record)
        elif superCondition == 5:
            return frac_critical_check(record)
        elif superCondition > 5:
            if age > 75:
                return 'Replace'
            else:
                return design_load_check(record)
    except:
        return 'None'


def deck_condition_check(record):
    """
    Description: Check substructure condition
    Args:
        record (list): list to the bridge attributes
    Returns:
        structures (list): a list of structures that satisfy the condition
        function: record passed to a depended function
    """
    try:
        deckCondition = int(record.DECK_COND_058)

        if deckCondition > 5:
            return 'Redeck'
        elif deckCondition < 5:
            # NOTE: No membrane type for asphalt
            if record.MEMBRANE_TYPE_108B == '3':
                return 'Add deck Protection System, Preserve Sub & Super'
        else:
            return 'Deck UIP, Preserve Sub & Super'
    except:
        return 'None'


def design_load_check(record):
    """
    Description: Check substructure condition
    Args:
        record (list): list to the bridge attributes
    Returns:
        structures (list): a list of structures that satisfy the condition
        function: record passed to a depended function
    """
    try:
        designLoad = int(record.DESIGN_LOAD_031)

        if designLoad < 3:
            return 'Rehab Pending Sub Capacity Review'
        else:
            return 'Rehab'
    except:
        return 'None'


def cbc_condition_check(record):
    """
    Description: Takes records can performs condition checks
    Args:
        record (list): A list of bridge attributes
    Returns:
        structures (list): a list of structures that require maintenance
        function: calls a corresponding function
    """
    try:
        cbcCondition = int(record.CULVERT_COND_062)
        age = calc_age(record.YEAR_BUILT_027)

        if cbcCondition < 4:
            return 'Replace'
        elif cbcCondition > 4:
            return 'UIP'
        else:
            if age > 70:
                return 'Replace'
            return 'Repair'
    except:
        return 'None'

def decision_flow_chart(record):
    """
    Description: Takes records can performs condition checks
    Args:
        record (list): A list of bridge attributes
    Returns:
        structures (list): a list of structures that require maintenance
        function: calls a corresponding function
    """
    isCulvert = is_culvert(record.STRUCTURE_TYPE_043B)
    if isCulvert is False:
        return sub_condition_check(record)
    else:
        return cbc_condition_check(record)


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
            record = Record(*row)
            print(decision_flow_chart(record))


def main():
    csvFileName = '/home/akshay/data/nbi/nbi.csv'
    print(read_csv(csvFileName))


if __name__ == '__main__':

    main()
