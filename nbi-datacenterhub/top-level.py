import pandas as pd
import csv
import os
import numpy as np
from collections import OrderedDict

# Reading the Inspection data files
df = pd.read_csv("NBI Inspections Data - 131.csv", low_memory = True, index_col = False)
df_new_cases = pd.read_csv("transformed NBI spreadsheet.csv", low_memory = False)
# Dropping columns

df = df.drop(['2018', '2019'], axis = 1)

# Creating columns from the transformed NBI spreadsheet
case_id = df_new_cases['Case Id'].astype(str)
case_id_og = df['Case Id'].astype(str)

year = ''*len(df_new_cases['Case Id'])

latitude = df_new_cases['Latitude']
latitude_og = df['Latitude']


longitude = df_new_cases['Longitude']
longitude_og = df['Longitude']

year_built = df_new_cases['Built in']
year_built_og = df['Year Built']

material = df_new_cases['Material']
material_og = df['Material']

construction = df_new_cases['Construction Type']
construction_og = df['Construction Type']

ADT = df_new_cases['ADT']
ADT_og = df['ADT']

ADTT = df_new_cases['ADTT (% ADT)']
ADTT_og = df['ADTT']

deck = df_new_cases['Deck']
deck_og = df['Deck']

superstructure = df_new_cases['Super']
sup_og = df['Superstructure']

substructure =  df_new_cases['Sub']
sub_og = df['Substructure']

# creating new dataframe for transformed NBI spreadsheet
df_top_level = pd.DataFrame({'Case Id.27': case_id,
                                         '2018': year,
                                         'Latitude': latitude,
                                         'Longitude': longitude,
                                         'Year Built': year_built,
                                         'Material': material,
                                         'Construction Type': construction,
                                         'ADT.27': ADT,
                                         'ADTT.27': ADTT,
                                         'Deck.27': deck,
                                         'Superstructure.27': superstructure,
                                         'Substructure.27': substructure,
                             })

# Add new case Id at the bottom the top-level df
new_bridges = list(set(case_id) - set(df['Case Id']))
new_bridge = pd.DataFrame({'Case Id': new_bridges})
df = df.append(new_bridge, ignore_index=True)


## Longitude
# Create dictionary Longitude with respect to the case id
_id_longi_dict =  {_id: longi for _id, longi in zip(case_id, longitude)}

# Dictionary of the existing top-level file
_id_longi_og_dict = {_id:longi_og for _id, longi_og in zip (case_id_og, longitude_og)}

# Update longitude of the top-level dictionary
for key, value in _id_longi_og_dict.items():
    if (_id_longi_dict.get(key)) != None:
        _id_longi_og_dict[key] = _id_longi_dict[key]

update_longitude = df['Case Id'].map(_id_longi_og_dict)

## Latitude
# Create dictionary of latitude with respect to the case id
_id_lati_dict =  {_id: lati for _id, lati in zip(case_id, latitude)}

# Dictionary of the existing top-level file
_id_lati_og_dict = {_id: lati_og for _id, lati_og in zip (case_id_og, latitude_og)}

# Update latitude of the top-level dictionary
for key, value in _id_lati_og_dict.items():
    if (_id_lati_dict.get(key)) != None:
        _id_lati_og_dict[key] = _id_lati_dict[key]

update_latitude = df['Case Id'].map(_id_lati_og_dict)


## Year Built
# Create dictionary of year built with respect to the case id
_id_year_dict =  {_id: year for _id, year in zip(case_id, year_built)}

# Dictionary of the existing top-level file
_id_year_og_dict = {_id: year_og for _id, year_og in zip (case_id_og, year_built_og)}

# Update year built  of the top-level dictionary
for key, value in _id_year_og_dict.items():
    if (_id_year_dict.get(key)) != None:
        _id_year_og_dict[key] = _id_year_dict[key]

update_year = df['Case Id'].map(_id_year_og_dict) 

## Material 
# Create dictionary of material with respect to the case id
_id_mat_dict =  {_id: mat for _id, mat in zip(case_id, material)}

# Dictionary of the existing top-level file
_id_mat_og_dict = {_id: mat_og for _id, mat_og in zip (case_id_og, material_og)}

# Update material of the top-level dictionary
for key, value in _id_mat_og_dict.items():
    if (_id_mat_dict.get(key)) != None:
        _id_mat_og_dict[key] = _id_mat_dict[key]

