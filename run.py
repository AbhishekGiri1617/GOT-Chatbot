from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from rag_engine import RAGEngine

# Load environment variables (GROQ_API_KEY)
load_dotenv()

app = FastAPI(title="RAG Microservice API")

# Initialize the engine once when the server starts
# It will automatically check for the persistent index
rag_service = RAGEngine(pdf_path="GOT.pdf")

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    """Endpoint to query the RAG system."""
    try:
        answer = rag_service.query(request.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "ready"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
