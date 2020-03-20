"""Contain functions to manipulate and derive new data"""
import pandas as pd
import numpy as np
import maps

__author__ = 'Akshay Kale'
__copyright__ = 'GPL'
__credit__ = []
__email__ = 'akale@unomaha.edu'

class Data:
    def __init__(self):
        pass

    def mapper(self, keys):
        """ Creates dictionary """
        pass

    def get_values(self, keys, dictionary):
        """ Return a list of values and keys """
        return [dictionary[key] for key in keys]

    def create_dictionary(self, keys, values):
        return {key: value for key, value in zip(keys, values)}

    def create_latest_maps(survey_records, columns, key):
        """
        Returns dictionary of key : lastest value of the column
        for example:
                    structure number (key): lastest value of the deck (value)
        Args:
            key (string):
            survey_records (pandas dataframe):
        
        Returns:
            all_dict (dict):
        
        """
        # Initialize list
        all_dict = []
        for col in columns:
            df = survey_records[[key, col]]
            struct_dict = {i:0 for i in df[key]}
       
            for k, v in zip(df[key], df[col]):
                struct_dict[k] = v
            all_dict.append(struct_dict)  
    
        return all_dict

    def create_list_of_maps(survey_records, columns, key):
        """
        Returns dictionary of key (string) : list value of the column (list)
        for example:
                structure number (key): list of value of the deck (value)
        Args:
            key (string):
            survey_records (pandas dataframe):
    
        Returns:
            all_dict (dict):
    
        """
    
        # Initialize list
        all_dict = []
    
        for col in columns:
            df = survey_records[[key, col]]
            struct_dict_list = {i:[] for i in df[key]}
            for k, v in zip(df[key], df[col]):
                struct_dict_list[k].append(v)
            all_dict.append(struct_dict_list)        
    
        return all_dict

        # calling of the functions



    def create_groupby_df(key, df, list_of_maps):
        """
        Returns Groupby dataframe with values of the columns arranged according to their time series.
    
        Args:
            key (string): Key is the groupby criteria
            df (dataframe): the existing dataframe of lose individual records
            list_of_map (list): list of dictionary of columns in the df.
                            Each column is mapped to the key such tha'key' as the key,
                            and value as the 'value' of the column
        Returns:
            df_new (dataframe): a dataframe of columns grouped by key 'structure number'
        """
        #Select columns
        columns = list(df.columns)
    
        # initialize empty dataframe
        df_new = pd.DataFrame(columns = columns)
    
        # Setting column of structure number
        df_new[key] = df[key].unique()
    
        # mapping other column values to the structure number
        for number, col in enumerate(columns[1:]):
            df_new[col] = df_new[key].map(list_of_maps[number])
    
        return df_new   
    

    def transfrom_timeseries(self):
        pass
