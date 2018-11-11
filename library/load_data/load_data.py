''' Loads json from path and returns pandas dataframe '''
import os
import sys
import pandas as pd

#Package path
AUTOCOMPLETE = os.path.abspath(__file__ + "/../../../")

# Insert library path to import log_setup
sys.path.insert(0, "{}/library/".format(AUTOCOMPLETE))

#Create logger for module
from log_setup import log_setup as ls
logger = ls.log_setup(__name__)

chat_data = "sample_conversations.json"

class LoadData():
    '''
    Loads json from path. Note: Assumes specific json file in data directory.
    A more generalized data ingest is desireable for production code.

    Returns pandas dataframe.
    '''
    def __init__(self):
        try:
            self.DATA_PATH = "{}/data/{}".format(AUTOCOMPLETE, chat_data)
        except Exception as e:
            logger.exception(e)
