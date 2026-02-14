import streamlit as st
import requests

# --- Configuration ---
API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="PDF RAG Assistant", page_icon="🤖")

# --- UI Header ---
st.title("📄 Chat with your PDF")
st.markdown("---")

# --- Chat History Setup ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- User Input ---
if prompt := st.chat_input("Ask a question about your document..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call the FastAPI Backend
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(API_URL, json={"question": prompt})
                if response.status_code == 200:
                    answer = response.json().get("answer", "No answer received.")
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error(f"Error: {response.status_code}")
            except Exception as e:
                st.error(f"Could not connect to Backend: {e}")

# --- Sidebar ---
with st.sidebar:
    st.info("Ensure your FastAPI server is running (`python main.py`) before asking questions.")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
