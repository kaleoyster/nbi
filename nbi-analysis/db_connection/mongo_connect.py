"""Contains functions to connect to Mongo"""
import pymongo import MongoClient

__author__ = "Akshay Kale"
__copyright__ = "GPL"
__email__ = "akale@unomaha.edu"


def connect_to_mongo_nbi(collection_name, connection_string):
    """ Connect to NBI mongodb instance and returns a connection
        Args: (string) collection_name 
              (string) connection_string
        
        Returns: (string) collection """

        Client = MongoClient(connection_sting)
        database = Client.nbi
        return database[collection_name]

    
