import os
import numpy as np
import csv
from collections import namedtuple
from collections import Counter

def main():
    path = '../../../../data/nbi/'
    csvFile = 'intervention_bds.csv'
    os.chdir(path)

    records = list()
    with open(csvFile, 'r') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        header = next(csvReader)
        Record = namedtuple('Record', header)

        for row in csvReader:
            records.append(Record(*row))

    categories = list()
    for rec in records:
        categories.append(rec.category)

    interventions = list()
    for rec in records:
        interventions.append(rec.intervention)

    print(Counter(categories))
    print(Counter(interventions))


if __name__ == '__main__':
    main()
