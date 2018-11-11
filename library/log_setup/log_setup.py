''' Creates logger with filehandler for a given module.'''
import os
import logging

PATH  = os.path.abspath(__file__ + "/../../../logs")

#Sets up Logging
def log_setup(logger_name):

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
