import os
import numpy as np
import csv
from collections import namedtuple
from collections import Counter

def main():
    path = '../../../../data/nbi/'
    csvFile = 'intervention_bds.csv'
    os.chdir(path)

    # open csv file
    records = list()
    with open(csvFile, 'r') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        header = next(csvReader)
        Record = namedtuple('Record', header)

        # immutable records
        for row in csvReader:
            records.append(Record(*row))
            #print(Record(*row))

    # create a list of categories
    categories = list()
    for rec in records:
        categories.append(rec.category)

    # create a list of interventions
    interventions = list()
    for rec in records:
        interventions.append(rec.intervention)

    # create a list of rfInterventions
    rfInterventions = list()
    for rec in records:
        rfInterventions.append(rec.rfIntervention)

    recordsTemp = list()
    for rec in records:
        if rec.rfIntervention == 'yes':
            recordsTemp.append(rec)

    print("Count of bridges with respect to categories")
    print(Counter(categories))
    print("\n")

    print("Count of bridges with respect to interventions")
    print(Counter(interventions))
    print("\n")

    print("Count of bridges with respect to random forest interventions")
    print(Counter(rfInterventions))
    print("\n")


if __name__ == '__main__':
    main()
