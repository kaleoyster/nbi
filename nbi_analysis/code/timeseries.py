"""
    Contains procedures to create the training and testing data 
    for decision tree analysis
"""
import pandas as pd
from datetime import date
import sys

sys.path.append("..")
import path
from path.paths import *

import data_code
from data_code import *
from data_code.sampler import *
from data_code.maps import * 
from data_code.data import *

__author__ = "Akshay Kale"
__copyright_ = "GPL"
__email__ = "akale@unomaha.edu"

# Path variables
NBIDATA = "/Users/AkshayKale/Documents/github/thesis/1992-2017-timeseries.csv"
SNOWFALL_FREEZE = "/Users/AkshayKale/Google Drive/Data/scripts/climate_reduced.csv"
SAMPLE_PATH = "/Users/AkshayKale/Google Drive/Data/sample"

# Helper function, to create sample of the working data
def create_samples(NBIDATA, SNOWFALL_FREEZE):
    survey_records = pd.read_csv(NBIDATA)
    snowfall_freezethaw = pd.read_csv(SNOWFALL_FREEZE)
    sampler(survey_records, 'survey_sample.csv') 
    sampler(snowfall_freezethaw, 'snowfall_sample.csv')

def main():
    NBI_DATA = SAMPLE_PATH + "/survey_sample.csv"
    SNOWFALL_FREEZE = SAMPLE_PATH + "/snowfall_sample.csv"
    dc = data.DataChef()
    maps = maps.Maps()

    #============================= Import data ================================#
    # NBI records
    survey_records = pd.read_csv(NBI_DATA, low_memory=False)
     
    # Snowfall and freezethaw data
    snowfall_freezethaw = pd.read_csv(SNOWFALL_FREEZE, low_memory=False)
    
    # Precipitation data
    
    #============================ Create maps ================================#
    # Create maps
    bridge_snowfall_map = dc.create_dictionary(snowfall_freezethaw['structure_number'],
                                               snowfall_freezethaw['no_of_snowfalls'])
    
    bridge_freezethaw_map = dc.create_dictionary(snowfall_freezethaw['structure_number'],
                                                 snowfall_freezethaw['NO_OF_FREEZE_THAW_CYCLES'])
     
    #=========================== Column Manipulation =================================#
    # Select columns 

    # New columns
    survey_records['No. of snowfall'] = survey_records['structureNumber'].map(bridge_snowfall_map)
    survey_records['No. of freezethaw'] = survey_records['structureNumber'].map(bridge_freezethaw_map)
    
    # Change columns names
    
    #========================== Transform (timeseries) ========================# 
    dictionary_list = dc.create_maps(survey_records, columns_list, type='list')
    dictionary_latest = dc.create_maps(survey_records, columns_latest, type='latest')    
    
    dictionary = dictionary_list + dictionary_latest

    df['Structure Number'] = survey_records['structureNumber'].unique()

    #================================ Export ==================================#
    df.to_json(SAVE_AT+ 'timeseries_'+ datetime.now().date)
    #print(bridge_snowfall_map)
    #print(bridge_freezethaw_map)
    #print(survey_records)

if __name__ == '__main__':
    #main()
    file_name_all_states_years = str(date.today()) \
                                + '_all_states'    \
                                + '_all_years'     \
                                + '_timeseries.csv'

    print(file_name_all_states_years)
    #create_samples(NBIDATA, SNOWFALL_FREEZE)
