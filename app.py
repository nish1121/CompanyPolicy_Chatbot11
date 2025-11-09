import os
import streamlit as st
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from utils.azure_setup import get_azure_openai_llm
from utils.document_processor import setup_knowledge_base
from config import APP_NAME

# Configure Streamlit page
st.set_page_config(
    page_title=APP_NAME,
    page_icon=":robot_face:",
    layout="wide"
)

# Initialize session state variables
if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "process_complete" not in st.session_state:
    st.session_state.process_complete = False

def setup_conversation_chain(vector_store):
    """Set up the conversation chain with memory and retrieval"""
    llm = get_azure_openai_llm()
    
 # Create memory for conversation
 memory = ConversationBufferMemory(
 memory_key="chat_history",
 return_messages=True
    )
# Define a custom prompt template
    template = """
    You are a helpful assistant for company employees. Your role is to answer questions about company policies, procedures, and provide support.
    Use the following context to answer the question. If you don't know the answer, just say that you don't know, don't try to make up an answer.
    
    Context: {context}
    
    Question: {question}
    
    Helpful Answer:
    """
    
    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )
 # Create the conversation chain
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt}
    )
    
    return conversation_chain

def handle_userinput(user_question):
    """Process user input and generate response"""
    if st.session_state.conversation is not None:
        response = st.session_state.conversation({"question": user_question})
        st.session_state.chat_history.append({"role": "user", "content": user_question})
        st.session_state.chat_history.append({"role": "assistant", "content": response["answer"]})

def main():
    """Main application function"""
    st.header(APP_NAME)
    
