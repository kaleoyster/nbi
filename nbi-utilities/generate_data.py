""" -------------------------------------------------
description: functions to query NBI mongodb,
    and generate dataset.
author: Akshay Kale
Data: February 22, 2020
-------------------------------------------------"""

__author__ = 'Akshay Kale'
__copyright__ = 'GPL'
__email__ = 'akale@unomaha.edu'

import json
import numpy as np
from pymongo import MongoClient
from tqdm import tqdm
from datetime import date
from collections import defaultdict
from collections import Counter
from nbi_data_chef import *

#from precipitation import *
#from snowfall_freezethaw import *

def main():
    nbiDB = get_db()
    collection = nbiDB['nbi']

    # select features:
    fields = {
                "_id":0,
                "year":1,
                "structureNumber":1,
                "yearBuilt":1,
                "yearReconstructured":1,
                "averageDailyTraffic":1,
                "avgDailyTruckTraffic":1,
                "deck":1,
                "substructure":1,
                "superstructure":1,
                "owner":1,
                "maintainanceResponsibility":1,
                "designLoad":1,
                "operatingRating":1,
                "structureLength":1,
                "numberOfSpansInMainUnit":1,
                "scourCriticalBridges":1,
                "material":"$structureTypeMain.kindOfMaterialDesign",
                "wearingSurface":"$structureTypeMain.kindOfDesignConstruction",
                "longitude":"$loc.coordinates[0]",
                "latitude":"$loc.coordinates[1]"
            }

    # select states:
    states = ['31'] # Nebraska

    # years:
    years = [year for year in range(1992, 2020)]

    # process precipitation data
    #structBdsMap, structPrecipMap = process_precipitation()

    # process snowfall and freezethaw data
    #structSnowMap, structFreezeMap = process_snowfall()

    # query
    individualRecords = query(fields, states, years, collection)
    #individualRecords = sample_records()

    # group records
    groupedRecords = group_records(individualRecords, fields)

    # Compute baseline differnce score:
    groupedRecords, baselineDeck = compute_bds_score(groupedRecords,
                                                     component='deck')

    groupedRecords, baselineSubstructure = compute_bds_score(groupedRecords,
                                                             component='substructure')

    groupedRecords, baselineSuperstructure = compute_bds_score(groupedRecords,
                                                               component='superstructure')
    # Creating BDS map
    deckBDSMap = create_map(groupedRecords, column='deckBDSScore')
    substructurreBDSMap = create_map(groupedRecords, column='substructureBDSScore')
    superstructureBDSMap = create_map(groupedRecords, column='superstructureBDSScore')

    individualRecords = integrate_ext_dataset_list(deckBDSMap,
                                                   individualRecords,
                                                   'deckBDSScore')

    individualRecords = integrate_ext_dataset_list(substructureBDSMap,
                                                   individualRecords,
                                                   'substructureBDSScore')

    individualRecords = integrate_ext_dataset_list(superstructureBDSMap,
                                                   individualRecords,
                                                   'superstructureBDSScore')

    # Save to the file
    print(individualRecords)
    csvfile = 'nebraska.csv'
    tocsv_list(individualRecords, csvfile)
    create_df(baselineDeck, baselineSubstructure, baselineSuperstructure)

if __name__=='__main__':
     main()
