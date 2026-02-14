🤖 PDF RAG Microservice (LangChain + FastAPI)
A high-performance, persistent Retrieval-Augmented Generation (RAG) microservice built with LangChain 0.3, FastAPI, and FAISS. This service allows you to chat with your PDF documents via a clean REST API.
✨ Features
Persistent Vector Store: Chunks and embeddings are saved locally using FAISS. No need to re-process your PDF every time the server starts!
Modern LangChain: Built using LCEL (LangChain Expression Language) for efficient streaming and chain management.
FastAPI Powered: Includes high-performance endpoints with automatic Swagger UI documentation.
Asynchronous Support: Handles multiple queries concurrently.
HuggingFace Embeddings: Uses all-MiniLM-L6-v2 for lightweight, high-quality semantic search.
🛠️ Tech Stack
Framework: FastAPI
Orchestration: LangChain
LLM: Groq (Llama 3.1 70B)
Vector DB: FAISS
Embeddings: HuggingFace
🚀 Getting Started
1. Prerequisites
Python 3.9+
A Groq API Key (Get one at console.groq.com)
2. Installation
bash
# Clone the repo
git clone 
Use code with caution.

bash
https://github.com
Use code with caution.

bash

cd YOUR_REPO_NAME

# Install dependencies
pip install -r requirements.txt
Use code with caution.

3. Setup Environment
Create a .env file in the root directory:
env
GROQ_API_KEY=your_groq_api_key_here
Use code with caution.

4. Run the Service
bash
python main.py
Use code with caution.

The server will start at http://127.0.0.1:8000. On the first run, it will automatically process sample.pdf and create a faiss_index folder.
📖 API Usage
Interactive Docs
Access the built-in Swagger UI at: http://127.0.0.1
Ask a Question (cURL)
bash
curl -X POST "http://127.0.0.1" \
     -H "Content-Type: application/json" \
     -d '{"question": "What are the main points in the document?"}'
Use code with caution.

Response Format
json
{
  "answer": "The main points discussed in the document are..."
}
Use code with caution.

📂 Project Structure
text
├── faiss_index/         # Persisted vector database (Generated)
├── main.py              # FastAPI application & API routes
├── rag_engine.py        # LangChain logic & RAG pipeline
├── sample.pdf           # Your source document
├── .env                 # Environment variables (Private)
└── requirements.txt     # Project dependencies
Use code with caution.

🔧 Future Enhancements
Add /upload endpoint to support multiple PDFs dynamically.
Implement a Streamlit frontend for a better user experience.
Add support for Docker containerization.
