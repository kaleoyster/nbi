"""
title: Integrator of the NBI dataset
author: Akshay Kale
description: This script maintains individual scripts
"""
import pandas as pd
from collections import defaultdict
import json

SAVE_AT = "/Users/AkshayKale/Google Drive/Data/sample/"
SNOWFALL_FREEZE = "/Users/AkshayKale/Google Drive/Data/scripts/climate_reduced.csv"

def sampler(df, name, sample=5, save_at=SAVE_AT):
    save_at = save_at + name
    return df.head(sample).to_csv(save_at)

def create_map(structure_number, values):
    structure_value_map = defaultdict(list)
    for struc_no, value in zip(structure_number, values):
        structure_value_map[struc_no].append(value)
    return structure_value_map

def create_jsondump(snow_map, freeze_map):
    # Create a list of years for the stucture number
    # Compare the list of years to other dataset
    # Create a list of jsondump and store in the MONGO DB
    structurenumber = 'Apple'
    snowfall = 19
    freezethaw = 20
    json_dump = json.dumps( {
                            'structurenumber': structurenumber,
                            'year':year,
                            'snowfall': snowfall,
                            'freezethaw':freezethaw

    json_dump = json.dumps( {
                            'structurenumber': structurenumber,
                            'year':year,
                            'snowfall': snowfall,
                            'freezethaw':freezethaw
                            })
                        })
    # Retrieve from the mongodb

    # Major Idea:
    # Create se# 
    return json_dump

def main():
   df = pd.read_csv(SNOWFALL_FREEZE, low_memory=True)
   structure_number = df['structure_number'] 
   freezethaw = df['NO_OF_FREEZE_THAW_CYCLES']
   snowfall = df['no_of_snowfalls']

   #Create maps
   struct_freeze = create_map(structure_number, freezethaw)
   struct_snowfall = create_map(structure_number, snowfall)

   print(len(struct_freeze))
   print(len(struct_snowfall))

  # print(freezethaw.head())
  # print(snowfall.head())
  # print(structure_number.head())

def test():
    print(create_jsondump(19, 20))
     



if __name__=='__main__':
    #main()
    test()
    