update_mat = df['Case Id'].map(_id_mat_og_dict) 

  
## Construction
# Create dictionary of construction type with respect to the case id
_id_construct_dict =  {_id: construct for _id, construct in zip(case_id, construction)}

# Dictionary of the existing top-level file
_id_construct_og_dict = {_id: construct_og for _id, construct_og in zip (case_id_og, construction_og)}

# Update construction type of the top-level dictionary
for key, value in _id_construct_og_dict.items():
    if (_id_construct_dict.get(key)) != None:
        _id_construct_og_dict[key] = _id_construct_dict[key]

update_construct = df['Case Id'].map(_id_construct_og_dict) 


## Average Daily Traffic
# Create dictionary of average daily traffic with respect to the case id
_id_adt_dict =  {_id: adt for _id, adt in zip(case_id, ADT)}

# Dictionary of the existing top-level file
_id_adt_og_dict = {_id: adt_og for _id, adt_og in zip (case_id_og, ADT_og)}

# Update average daily traffic of the top-level dictionary
for key, value in _id_adt_og_dict.items():
    if (_id_adt_dict.get(key)) != None:
        _id_adt_og_dict[key] = _id_adt_dict[key]

update_adt = df['Case Id'].map(_id_adt_og_dict) 


## Average Daily Truck Traffic
# Create dictionary of average daily truck traffic with respect to the case id
_id_adtt_dict =  {_id: adtt for _id, adtt in zip(case_id, ADTT)}

# Dictionary of the existing top-level file
_id_adtt_og_dict = {_id: adtt_og for _id, adtt_og in zip (case_id_og, ADTT_og)}

# Update average daily truck traffic of the top-level dictionary
for key, value in _id_adtt_og_dict.items():
    if (_id_adtt_dict.get(key)) != None:
        _id_adtt_og_dict[key] = _id_adtt_dict[key]

update_adtt = df['Case Id'].map(_id_adtt_og_dict) 


## Deck
# Create dictionary of deck with respect to the case id
_id_dec_dict =  {_id: dec for _id, dec in zip(case_id, deck)}

# Dictionary of the existing top-level file
_id_dec_og_dict = {_id: dec_og for _id, dec_og in zip (case_id_og, deck_og)}

# Update deck of the top-level dictionary
for key, value in _id_dec_og_dict.items():
    if (_id_dec_dict.get(key)) != None:
        _id_dec_og_dict[key] = _id_dec_dict[key]

update_deck = df['Case Id'].map(_id_dec_og_dict) 


## Substructure
# Create dictionary of substructure with respect to the case id
_id_sub_dict =  {_id: sub for _id, sub in zip(case_id, substructure)}

# Dictionary of the existing top-level file
_id_sub_og_dict = {_id: subs_og for _id, subs_og in zip (case_id_og, sub_og)}

# Update subtructure of the top-level dictionary
for key, value in _id_sub_og_dict.items():
    if (_id_sub_dict.get(key)) != None:
        _id_sub_og_dict[key] = _id_sub_dict[key]

update_sub = df['Case Id'].map(_id_sub_og_dict) 


## Superstructure
# Create dictionary of year built with respect to the case id
_id_super_dict =  {_id: super_ for _id, super_ in zip(case_id, superstructure)}

# Dictionary of the existing top-level file
_id_super_og_dict = {_id: super_og for _id, super_og in zip (case_id_og, sup_og)}

# Update superstructure of the top-level dictionary
for key, value in _id_super_og_dict.items():
    if (_id_super_dict.get(key)) != None:
        _id_super_og_dict[key] = _id_super_dict[key]

update_super = df['Case Id'].map(_id_super_og_dict) 


# Update df dataframe with new values 
df['Longitude'] = update_longitude
df['Latitutde'] = update_latitude
df['Year Built'] = update_year
df['Superstructure'] = update_super
df['Substructure'] = update_sub
df['Deck'] = update_deck
df['Construction Type'] = update_construct
df['Material'] = update_mat
df['ADT'] = update_adt
df['ADTT'] = update_adtt

# Add new columns
df['2018'] = year
df['ADT.27'] = update_adt
df['ADTT.27'] = update_adtt
df['Deck.27'] = update_deck
df['Superstructure.27'] = update_super
df['Substructure.27'] = update_sub


