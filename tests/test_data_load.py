''' Tests data_load.DataLoad. To scale and not slow down unit test runs,
use as integration tests. '''
import os
import sys
import pytest

#Prefix, data_load path insertion for import
AUTOC = os.path.abspath(__file__ + "/../../")
sys.path.insert(0, "{}/library/data_load".format(AUTOC))

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
