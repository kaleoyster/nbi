"""Contains functions to connect to Mongo"""
from pymongo import MongoClient

__author__ = "Akshay Kale"
__copyright__ = "GPL"
__email__ = "akale@unomaha.edu"


def connect_to_mongo_nbi(collection_name, connection_string):
    """ Description:
            Connect to NBI mongodb instance and returns a connection
        Args:
            (string) collection_name
            (string) connection_string
        Returns:
            (string) collection
    """
    Client = MongoClient(connection_string)
    database = Client.nbi
    return database[collection_name]
