"""
description: Validation of the decision tree outputs
"""
import csv
import os
from sklearn.metrics import confusion_matrix, classification_report
from collections import namedtuple
from collections import defaultdict
from collections import Counter

__author__ = 'Akshay Kale'
__copyright__ = 'GPL'

#  Year: 2019 ( output )
#  Requires: 1992 - 2019 dataset to create the timeseries data format  
#  Random Forest:  
#  Decision Trees:
    # Fir the random forest: 
        # For all the bridges in the nebraska:
def read_main_dataset(csvFile):
    listOfRecords = list()
    with open(csvFile, 'r') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        header = next(csvReader)
        header = [word.replace(" ", "_") for word in header]
        header = ["id" if word == '' else word for word in header]
        header[1] = 'unamed'
        Record = namedtuple('Record', header)
        for row in csvReader:
            record = Record(*row)
            structNum = record.structure_number
            deckInt = record.deck_intervention_in_next_3_years
            subInt = record.sub_intervention_in_next_3_years
            superInt = record.super_intervention_in_next_3_years
            listOfRecords.append([structNum, deckInt, superInt, subInt])
    return listOfRecords


def read_gt_results(csvRfFile):
    listOfRfIntervention = list()
    with open(csvRfFile, 'r') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        header = next(csvReader)
        record = namedtuple('Record', header)
        for row in csvReader:
            rec = record(*row)
            structNum = rec.structureNumber
            intervention = rec.intervention
            rfIntervention =  rec.rfIntervention
            listOfRfIntervention.append([structNum, intervention, rfIntervention])
    return listOfRfIntervention


def create_dict(listOfRecords):
    structDeck = defaultdict()
    structSub = defaultdict()
    structSup = defaultdict()
    for record in listOfRecords:
        struct = record[0]
        deck = record[1]
        sub = record[2]
        sup = record[3]
        structDeck[struct] = deck
        structSub[struct] = sub
        structSup[struct] = sup
    return structDeck, structSub, structSup

def rf_true_negative(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]
    rfResult == 'Yes'

    if rfResult == 'No' and groundTruth == 'No':
        return True
    else:
        return False


def rf_false_negative(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]
    rfResult == 'Yes'

    if rfResult == 'No' and groundTruth == 'Yes':
        return True
    else:
        return False


def rf_false_positive(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]

    if rfResult == 'Yes' and groundTruth == 'No':
        return True
    else:
        return False


def rf_true_positive(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]
    if rfResult == 'Yes' and groundTruth == 'Yes':
        return True
    else:
        return False


def flow_true_positive(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]
    if intervention == 'Yes' and groundTruth == 'Yes':
        return True
    else:
        return False

def flow_false_positive(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]
    if intervention == 'Yes' and groundTruth == 'No':
        return True
    else:
        return False

def flow_false_negative(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]
    if intervention == 'No' and groundTruth == 'Yes':
        return True
    else:
        return False

def flow_true_negative(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]
    if intervention == 'No' and groundTruth == 'No':
        return True
    else:
        return False


def both_false_negative(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]

    if intervention == 'No' and rfResult == 'No' and groundTruth == 'Yes':
        return True
    else:
        return False


def both_true_negatives(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]

    if intervention == 'No' and rfResult == 'No' and groundTruth == 'No':
        return True
    else:
        return False

def both_true_positives(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]

    if intervention == 'Yes' and rfResult == 'Yes' and groundTruth == 'Yes':
        return True
    else:
        return False


def both_false_positives(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]

    if intervention == 'Yes' and rfResult == 'Yes' and groundTruth == 'No':
        return True
    else:
        return False


def both_rf_true_positive(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]
    if intervention == 'No' and rfResult == 'Yes' and groundTruth == 'Yes':
        return True
    else:
        return False

def both_rf_true_negative(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]
    if intervention == 'Yes' and rfResult == 'No' and groundTruth == 'No':
        return True
    else:
        return False


def both_flow_true_positive(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]
    if intervention == 'Yes' and rfResult == 'No' and groundTruth == 'Yes':
        return True
    else:
        return False


