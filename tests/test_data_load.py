''' Tests data_load.DataLoad. To scale and not slow down unit test runs,
use as integration tests. '''
import os
import sys
import pytest

#Package path
AUTOCOMPLETE = os.path.abspath(__file__ + "/../../")

# Insert library path to import log_setup
sys.path.insert(0, "{}/library/data_load".format(AUTOCOMPLETE))

@pytest.fixture(scope="module")
def chats():
    '''Returns DataLoad instance '''
    from data_load import DataLoad
    return DataLoad()

def test_data_path(chats):
    ''' Asserts that instance of DataLoad has attribute path '''
    assert chats.path

def test_json(chats):
    ''' Asserts that instance of DataLoad has correctly formed json attribute '''
    assert isinstance(chats.json, dict)
