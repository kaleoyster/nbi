"""
The script updates new cases to the top level file for the data-center hub
"""
import pandas as pd
import csv
import os
import numpy as np
from collections import OrderedDict
from collections import defaultdict
import sys

__author__ = 'Akshay Kale'
__copyright__ = 'GPL'
__credits__ = ['Jonathan Monical']
__email__ = 'akale@unomaha.edu'

list_of_args = [arg for arg in sys.argv]
codename, case_file, top_file, nbi_file, YEAR = list_of_args

# Import relevant files
df_cases = pd.read_csv(case_file, skiprows=[0, 2, 3], low_memory=False)
df_top_level = pd.read_csv(top_file, low_memory=False)
df_nbi = pd.read_csv(nbi_file, low_memory=False)


# Get Cases ids from all the files
set_cases_top = set(df_top_level['Case Id'])
set_cases_nbi = set(df_nbi['Case Id'])
set_cases_cases = set(df_cases['Case ID'])

new_cases = set_cases_cases - set_cases_top

# Check if the cases exist in the curent nbi survey records (DEAD CODE - Not used anywhere)
def check_case_in_cases(new_cases):
    if new_cases in set_cases_nbi:
        return True
    return False


# Condition rating coding
condition_rating_dict = {
                             1: 1,
                            '1': 1,

                             2: 2,
                             '2': 2,

                             3: 3,
                             '3': 3,

                             4: 4,
                             '4': 4,

                             5: 5,
                             '5': 5,

                             6: 6,
                             '6': 6,

                             7: 7,
                             '7': 7,

                             8: 8,
                             '8':8,

                             '9': 9,
                             9: 9,

                              0: 0,
                             '0': 0,
                             'N': None,
                          }
# Select columns
selected_columns = [
                      'Case Name', # Case Name
                      'Longitude', # Longitude
                      'Latitude',  # Latitude
                      'Built in',  # Year Built 
                      'Material',  # Material
                      'Construction Type', # Construction
                      'ADT', # ADT
                      'ADTT (% ADT)', # ADTT
                      'Deck', # Deck
                      'Super', # Superstructure
                      'Sub' # Substructure
                 ]

## Corresponding columns of selected columns in the top-level record
top_level_columns = [
                      'Case Name', # Case Name
                      'Longitude', # Longitude
                      'Latitude',  # Latitude
                      'Year Built',  # Year Built 
                      'Material',  # Material
                      'Construction Type', # Construction
                      'ADT', # ADT
                      'ADTT', # ADTT
                      'Deck', # Deck
                      'Superstructure', # Superstructure
                      'Substructure' # Substructure
                      ]

identity_columns = [
                     'Case Name',
                     'Longitude',
                     'Latitude',
                     'Year Built',
                     'Material',
                     'Construction Type'
                    ]

# Select the key: case ids
key = 'Case Id'

# Create list of the dictionaries
def create_list_of_dicts(columns, key):
    df_keys = df_nbi[key]
    list_of_dictionary = []

    for column in columns:
        temp_dict = defaultdict()
        df_column = df_nbi[column]

        for key, value in zip(df_keys, df_column):
            temp_dict[key] = value

        list_of_dictionary.append(temp_dict)
    return list_of_dictionary

list_of_dict = create_list_of_dicts(selected_columns, key)

# Create a updated list of attribute values from top level
def create_update_list(top_level_columns):
    list_of_updated_values = []
    for index, column in enumerate(top_level_columns):
        top_col = df_top_level[column] # Series
        top_ids = df_top_level['Case Id'] # Series
        nbi_col = list_of_dict[index] # Dictionary
        temp_list = []
        for top_id, top_val in zip(top_ids, top_col):
            if column in identity_columns:
                try:
                     temp_list.append(nbi_col[top_id])
                except:
                     temp_list.append(top_val)
            else:
                try:
                     temp_list.append(nbi_col[top_id])
                except:
                     temp_list.append(None)
        list_of_updated_values.append(temp_list)

    return list_of_updated_values

list_of_updated_values = create_update_list(top_level_columns)

# Update df_top_level 
df_top_level['Longitude'] = list_of_updated_values[1]
df_top_level['Latitude'] = list_of_updated_values[2]
df_top_level['Year Built'] = list_of_updated_values[3]
df_top_level['Material'] = list_of_updated_values[4]
df_top_level['Construction Type'] = list_of_updated_values[5]

# Get columns names
ADT = df_top_level.columns[-6]
ADTT = df_top_level.columns[-5]
DECK  = df_top_level.columns[-4]
SUPERSTRUCTURE = df_top_level.columns[-3]
SUBSTRUCTURE  = df_top_level.columns[-2]

# Update columns for the latest year in top level file
df_top_level[ADT]  = list_of_updated_values[6]
df_top_level[ADTT] = list_of_updated_values[7]
df_top_level[DECK] = pd.Series(list_of_updated_values[8]).map(condition_rating_dict)
df_top_level[SUPERSTRUCTURE] = pd.Series(list_of_updated_values[9]).map(condition_rating_dict)
df_top_level[SUBSTRUCTURE] = pd.Series(list_of_updated_values[10]).map(condition_rating_dict)
df_top_level[YEAR] = len(df_top_level)*[None]

# Save intermediate top-level file
df_top_level.to_csv('top-level-intermediate.csv')

#------------------------Updating id in the nbi id-----------------------------#
dict_case_id_name = defaultdict()
for case_id, dc_id in zip(df_top_level['Case Id'], df_top_level['Id']):
    dict_case_id_name[case_id] = dc_id

df_nbi['Id'] = df_nbi['Case Id'].map(dict_case_id_name)
filename_nbi = 'NBI' + YEAR + '.csv'
df_nbi.to_csv(filename_nbi)

#----------------Correcting the header of the top level file------------------------#
filename_top = 'TopLevel1992-' + YEAR + '.csv'
with open('top-level-intermediate.csv', 'r') as inFile, open(filename_top, 'w', newline = '') as outFile:
    r = csv.reader(inFile)
    w = csv.writer(outFile)
    lines = inFile.readlines()
    lines_reader = lines[0].split(',')
    new_words = []

    #Following for loop removes '.Number' from the column names
    for word in lines_reader:
        if '.' in word:
            temp_word = ''
            for char in word:
                if char == '.':
                    new_words.append(temp_word)
                    temp_word = ''
                else:
                    temp_word = temp_word + char
        else:
            new_words.append(word.strip('\n'))
    next(r, None)
    w.writerow(new_words)
    for row in lines[1:]:
        write_row = row.split(",")
        write_row[-1] = write_row[-1].strip()
        w.writerow(write_row)
