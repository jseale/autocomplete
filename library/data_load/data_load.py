''' Loads json from path and returns pandas dataframe '''
import os
import sys
import json
import pandas as pd

#Package path
AUTOC = os.path.abspath(__file__ + "/../../../")

# Insert library path to import log_setup
sys.path.insert(0, "{}/library/log_setup".format(AUTOC))

#Create logger for module
import log_setup as ls
logger = ls.log_setup('data_load')

#JSON Chat data file name
chat_data = "sample_conversations.json"

class DataLoad():
    '''
    Loads json from path. Note: Assumes specific json file in data directory.
    A more generalized ingest is desireable for production code.

    The DataLoad.json attribute is used in the data_prep module.
    '''

    def __init__(self):
        logger.info("Creating instance of DataLoad")
        self.path = f"{AUTOC}/data/{chat_data}"
        self.__json_load()

    def json_load(self):
        ''' Loads json into json attribute of a DataLoad instance. '''
        with open(self.path) as f:
            try:
                self.json = json.load(f)
                logger.info("Loading json")
            except ValueError as e:
                logger.exception(str(e))

    __json_load = json_load

