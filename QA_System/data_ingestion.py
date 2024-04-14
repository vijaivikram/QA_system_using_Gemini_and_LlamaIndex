from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging


def load_data(data):
    """
    Load PDF docs from a directory

    Parameters:
    - data(str): Path to the directory containing the PDf files

    Returns:
    - A list of loaded PDF docs. Type of docs may vary.

    """

    try:
        logging.info('Data Ingestion started')
        loader = SimpleDirectoryReader('Data')
        documents = loader.load_data()
        logging.info('Data Ingestion completed')
        
        
        return documents
    except Exception as e:
        logging.info('Exception in data ingestion')
        raise customexception(e,sys)