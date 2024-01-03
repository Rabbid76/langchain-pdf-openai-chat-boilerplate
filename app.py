from langchain.agents.agent_toolkits import (create_vectorstore_agent, VectorStoreToolkit, VectorStoreInfo)
from langchain.callbacks.base import BaseCallbackHandler
from langchain_community.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.schema import HumanMessage
from langchain.vectorstores import Chroma
import streamlit as st
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

openai_key = None # YOUR OPENAI KEY HERE'
if openai_key is not None:
    os.environ['OPENAI_API_KEY'] = openai_key

persist_directory = './chroma_db'

llm = OpenAI(temperature = 0.1, verbose = True)
embeddings = OpenAIEmbeddings()
db = Chroma(persist_directory = persist_directory, embedding_function = embeddings)

vectorstore_info = VectorStoreInfo(name= 'pdf_report', description = 'report in PDF format', vectorstore = db)
toolkit = VectorStoreToolkit(vectorstore_info = vectorstore_info)

agent_executor = create_vectorstore_agent(llm=llm, toolkit=toolkit, verbose=True)

st.title("ChatGPT like PDF chatbot")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = agent_executor.run(prompt)
        message_placeholder.markdown(full_response)

    st.session_state.chat_history.append({'user': prompt, 'bot': full_response})    
    st.session_state.messages.append({"role": "assistant", "content": full_response})