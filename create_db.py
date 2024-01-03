from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.vectorstores import Chroma
import os
import pathlib
import sys

os.chdir(pathlib.Path(__file__).resolve().parent)

collection_name = 'PDF-collection'
persist_directory = './chroma_db'

def create_db(path_to_pdfs):
    print('load PDF documents from {path_to_pdfs} ...')
    loader = PyPDFDirectoryLoader(path_to_pdfs)
    documents = loader.load()
    print(f'... found {len(documents)} pages')
    embeddings = OpenAIEmbeddings()
    Chroma.from_documents(documents, embeddings, collection_name = collection_name, persist_directory = persist_directory)
    print('... db created')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise RuntimeError('usage: create_db.py <path_to_pdfs> [<openai_key>]')

    path_to_pdfs = sys.argv[1]
    if pathlib.Path(path_to_pdfs).is_dir() == False:
        raise RuntimeError(f'{path_to_pdfs} is not a directory')
    if len(sys.argv) > 2:
        openai_key = sys.argv[2]
        print(f'using OpenAI key: {openai_key}')
        os.environ['OPENAI_API_KEY'] = openai_key

    create_db(path_to_pdfs)
