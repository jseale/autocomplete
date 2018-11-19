''' Tests autocomplete.autocompleter.'''
import os
import sys
import re
import numpy as np

#Prefix, path insertion
AUTOC = os.path.abspath(__file__ + "/../../")
sys.path.insert(0, "{}/library/autocomplete".format(AUTOC))
import autocompleter as a

def test_prefix():
    """ Asserts that prefix.compiled is a regex pattern. """
    prefix = a.Prefix("£®🚴")
    assert isinstance(prefix.compiled, re.Pattern)

def test_autocompleter():
    """ Asserts that autcompleter returned the top number of completions allowed. """
    autoc = a.Autocompleter()
    completions = autoc.generate_completions("he")
    assert np.equal(len(completions), 5)