def both_flow_true_negative(record):
    intervention = record[1]
    rfResult = record[2]
    groundTruth = record[3]
    if intervention == 'No' and rfResult == 'Yes' and groundTruth == 'No':
        return True
    else:
        return False



def count_ground_truth(lists):
    yesList = list()
    noList = list()
    for record in lists:
        yesRecord = record[3]
        if yesRecord == 'Yes':
            yesList.append(record)
        noList.append(record)
    return yesList, noList


def integrate(listOfRfIntervention, structDeck):
    rfTruePositive = list()
    rfTrueNegative = list()
    rfFalsePositive = list()
    rfFalseNegative = list()

    flowTruePositive = list()
    flowTrueNegative = list()
    flowFalsePositive = list()
    flowFalseNegative = list()

    bothTruePositive = list()
    bothTrueNegative = list()
    bothFalseNegative = list()
    bothFalsePositive = list()

    bothRfTruePositive = list()
    bothRfTrueNegative = list()

    bothFlowTruePositive = list()
    bothFlowTrueNegative = list()

    counter = 0
    yesList = list()
    noList = list()
    for record in listOfRfIntervention:
        structNum = record[0]
        record.append(structDeck.get(structNum))

        # Recoding flow chart intervention
        if record[1][:4] == 'None':
            record[1] = 'No'
        else:
            record[1] = 'Yes'

        # Recoding random forest results
        if record[2] == '':
            record[2] = None
        elif record[2] == 'yes':
            record[2] = 'Yes'
        else:
            record[2] = 'No'


        # Record both positive
        if record[2] != None:
            counter = counter + 1
            if record[3] == 'Yes':
                yesList.append(record)

            if record[3] == 'No':
                noList.append(record)

            if both_true_positives(record):
                bothTruePositive.append(record)

            if both_true_negatives(record):
                bothTrueNegative.append(record)

            if both_false_negative(record):
                bothFalseNegative.append(record)

            if both_false_positives(record):
                bothFalsePositive.append(record)

            if rf_true_positive(record):
                rfTruePositive.append(record)

            if rf_true_negative(record):
                rfTrueNegative.append(record)

            if rf_false_positive(record):
                rfFalsePositive.append(record)

            if rf_false_negative(record):
                rfFalseNegative.append(record)

            if flow_true_positive(record):
                flowTruePositive.append(record)

            if flow_true_negative(record):
                flowTrueNegative.append(record)

            if flow_false_positive(record):
                flowFalsePositive.append(record)

            if flow_false_negative(record):
                flowFalseNegative.append(record)

            if both_rf_true_positive(record):
                bothRfTruePositive.append(record)

            if both_rf_true_negative(record):
                bothRfTrueNegative.append(record)

            if both_flow_true_positive(record):
                bothFlowTruePositive.append(record)

            if both_flow_true_negative(record):
                bothFlowTrueNegative.append(record)
        else:
            continue

        returnSt = [ bothFalseNegative,
                     bothFalsePositive,
                     bothTrueNegative,
                     bothTruePositive,
                     rfTrueNegative,
                     rfTruePositive,
                     rfFalseNegative,
                     rfFalsePositive,
                     flowTrueNegative,
                     flowTruePositive,
                     flowFalseNegative,
                     flowFalsePositive,
                     counter,
                     yesList,
                     noList,
                     bothFlowTruePositive,
                     bothFlowTrueNegative,
                     bothRfTruePositive,
                     bothRfTrueNegative
                  ]


    return returnSt


def to_csv(listOfRecords, filename):
    with open(filename, 'w') as csvfile:
        csvWriter = csv.writer(csvfile)
        header = ['structureNumber']
        for row in listOfRecords:
            csvWriter.writerow([row[0]])


def to_csv_all_bridges(listOfRecords, filename):
    with open(filename, 'w') as csvfile:
        csvWriter = csv.writer(csvfile)
        header = ['structureNumber', 'flowChartResult', 'randomForest', 'groundTruth']
        csvWriter.writerow(header)
        for row in listOfRecords:
            csvWriter.writerow(row)


