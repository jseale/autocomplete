''' Tests load_data.LoadData'''
import os
import sys

#Package path
AUTOCOMPLETE = os.path.abspath(__file__ + "/../../")

# Insert library path to import log_setup
sys.path.insert(0, "{}/library/".format(AUTOCOMPLETE))

from load_data import load_data as ld

def test_data_path():
    ''' Asserts LoadData has attribute DATA_PATH '''
    load_data = ld.LoadData()
    assert load_data.DATA_PATH
