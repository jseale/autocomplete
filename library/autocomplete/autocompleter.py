""" Receives user-generated prefix and returns autocompletion suggestions """
import os
import sys
import re
from collections import Counter

#Get package prefix; insert library on path for imports
AUTOC = os.path.abspath(__file__ + "/../../../")
sys.path.insert(0, "{}/library".format(AUTOC))
from data_load import data_load as dl
from data_prep import data_prep as dp

#Create logger for module
from log_setup import log_setup
logger = log_setup('autocompleter')

class Prefix():
    """ Ensures utf-8 encoding and compiles a
        regex pattern that ignores c
        Instantiated in autocompleter.generate_completions
        to process strings for autocompletion."""

    def __init__(self, prefix_string):
        """ Initializes and sets attributes: prefix string (Prefix.string)
        and compiled prefix string (Prefix.compiled)"""
        self.string = prefix_string
        self.__encode_prefix()
        self.__compile_prefix()

    def encode_prefix(self):
        """ Encodes user-input string as utf-8. """
        try:
            self.encoded = self.string.encode("utf-8")
            logger.info("Prefix encoded.")
        except Exception as e:
            logger.exception(str(e))

    __encode_prefix = encode_prefix

    def compile_prefix(self):
        """ Compiles user-input string as
        regex pattern to match previously generated outbound
        messages with. """
        try:
            self.compiled = re.compile(self.encoded, re.I)
            logger.info("Prefix compiled.")
        except Exception as e:
            logger.exception(str(e))

    __compile_prefix = compile_prefix

class Autocompleter():
    """ Prepares message corpus for use in autocompletion;
        matches outbound messages with prefixes. Returns
        list of autocompletion suggestions. """

    def __init__(self):
        """ Sets messages attribute. """
        self.messages = self.__get_messages()
        #Sets cutoff for how many messages get returned. Cutoff based
        #roughly off 'competetive analysis':
        #https://staff.fnwi.uva.nl/m.derijke/wp-content/papercite-data/pdf/cai-survey-2016.pdf
        self.cutoff = 5

    def get_messages(self):
        """ Loads, preps and returns outbound chat messages as
        the text that gets matched with prefixes for autocomplete. """
        data = dl.DataLoad()
        data_prepped = dp.DataPrep(data.json)
        return data_prepped.outbound_messages

    __get_messages = get_messages

    def top_messages(self, completions, number=1):
        """ Parameters: List of completions obtained in generate_completions,
        and the number of completions you want to return.
        Counts the number of times each message occurs and returns n most
        frequent messages. This should provide a better autocomplete service
        for those searching for common messages."""
        try:
            message_counts = Counter([message for message in completions])
            return [message for message, count in message_counts.most_common(number)]
        except Exception as e:
            logger.exception(str(e))

    __top_messages = top_messages

    def prioritize(self, completions):
        """ Parameter: Completions obtained in generate_completions
        Returns list of up to the top n most common as defined
        by self.cutoff. """
        if len(completions) == 0:
            return completions
        elif len(completions) >= self.cutoff:
            return self.__top_messages(completions, number=self.cutoff)
        else:
            return self.__top_messages(completions, number=len(completions))

    __prioritize = prioritize

    def generate_completions(self, prefix_string):
        """ Parameter: String input (by customer service representative)
        Calls Prefix on string to compile as regex pattern. Matches outbound
        messages at beginning against pattern. Returns list of matches/
        autocompletions. """

        #Set compiled input/prefix
        prefix = Prefix(prefix_string)
        self.prefix = prefix.compiled

        #Return matches against prefix
        try:
            completions = list(self.messages[self.messages.apply(\
                    lambda text: bool(self.prefix.match(text)))])
            return self.__prioritize(completions)
        except Exception as e:
            logger.exception(str(e))
