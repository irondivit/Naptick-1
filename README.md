# 🧠 Naptick AI Challenge – Task 1  
**Multimodal RAG Chatbot for Personal Sleep Insights**

This project implements a modular, context-aware Retrieval-Augmented Generation (RAG) chatbot using LangChain and Gemini 1.5 Flash. The system processes structured and semi-structured data across 5 different domains to answer personalized user queries related to sleep, habits, and behavior. It is accessible through an interactive Chainlit interface.

---

## 🎯 Task Description

**Objective:**  
Build an AI chatbot capable of retrieving and reasoning across multiple structured and semi-structured data collections using a RAG pipeline.

### ✅ Required Capabilities:
- Multi-source document ingestion (5 JSONL + CSV)
- Memory layer for follow-up queries
- Chunking, embedding, and retrieval
- Chainlit-based user interface
- LLM-based response generation

---

## 🧩 Data Collections

Processed through a unified loader:

- `wearable_data.csv` — Sleep stats, steps, heart rate
- `chat_history.jsonl` — Past user–bot interactions
- `user_profile.jsonl` — Age, name, goals, chronotype
- `location_data.jsonl` — Time-stamped place visits
- `custom_notes.jsonl` — Sleep journal entries and habits

---

## 🔧 Features Implemented

### 📄 Multi-Collection RAG
- Loads and parses 5 data sources
- Applies consistent chunking and embedding
- Indexes all documents into a shared Chroma vector store

### 🔍 Retrieval Pipeline
- **Chunking:** `RecursiveCharacterTextSplitter` (configurable)
- **Embedding:** Gemini Embeddings via LangChain
- **Storage:** Vector store backed by ChromaDB
- **Retrieval:** Single retriever across all indexed chunks

### 🤖 Gemini-Powered Generation
- Uses `gemini-1.5-flash` via LangChain's `ChatGoogleGenerativeAI`
- Configured with temperature 0.3 for factual answers

### 🧠 Context Memory
- Built-in LangChain memory (`ConversationBufferMemory`) for follow-up understanding

### 💬 UI: Chainlit App
- Clean, responsive web UI at `localhost:8000`
- Chainlit hot reload support with `--watch`

---

## ⚙️ Technology Stack

| Component           | Tool                         |
|---------------------|------------------------------|
| LLM                 | Google Gemini 1.5 Flash      |
| Framework           | LangChain                    |
| Vector Store        | ChromaDB                     |
| Embedding Model     | Google Generative Embeddings |
| UI                  | Chainlit                     |
| Data Format         | JSONL, CSV                   |

---

## 🛠 Setup Instructions

1. **Clone the repo:**
```bash
git clone https://github.com/DivitM/Naptick1.git
cd Naptick1

2. **Create and activate a virtual environment (optional but recommended):**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows

3. **Install dependencies:**
```bash
pip install -r requirements.txt

4. **Add your Gemini API key in .env:**
```bash
GOOGLE_API_KEY=your_gemini_key_here

5. **Run the app:**
```bash
chainlit run app.py --watch
