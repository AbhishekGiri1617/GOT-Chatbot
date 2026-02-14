🤖 PDF RAG Microservice (LangChain + FastAPI):

A high-performance, persistent Retrieval-Augmented Generation (RAG) microservice built with LangChain 0.3, FastAPI, and FAISS. This service allows you to chat with your PDF documents via a clean REST API.

✨ Features
Persistent Vector Store: Chunks and embeddings are saved locally using FAISS. No need to re-process your PDF every time the server starts!
Modern LangChain: Built using LCEL (LangChain Expression Language) for efficient streaming and chain management.
FastAPI Powered: Includes high-performance endpoints with automatic Swagger UI documentation.
Asynchronous Support: Handles multiple queries concurrently.
HuggingFace Embeddings: Uses all-MiniLM-L6-v2 for lightweight, high-quality semantic search.
🛠️ Tech Stack
FastAPI,
LangChain,
openai/gpt-oss-120b (from Groq),
FAISS,
HuggingFace

🚀 Getting Started
1. Prerequisites
Python 3.9+
A Groq API and HuggingFace API Key 
2. Installation
bash
# Clone the repo

bash
git clone githttps://github.com/AbhishekGiri1617/GOT-Chatbot.git

bash

cd GOT-Chatbot

# Install dependencies
pip install -r requirements.txt

3. Setup Environment
Create a .env file in the root directory:
env
GROQ_API_KEY=your_groq_api_key_here

4. Run the Service
bash
python main.py
Use code with caution.

The server will start at http://127.0.0.1:8000. On the first run, it will automatically process GOT.pdf and create a faiss_index folder.
📖 API Usage
Interactive Docs
Access the built-in Swagger UI at: http://127.0.0.1/docs
Ask a Question (cURL)
bash
     '{"question": "What are the main points in the document?"}'


Response Format
json
{
  "answer": "The main points discussed in the document are..."
}
Use code with caution.

📂 Project Structure
text
├── rag_engine.py        # LangChain logic & RAG pipeline
├── GOT.pdf           # Your source document
├── .env                 # Environment variables (Private)
└── requirements.txt     # Project dependencies
Use code with caution.

🔧 Future Enhancements
Implement a Streamlit frontend for a better user experience.
Add support for Docker containerization.
