"""
title: This file contains functions that emulate the conditions of
deicison flow chart by NDOT
author: Akshay Kale
"""
import csv
import datetime
from collections import namedtuple
from collections import defaultdict


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
        True / False (Bool)
    """
    if int(structureType) == 19:
        return True
    return False


def calc_age(built_year):
    """
    Description: Calculate Age of the Bridge from the Year built
    Args:
        built_year (string): Built year of the bridge
    Returns:
        age (int): age of the bridge
    """
    datetime_now = datetime.datetime.now()
    year = datetime_now.year
    built_year = int(built_year)
    age = year - built_year
    return age


def sub_condition_check(record):
    """
    Description: Check substructure condition
    Args:
        record (list): list to the bridge attribute
    Returns:
        Replace (str): result of the sub_condition_check
        scour_critical_check (function): records passed to scour_critical_check
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
    Description: Check bridge scour critical
    Args:
        record (list): list to the bridge attributes
    Returns:
        'Replace' (str): result of the scour critical check
        sub_condition_check (function): record passed to a sub_condition_check
    """
    try:
        scourRating = int(record.SCOUR_CRITICAL_113)

        if scourRating > 0 and scourRating <= 3:
            return 'Replace'
        elif scourRating == 8:
            return 'Replace - Scour Rating = 8'
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
        'Replace' (str)
        super_condition_check (function): record passed to a depended function
    """
    try:
        subCondition = int(record.SUBSTRUCTURE_COND_060)
        age = calc_age(record.YEAR_BUILT_027)

        if subCondition == 4 and age > 75:
            return 'Replace - Subcondition = 4 and age > 75'
        else:
            return super_condition_check(record)
    except:
        return super_condition_check(record)


def super_condition_check(record):
    """
    Description: Check substructure condition of a bridge
    Args:
        record (list): list to the bridge attributes
    Returns:
        'Replace' (str): a list of structures that satisfy the condition
        design_load_check (function): record passed to a depended function
    """
    try:
        superCondition = int(record.SUPERSTUCTURE_COND_059)
        age = calc_age(record.YEAR_BUILT_027)

        if superCondition > 5:
            return deck_condition_check(record)
        elif superCondition == 5:
            return fract_critical_check(record)
        elif superCondition > 5:
            if age > 75:
                return 'Replace - Superstructure condition > 5 and age > 75'
            else:
                return design_load_check(record)
    except:
        return 'None - Super condition check'


def fract_critical_check(record):
    """
    Description: Check fracture critical of a bridge
    Args:
        record (list): list of the  bridge attributes
    Returns:
        'Replace' (str)
        'None' (str)
    """
    try:
        fracCritical = int(record.FRACTURE_LAST_DATE_093A)

        if fracCritical != 0:
            return 'Replace'
        else:
            return deck_condition_check(record)

    except:
        return 'None - Fracture Critical Check'


def deck_condition_check(record):
    """
    Description: Check substructure condition
    Args:
        record (list): list to the bridge attributes
    Returns:
        'Redeck' (string)
        'Add Deck Protection System' (string)
        'Deck UIP, Preseve Sub & Super'
    """
    try:
        deckCondition = int(record.DECK_COND_058)

        if deckCondition > 5:
            return 'Redeck'
        elif deckCondition < 5:
            # NOTE: No membrane type for asphalt
            if record.MEMBRANE_TYPE_108B == '3':
                return 'Add Deck Protection System, Preserve Sub & Super'
        else:
            return 'Deck UIP, Preserve Sub & Super'
    except:
        return 'None - deck condition check'


def design_load_check(record):
    """
    Description: Check substructure condition
    Args:
        record (list): list to the bridge attributes
    Returns:
        'Rehab Pending Sub Capacity Review' (string)
        'Rehab - Design Load Check' (string)
        'None' (string)
    """
    try:
        designLoad = int(record.DESIGN_LOAD_031)

        if designLoad < 3:
            return 'Rehab Pending Sub Capacity Review'
        else:
            return 'Rehab - Design Load Check'
    except:
        return 'None - from desing load check'


def cbc_condition_check(record):
    """
    Description: Takes records can performs condition checks
    Args:
        record (list): A list of bridge attributes
    Returns:
        'Replace'(string)
            'UIP'(string)
            'None'(string)
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
        return 'None - Return from cbc_condition_check'


def starting_point(record):
    """
    Description: Takes records can performs condition checks
    Args:
        record (list): A list of bridge attributes
    Returns:
        sub_condition_check (function): calls a corresponding function
    """
    isCulvert = is_culvert(record.STRUCTURE_TYPE_043B)
    if isCulvert is False:
        return sub_condition_check(record)
    else:
        return cbc_condition_check(record)


def decision_flow_chart(filename):
    """
    Description: takes in filename and performs NDOT conditional checks
    Args:
        filename (string): path to the nbi file
    Returns:
        structIntervention (list): a list of structures and interventions
    """
    structInterventions = defaultdict()
    with open(filename, 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        header = next(csvReader)
        Record = namedtuple('Record', header)
        for row in csvReader:
            record = Record(*row)
            structNum = record.STRUCTURE_NUMBER_008
            structNum = structNum.strip()
            structInterventions[structNum] = starting_point(record)
    return structInterventions


def main():
    csvFileName = '/home/akshay/data/nbi/nbi.csv'
    structIntervention = decision_flow_chart(csvFileName)

    with open('/home/akshay/data/nbi/intervention.csv', 'w') as outputFile:
        for key in structIntervention.keys():
            outputFile.write("%s, %s\n" % (key, structIntervention[key]))


if __name__ == '__main__':
    main()
