# LangChain PDF OpenAI Chat Boilerplate

The application consists of two scripts.
The first generates a [Chroma](https://www.trychroma.com/) database from a given set of PDFs. The database is created in the subfolder "chroma_db".
The second implements a [Streamlit](https://docs.streamlit.io/) web chat bot, based on the database, which can be used to ask questions related to the content of the PDFs.

An OpenAI key is required for this application (see [Create an OpenAI API key](https://gptforwork.com/help/gpt-for-docs/setup/create-openai-api-key)).
The OpenAI key must either be set in the environment variable `OPENAI_API_KEY` or must be passed as an argument to the scripts.

## Required python packages

`chromadb`, `langchain`, `langchain-community`, `openai`, `pypdf`, `streamlit`, `tiktoken`


## Create the database

To create the database, the "create_db.py" script must be executed and a file path to the PDFs must be passed as the first argument.
The second argument is optional and can be the OpenAI key.

```none
python3 create_db.py <path_to_pdfs> [<openai_key>]
```

## Run the chat bot

The OpenAI key must be set in the environment variable `OPENAI_API_KEY` or set in the "app.py" script.
To run the chat bot, the "app.py" script must be executed.

```none
streamlit run app.py
```

## Resources

- [LangChain - Introduction](https://python.langchain.com/docs/get_started/introduction)
- [LangChain - Chroma](https://python.langchain.com/docs/integrations/vectorstores/chroma)  
- [LangChain - PDF](https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf)
- [LangChain - Agents](https://python.langchain.com/docs/modules/agents/)
- [LangChain - Custom callback handlers](https://python.langchain.com/docs/modules/callbacks/custom_callbacks)
- [Streamlit - Documentation](https://docs.streamlit.io/#streamlit-documentation)
- [Streamlit - Build a ChatGPT-like app](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps#build-a-chatgpt-like-app)
