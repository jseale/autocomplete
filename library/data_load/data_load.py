''' Loads json from path and returns pandas dataframe '''
import os
import sys
import json

#Get package prefix; insert log_setup on path for import
AUTOC = os.path.abspath(__file__ + "/../../../")
sys.path.insert(0, "{}/library/log_setup".format(AUTOC))

#Create logger for module
from log_setup import log_setup
logger = log_setup('data_load')

#JSON Chat data file name
chat_data = "sample_conversations.json"

# DataLoad assumes specific json file in data directory.
# A more generalized ingest is desireable for production code.
class DataLoad():
    """
    Loads json from path.

    The json attribute is used in the data_prep module.
    """

    def __init__(self):
        logger.info("Creating instance of DataLoad")
        self.__path = f"{AUTOC}/data/{chat_data}"
        self.__json_load()

    def json_load(self):
        """ Loads json into json attribute of a DataLoad instance. """
        try:
            with open(self.__path) as f:
                try:
                    self.json = json.load(f)
                    logger.info("Loading json")
                except ValueError as e:
                    logger.exception(str(e))
        except Exception as e:
            logger.exception(str(e))
    __json_load = json_load
