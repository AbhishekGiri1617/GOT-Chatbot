import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

class RAGEngine:
    def __init__(self, pdf_path: str, index_folder: str = "faiss_index"):
        self.pdf_path = pdf_path
        self.index_folder = index_folder
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.chain = self._initialize_chain()

    def _initialize_chain(self):
        # Persistent Loading Logic
        if os.path.exists(self.index_folder):
            print(f"✅ Loading existing index from '{self.index_folder}'...")
            # 'allow_dangerous_deserialization' is required for loading local pickle files
            vectorstore = FAISS.load_local(
                self.index_folder, 
                self.embeddings, 
                allow_dangerous_deserialization=True
            )
        else:
            print("⏳ No index found. Processing PDF (this may take a moment)...")
            loader = PyPDFLoader(self.pdf_path)
            docs = loader.load()
            
            splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
            chunks = splitter.split_documents(docs)
            
            # Create and save locally
            vectorstore = FAISS.from_documents(chunks, self.embeddings)
            vectorstore.save_local(self.index_folder)
            print(f"💾 Index saved to '{self.index_folder}' for future use.")

        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        
        # Build LCEL Chain
        llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.7)
        template = """Answer the question using ONLY the provided context.
        Context: {context}
        Question: {question}
        Answer:"""
        
        prompt = ChatPromptTemplate.from_template(template)

        return (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt 
            | llm 
            | StrOutputParser()
        )

    def query(self, question: str):
        return self.chain.invoke(question)
