from langchain.chains import RetrievalQA
from chains.retriever_builder import get_retriever
from langchain_google_genai import ChatGoogleGenerativeAI

# Gemini LLM
llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", temperature=0.3)
retriever = get_retriever()

# Default QA Chain (no memory, no prompt)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=False,
)

async def run_chatbot(user_input):
    return await qa_chain.ainvoke({"query": user_input})
