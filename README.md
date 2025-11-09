<img width="655" height="328" alt="Screenshot 2025-11-09 at 5 39 42 PM" src="https://github.com/user-attachments/assets/f61d6848-1f01-4186-b3c6-c3d1606b660c" />
# CompanyPolicy_Chatbot11
# Company Policy & Support Chatbot

An AI-powered chatbot built with LangChain, Azure OpenAI, and Azure AI Studio to provide employees with instant access to company policies and support.

## Features

- RAG (Retrieval-Augmented Generation) system for accurate policy information
- Conversational memory for context-aware interactions
- Document processing from PDF files
- Streamlit-based user interface
- Integration with Azure OpenAI and Azure AI Search

## Setup

Clone this repository
Install dependencies: `pip install -r requirements.txt`
Set up your Azure OpenAI and Azure AI Search services
Create a `.env` file with your Azure credentials
Add company policy PDFs to the `data/company_policies` directory
Run the application: `streamlit run app.py`

## Usage

Click "Process Documents" in the sidebar to ingest company policies
 Ask questions about company policies in the chat interface
 Reset the conversation at any time using the "Reset Conversation" button

## Azure Setup

### Azure OpenAI

 Create an Azure OpenAI resource in the Azure portal
 Deploy a model (e.g., GPT-4)
 Note down the API key, endpoint, and deployment name

### Azure AI Search

Create an Azure AI Search service
Create an index for storing document embeddings
Note down the endpoint and key


###How to Run the Project

Install the required dependencies:
pip install -r requirements.txt

Set up your Azure services and configure the .env file with your credentials.

Add your company policy documents (PDFs) to the data/company_policies directory.

Run the application:
streamlit run app.py


Open your browser and navigate to the provided URL (usually http://localhost:8501).

Click "Process Documents" in the sidebar to ingest your company policies.

Start asking questions about company policies in the chat interface!


Customization Options
Document Types: Modify the document_processor.py to handle other document formats like Word, HTML, etc.
Chat Interface: Customize the Streamlit UI in app.py to match your company's branding.
Response Style: Adjust the prompt template in app.py to change the bot's tone and response style.
Integration: Integrate with other communication platforms like Microsoft Teams or Slack by replacing the Streamlit interface.
This project provides a solid foundation for a company policy and support chatbot that can be further customized to meet specific organizational needs.
