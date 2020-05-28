"""Contain functions to manipulate and derive new data"""
import pandas as pd
import numpy as np
import datetime
from collections import defaultdict
from collections import deque

__author__ = 'Akshay Kale'
__copyright__ = 'GPL'
__credit__ = []
__email__ = 'akale@unomaha.edu'

class DataChef:
    """ Contains function that operate on list, dictionary, dataframe, and series """
    def __init__(self):
        pass

    def get_values(self, keys, dictionary):
        # PERFECT
        """ Return a list of values for a given key """
        return [dictionary[key] for key in keys]

    def create_dictionary(self, keys, values):
        # PERFECT
        """ Return a dictionary
        Args: keys (list)
              value (list)

        Returns: a dicitonary (dict) """
        return dict(zip(keys, values))

    def create_maps(self, df, columns, key, type_of_maps='list'):
        # PERFECT
        """
        Returns dictionary of key : lastest value of the column
        for example:
                    structure number (key): lastest value of the deck (value)
        Args:
            key (string):
            survey_records (pandas dataframe):

        Returns:
            list_of_dict (list):  a list of dictionaries

        """
        def create_dictionary(list_of_keys, list_of_values):
            # PERFECT 
            df_keys = dataframe_temp[list_of_key]
            df_values = dataframe_temp[list_of_values]

            if type_of_maps == 'list':
                dictionary = defaultdict(list)
                for key_temp, value_temp in zip(df_keys, df_values):
                    dictionary[key_temp].append(value_temp)
            else:
                dictionary = defaultdict()
                for key_temp, value_temp in zip(df_keys, df_values):
                    dictionary[key_temp] = value_temp

            return dictionary

            list_of_dictionaries = []
            for col in columns:
                dataframe_temp = dataframe[[key, col]]
                temp_dict  = create_dictionary(dataframe[key], dataframe[col])
                list_of_dictionaries.append(temp_dict)

            return list_of_dictionaries


    def create_groupby_df(self, key, df, list_of_maps):
        # PERFECT
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

    def is_same_elements(self, elements):
        """ Returns True if all the element are same """
        return all(elem == elements[0] for elem in elements)

    def calculate_age(self, list_of_year_built, list_of_survey, kind='survey'):
        """ Returns age of the of the bridge """
        year_built = np.array(list_of_year_built)
        year_survey = np.array(list_of_survey)

        now = datetime.datetime.now()

        if kind == 'survey':
            return year_survey - year_built
        elif kind == 'current':
            return  now.year - year_built

    def categorizeBridgesByADT(ADT):
        # PERFECT
        """ returns A list of class of the bridge as define by Author in so and so """
        class_of_bridges_adt = []
        for adt in ADT:
            if adt < 100:
                class_of_bridges_adt.append('Very Light')
            elif 100 <= adt < 1000:
                class_of_bridges_adt.append('Light')
            elif 1000 <= adt < 5000:
                class_of_bridges_adt.append('Moderate')
            elif 5000 <= adt:
                class_of_bridges_adt.append('Heavy')
            else:
                class_of_bridges_adt.append('IDK')
        return class_of_bridges_adt


    def categorizeBridgesByADTT(ADTT): 
        # PERFECT
        """ returns A list of class of the bridge as define by Author in so and so """
        class_of_bridges_adtt = []
        for adtt in ADTT:
            if adtt < 100:
                class_of_bridges_adtt.append('Light')     
            elif 100 <= adtt < 500:
                class_of_bridges_adtt.append('Moderate')
            elif 500 <= adtt:
                class_of_bridges_adtt.append('Heavy')
            else:
                class_of_bridges_adtt.append('IDK')
        return class_of_bridges_adtt
