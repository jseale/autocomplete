''' Tests data_prep.DataPrep.'''
import os
import sys
import numpy as np
import pytest

#Prefix, path insertion
AUTOC = os.path.abspath(__file__ + "/../../")
sys.path.insert(0, "{}/library/data_prep".format(AUTOC))

@pytest.fixture(scope="module")
def get_chats():
    '''Returns part of chats data '''
    chats = {'NumTextMessages': 22264,
            'Issues': [{'IssueId': 1,
                        'CompanyGroupId': 1,
                        'Messages': [{'IsFromCustomer': True,
                                      'Text': "Hi! I placed an order on your website."},
                                     {'IsFromCustomer': True,
                                      'Text': 'I think I used my email address to log in.'}]},
                       {'IssueId': 30001,
                        'CompanyGroupId': 40001,
                        'Messages': [{'IsFromCustomer': True, 'Text': 'Hello'},
                                     {'IsFromCustomer': False,
                                      'Text': 'Hello Werner how may I help you today?'}]}]}
    return chats


def test_data_prep(get_chats):
    """ Asserts that DataPrep.outbound_messages contains one item.
    Only one of the messages in the chats fixture is not from a customer. """
    from data_prep import DataPrep
    dp = DataPrep(get_chats)
    assert np.equal(len(dp.outbound_messages), 1)
