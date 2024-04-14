from llama_index.embeddings.gemini import GeminiEmbedding

from QA_System.data_ingestion import load_data

import sys
from exception import customexception
from logger import logging

def download_gemini_embedding(model,document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings

    Returns:
    - VectorStoreIndex: An Index of vector embeddings for efficient similiartity search

    """

    try:
        
        
    except Exception as e:
        logging.info('Exception in Embedding')
        raise customexception(e,sys)