import os
from typing import List
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain.vectorstores import AzureSearch
from utils.azure_setup import get_azure_openai_embeddings, get_azure_search_client

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text content from a PDF file"""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def process_documents(directory: str) -> List[Document]:
    """Process all PDF documents in the specified directory"""
    documents = []
    
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory, filename)
            text = extract_text_from_pdf(file_path)
            
            # Create a document object with metadata
            doc = Document(
                page_content=text,
                metadata={"source": filename}
            )
            documents.append(doc)
    
    return documents

def chunk_documents(documents: List[Document], chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Document]:
    """Split documents into chunks for processing"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return text_splitter.split_documents(documents)

def create_vector_store(documents: List[Document]):
    """Create and populate a vector store with document chunks"""
    embeddings = get_azure_openai_embeddings()
    
    # Create Azure Search vector store , Add documents to the vector store
    vector_store = AzureSearch(
        azure_search_endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
        azure_search_key=os.getenv("AZURE_SEARCH_KEY"),
        index_name=os.getenv("AZURE_SEARCH_INDEX_NAME", "company-policies"),
        embedding_function=embeddings.embed_query,
    )
    
    vector_store.add_documents(documents)
    
    return vector_store

def setup_knowledge_base(directory: str = "data/company_policies"):
    """Set up the knowledge base from documents"""
    # Process documents , Chunk documents , Create vector store
    documents = process_documents(directory)
  
    chunks = chunk_documents(documents)
    
    vector_store = create_vector_store(chunks)
    
    return vector_store
