from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from chains.embedding_loader import get_documents
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_retriever():
    documents = get_documents()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=750, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectordb = Chroma.from_documents(docs, embedding=embeddings)
    return vectordb.as_retriever()