# rearrange columns
columns = ['Case Id', 'Latitude', 'Longitude', 'Year Built', 'Material',
           'Construction Type', 'ADT', 'ADTT', 'Deck', 'Superstructure', 'Substructure',
           '1992', 'ADT.1','ADTT.1', 'Deck.1', 'Superstructure.1', 'Substructure.1',
           '1993', 'ADT.2','ADTT.2', 'Deck.2', 'Superstructure.2', 'Substructure.2',
           '1994', 'ADT.3','ADTT.3', 'Deck.3', 'Superstructure.3', 'Substructure.3',
           '1995', 'ADT.4','ADTT.4', 'Deck.4', 'Superstructure.4', 'Substructure.4',
           '1996', 'ADT.5','ADTT.5', 'Deck.5', 'Superstructure.5', 'Substructure.5',
           '1997', 'ADT.6','ADTT.6', 'Deck.6', 'Superstructure.6', 'Substructure.6',
           '1998', 'ADT.7','ADTT.7', 'Deck.7', 'Superstructure.7', 'Substructure.7',
           '1999', 'ADT.8','ADTT.8', 'Deck.8', 'Superstructure.8', 'Substructure.8',
           '2000', 'ADT.9','ADTT.9', 'Deck.9', 'Superstructure.9', 'Substructure.9',
           '2001', 'ADT.10','ADTT.10', 'Deck.10', 'Superstructure.10', 'Substructure.10',
           '2002', 'ADT.11','ADTT.11', 'Deck.11', 'Superstructure.11', 'Substructure.11',
           '2003', 'ADT.12','ADTT.12', 'Deck.12', 'Superstructure.12', 'Substructure.12',
           '2004', 'ADT.13','ADTT.13', 'Deck.13', 'Superstructure.13', 'Substructure.13',
           '2005', 'ADT.14','ADTT.14', 'Deck.14', 'Superstructure.14', 'Substructure.14',
           '2006', 'ADT.15','ADTT.15', 'Deck.15', 'Superstructure.15', 'Substructure.15',
           '2007', 'ADT.16','ADTT.16', 'Deck.16', 'Superstructure.16', 'Substructure.16',
           '2008', 'ADT.17','ADTT.17', 'Deck.17', 'Superstructure.17', 'Substructure.17',
           '2009', 'ADT.18','ADTT.18', 'Deck.18', 'Superstructure.18', 'Substructure.18',
           '2010', 'ADT.19','ADTT.19', 'Deck.19', 'Superstructure.19', 'Substructure.19',
           '2011', 'ADT.20','ADTT.20', 'Deck.20', 'Superstructure.20', 'Substructure.20',
           '2012', 'ADT.21','ADTT.21', 'Deck.21', 'Superstructure.21', 'Substructure.21',
           '2013', 'ADT.22','ADTT.22', 'Deck.22', 'Superstructure.22', 'Substructure.22',
           '2014', 'ADT.23','ADTT.23', 'Deck.23', 'Superstructure.23', 'Substructure.23',
           '2015', 'ADT.24','ADTT.24', 'Deck.24', 'Superstructure.24', 'Substructure.24',
           '2016', 'ADT.25','ADTT.25', 'Deck.25', 'Superstructure.25', 'Substructure.25',
           '2017', 'ADT.26','ADTT.26', 'Deck.26', 'Superstructure.26', 'Substructure.26',
           '2018', 'ADT.27','ADTT.27', 'Deck.27', 'Superstructure.27', 'Substructure.27',
           ]

# Arranging df columns
df = df[columns]
df = df[1:]

# Saving df_top_file
df.to_csv("new_top_file.csv", index=False)

# Use the newly saved and modified new_top_file as input
inputFileName = "new_top_file.csv"

# Use the NBI inspection data file to extract columns
headerFileName = "NBI Inspections Data - 131.csv"
outputFileName = "NBI Inspections Data - 131_modified.csv"

# Extract header/column name
with open(headerFileName, 'r') as headerfile:
    headers = headerfile.readlines()[0]


# Modify and add new columns
with open(inputFileName, 'r') as inFile, open(outputFileName, 'w', newline ='') as outFile:
    r = csv.reader(inFile)
    w = csv.writer(outFile)
    
    lines_reader  = inFile.readlines()
    new_column = headers.split(",")[:-2] + ['2018', 'ADT', 'ADTT', 'Deck', 'Superstructure', 'Substructure']
    new_column = [word.strip('"') for word in new_column]
    new_column[0] = 'Case Id'
    w.writerow(new_column)
    
    for row in lines_reader[1:]:
        write_row = row.split(",")
        write_row[-1] = write_row[-1].strip()
        w.writerow(write_row)

