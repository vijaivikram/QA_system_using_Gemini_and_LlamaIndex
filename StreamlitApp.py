import streamlit as st
from QA_System.data_ingestion import load_data
from QA_System.embedding import download_gemini_embedding
from QA_System.model_api import load_model

def main():
    st.set_page_config("QA with Docs")

    doc = st.file_uploader("Upload your documents here!")

    st.header('QA with documents(Information Retrieval)')

    user_question = st.text_input('Ask any question from your docs')

    if st.button('Submit & Process'):
        with st.spinner('Processing...'):
            document = load_data(doc)
            model = load_model()
            query_engine = download_gemini_embedding(model,document)

            response = query_engine.query(user_question)

            st.write(response.response)

    
if __name__ == '__main__':
    main()