def main():
    path = '../../../../data/trees/decision-tree-dataset/'
    csvFile = 'decision_tree.csv'
    os.chdir(path)

    pathIntervention = '../../nbi/'
    csvGtFile = 'intervention_bds.csv'

    listOfRecords = read_main_dataset(csvFile)
    os.chdir(pathIntervention)
    listOfGtIntervention = read_gt_results(csvGtFile)
    # listOfRecords -  deck, superstructure, substructure
    structDeck, structSub, structSup = create_dict(listOfRecords)

    ## RF intervention
    #Structure Number, Flow Chart, Random Forest, label
    bFN, bFP, bTN, bTP, rfTN, rfTP, rfFN, rfFP, flTN, flTP, flFN, flFP, count, yes, no, bfl, bfln, brf, brfn = integrate(listOfGtIntervention, structDeck)


    print("\n")
    print("--"*16+' Ground Truth '+"--"*16)
    print("\n")
    print('Number of records with ground truth Yes (Positive):', len(yes), ', Percent: ', (len(yes)/count)*100)
    print('Number of records with ground truth No (Negative):', len(no), ', Percent: ', (len(no)/count)*100)

    print("\n")
    print("--"*16+' Random Forest '+"--"*16)
    print("\n")

    # Randomforest
    print('Random Forest True Positive:', len(rfTP), ', Percent: ', (len(rfTP)/count)*100)
    print('Random Forest True Negative:', len(rfTN), ', Percent: ', (len(rfTN)/count)*100)
    print('Random Forest False Positive:', len(rfFP), ', Percent: ', (len(rfFP)/count)*100)
    print('Random Forest False Negative:', len(rfFN), ', Percent: ', (len(rfFN)/count)*100)
    print('Random Forest Accuracy:', (len(rfTP) + len(rfTN)) / count)

    print("\n")
    print("--"*16+' Flow Chart '+"--"*16)
    print("\n")

    # Flow chart
    print('Flow Chart True Positive:', len(flTP), ', Percent: ', (len(flTP)/count)*100)
    print('Flow Chart True Negative:', len(flTN), ', Percent: ', (len(flTN)/count)*100)
    print('Flow Chart False Positive:', len(flFP), ', Percent: ', (len(flFP)/count)*100)
    print('Flow Chart False Negative:', len(flFN), ', Percent: ', (len(flFN)/count)*100)
    print('Flow Chart Accuracy:', (len(flTP) + len(flTN)) / count)

    print("\n")
    print("--"*16+' Random Forest and Flow Chart  '+"--"*16)
    print("\n")

    # Flow chart
    print('Both True Positive:', len(bTP), ', Percent: ', (len(bTP)/count)*100)
    print('Both True Negative:', len(bTN), ', Percent: ', (len(bTN)/count)*100)
    print('Both False Positive:', len(bFP), ', Percent: ', (len(bFP)/count)*100)
    print('Both False Negative:', len(bFN), ', Percent: ', (len(bFN)/count)*100)
    print('True Positive Rf - False Negative Flow:', len(brf), ', Percent: ', (len(brf)/count)*100)
    print('True Negative Rf - False Positive Flow:', len(brfn), ', Percent: ', (len(brfn)/count)*100)

    print('True Positive Flow - False Negative Rf:', len(bfl), ', Percent: ', (len(bfl)/count)*100)
    print('True Negative Flow - False Positive Rf:', len(bfln), ', Percent: ', (len(bfln)/count)*100)
    print("\n")
    print(len(bTP)+len(bTN)+len(bFP)+len(bFN)+len(brf)+len(brfn)+len(bfl)+len(bfln))
    #print(count)

    #export both true positive
    to_csv_all_bridges(bTP, 'bTP.csv')
    to_csv_all_bridges(bTN, 'bTN.csv')
    to_csv_all_bridges(bFP, 'bFP.csv')
    to_csv_all_bridges(bFN, 'bFN.csv')

    # flowchart
    to_csv_all_bridges(bfl, 'bridgesFl.csv')
    to_csv_all_bridges(bfln, 'bridgesFlNegative.csv')

    # randomforest
    to_csv_all_bridges(brf, 'bridgesRf.csv')
    to_csv_all_bridges(brfn, 'bridgesRfNegative.csv')

    # all bridges
    to_csv_all_bridges(listOfGtIntervention, 'allBridges.csv')



if __name__ == '__main__':
    main()
