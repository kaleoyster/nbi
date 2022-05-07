""" -------------------------------------------------
description: functions to query NBI mongodb,
    and generate dataset.
author: Akshay Kale
Data: February 22, 2020
-------------------------------------------------"""

__author__ = 'Akshay Kale'
__copyright__ = 'GPL'
__email__ = 'akale@unomaha.edu'

from nbi_data_chef import *
#from precipitation import *
#from snowfall_freezethaw import *

def main():
    """
    Config file
    """
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
                "structureType":"$structureTypeMain.typeOfDesignConstruction",
                "material":"$structureTypeMain.kindOfMaterialDesign",
                "wearingSurface":"$structureTypeMain.kindOfDesignConstruction",
                "coordinates":"$loc.coordinates"
            }

    # Select states:
    states = ['31'] # Nebraska

    # years:
    years = [year for year in range(1992, 2020)]

    # process precipitation data
    #structBdsMap, structPrecipMap = process_precipitation()

    # Process snowfall and freezethaw data
    #structSnowMap, structFreezeMap = process_snowfall()

    # Query
    #individualRecords = query(fields, states, years, collection)

    individual_records = sample_records()

    # Fixing coordinate by reformating the
    individual_records = fix_coordinates(individual_records)

    # Group records
    groupedRecords = group_records(individual_records, fields)
    groupedRecords = segmentize(groupedRecords)
    groupedRecords = reorganize_segmented_data(groupedRecords)
    #print(groupedRecords)

    # Segment the records
    #groupedRecords = segement(groudRecords, component='deck')

    # Compute baseline differnce score:
    groupedRecords, baselineDeck = compute_bds_score(groupedRecords,
                                                     component='deck')

    groupedRecords, baselineSubstructure = compute_bds_score(groupedRecords,
                                                             component='substructure')

    groupedRecords, baselineSuperstructure = compute_bds_score(groupedRecords,
                                                               component='superstructure')
    ## Creating BDS map
    deckBDSMap = create_map(groupedRecords, column='deckBDSScore')
    substructureBDSMap = create_map(groupedRecords, column='substructureBDSScore')
    superstructureBDSMap = create_map(groupedRecords, column='superstructureBDSScore')

    ## Compute slope
    groupedRecords = compute_deterioration_slope(groupedRecords, component='deck')
    groupedRecords = compute_deterioration_slope(groupedRecords, component='substructure')
    groupedRecords = compute_deterioration_slope(groupedRecords, component='superstructure')
    ## Creating slope map
    deckSlopeMap = create_map(groupedRecords, column='deckDeteriorationScore')
    substructSlopeMap = create_map(groupedRecords, column='substructureDeteriorationScore')
    superstructureSlopeMap = create_map(groupedRecords, column='superstructureDeteriorationScore')
    print(groupedRecords)
    #individualRecords = integrate_ext_dataset_list(deckBDSMap,
    #                                              individualRecords,
    #                                               'deckBDSScore')

    #individualRecords = integrate_ext_dataset_list(substructureBDSMap,
    #                                               individualRecords,
    #                                               'substructureBDSScore')

    #individualRecords = integrate_ext_dataset_list(superstructureBDSMap,
    #                                               individualRecords,
    #                                               'superstructureBDSScore')

    #individualRecords = integrate_ext_dataset_list(deckBDSMap,
    #                                               individualRecords,
    #                                               'deckDeteriorationScore')

    #individualRecords = integrate_ext_dataset_list(substructureBDSMap,
    #                                               individualRecords,
    #                                               'substructureDeteriorationScore')

    #individualRecords = integrate_ext_dataset_list(superstructureBDSMap,
    #                                               individualRecords,
    #                                               'superstructureDeteriorationScore')

    ## Save to the file
    #csvfile = 'testing-segmentation.csv'
    #tocsv_list(individualRecords, csvfile)
    #create_df(baselineDeck, baselineSubstructure, baselineSuperstructure)

if __name__=='__main__':
     main()
