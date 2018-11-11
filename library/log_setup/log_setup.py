''' Logging functionality:
    Checks for and creates logs directory if not extant;
    Creates logger with filehandler for modules.'''
import os
import logging

def log_path():
    ''' Functionality: Checks to see if log directory exists
        Returns: Logs directory path '''
    if not os.path.exists(os.path.abspath("{}/../../../logs".format(__file__))):
        os.makedirs(os.path.abspath("{}/../../../logs".format(__file__)))

    return os.path.abspath("{}/../../../logs".format(__file__))

def log_setup(logger_name):
    '''Returns formatted logger for a module '''
    #Return log directory path
    PATH = log_path()

    # Create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # Create file handler
    fh = logging.FileHandler('{}/{}.log'.format(PATH, logger_name))
    fh.setLevel(logging.INFO)

    # Set formatter
    formatter = logging.Formatter('%(asctime)s\
                                   %(name)-12s\
                                   %(levelname)-8s\
                                   %(message)s',\
                                   datefmt='%m/%d/%Y %I:%M:%S %p')
    fh.setFormatter(formatter)

    # Add file handler to logger
    logger.addHandler(fh)

    return logger
