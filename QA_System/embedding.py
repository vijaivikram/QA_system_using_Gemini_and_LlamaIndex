from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core import ServiceContext
from llama_index.core import StorageContext, load_index_from_storage

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
        logging.info('Embedding Started')
        gemini_embed_model = GeminiEmbedding(model_name='models/embedding-001')
        service_context = ServiceContext.from_defaults(llm=model,embed_model=gemini_embed_model,chunk_size=800,chunk_overlap=20)

        index = VectorStoreIndex.from_documents(document,service_context=service_context)
        index.storage_context.persist()

        query_engine = index.as_query_engine()

        return query_engine
        
    except Exception as e:
        logging.info('Exception in Embedding')
        raise customexception(e,sys)