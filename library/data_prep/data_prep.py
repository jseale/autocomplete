""" Prepares corpus of chats for use in autocompletion service for customer
service representatives."""
import os
import sys
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

#Prefix, and insertion of library path for imports
AUTOC = os.path.abspath(__file__ + "/../../../")
sys.path.insert(0, "{}/library".format(AUTOC))

#Create logger for module
from log_setup import log_setup
logger = log_setup('data_prep')

class DataPrep():
    """Parameters: the json attribute of a DataLoad instance (dl_json)—
       it holds chat data from customer service conversations

       Prepares outbound customer service representatives'
       message text for use in autocompletion.

       Stores messages as self.outbound_messages attribute.

       DataPrep is instantiated in autocompleter.get_messages()"""

    def __init__(self, dl_json):
        self.__data = dl_json
        self.__issues = []
        self.__normalized = {}
        self.__df = pd.DataFrame()
        self.__normalized_bytes = pd.DataFrame()
        self.outbound_messages = pd.Series()

        #Set attributes
        self.__isolate_issues()
        self.__normalize()
        self.__make_df()
        self.__to_bytes()
        self.__get_outbound()

    def isolate_issues(self):
        """Creates list of conversations about issues,
           removing 'NumTextMessages': 22264 from data.

           NumTextMessages was used to confirm that json
           resulting from isolate_issues and normalize functions
           retained all the text messages, as there are 22264
           rows in self.normalized.

           Stores list of conversations surrounding issues
           in self.issues attribute."""
        try:
            self.__issues = [convo for convo in self.__data['Issues']]
            logger.info("Issues obtained.")
        except Exception as e:
            logger.exception(str(e))

    __isolate_issues = isolate_issues

    def normalize(self):
        """Creates json with one row per message;
           each row contains the CompanyGroup and Issue IDs associated
           with each message.

           Stores messages and metadata as json in self.normalized
           attribute. """
        try:
            self.__normalized = json_normalize(self.__issues, \
                    'Messages', ['CompanyGroupId', 'IssueId'])
            logger.info("Issues json normalized.")
        except Exception as e:
            logger.exception(str(e))

    __normalize = normalize

    def make_df(self):
        """ Creates dataframe from self.normalized json.

            Stores messages and metadata as dataframe in self.df attribute."""
        try:
            self.__df = pd.DataFrame(self.__normalized)
            logger.info("DataFrame generated.")
        except Exception as e:
            logger.exception(str(e))

    __make_df = make_df

    def to_bytes(self):
        "Converts text to bytes"
        self.__normalized_bytes = self.__df['Text'].str.encode('utf-8')

    __to_bytes = to_bytes

    # For future chat topic extraction, it would probably be beneficial to keep
    # the conversations with customers intact.
    def get_outbound(self):
        """ Indexes into the chats dataframe at rows in which messages are
            from customer service representatives, in order to create messages
            to return in autocomplete.

            Stores Pandas series of outbound service representative messages
            in self.outbound_messages attribute

            DataPrep.outbound_messages is used as source of text for autocompletions
            in autocompleter.generate_completions. """
        try:
            self.outbound_messages = \
                self.__normalized_bytes.loc[
                    np.where(np.equal(self.__df["IsFromCustomer"], False))]
        except Exception as e:
            logger.exception(str(e))

    __get_outbound = get_outbound
