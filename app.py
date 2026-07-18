import streamlit as st
import shutil, os
from Src.exception import CustomException
from Src.logger import logging
from Src.documentloader import DocumentLoader
from Src.textsplitter import TextSplitter
from Src.embedding import EmbeddingModel
from Src.vectorstore import vectorstore
from Src.retriever import Retriever
from Src.prompt import PromptTemplate
from Src.model import LLM
from Src.ragchain import RagChain
from Src.memory import Memory


st.set_page_config(
    page_title="Multi File ChatBot",
    page_icon= "🤖",
    layout="wide"
)

st.title("🤖 Multi File ChatBot")

st.write("Upload any supported file and ask question")

upload_file = st.file_uploader(
    "choose file",
    type=[
        "pdf",
        "txt",
        "csv",
        "json",
        "md"
    ]
)


if upload_file:
    os.makedirs("Data" ,exist_ok=True)
    
    
    file_path =os.path.join(
        "Data",
        upload_file.name
    )
    
    with open(file_path, "wb")as f:
        f.write(upload_file.getbuffer())
        
    st.success("file upload successfully")
    
    
## processing

    with st.spinner("Processing Pdf..."):
        
        loader = DocumentLoader(file_path)
        docoument = loader.get_fileload()
        
        
        
        splitter = TextSplitter()
        chunks = splitter.split_document(docoument)
        
        
        if os.path.exists("Vector db"):
            shutil.rmtree("Vector db")
            
        vector_store = vectorstore()
        db = vector_store.create_vector_store(chunks)
        
        retriever = Retriever(db)
        
        search_engine = retriever.get_retriever()
        rag_chain = RagChain(search_engine)
        chain = rag_chain.create_chain()
        st.session_state.chain = chain
        
        st.error("❌ File Not Supported")
        st.warning("⚠ Upload a file first")
    
    st.success("ChatBot Ready..")

# if upload_file and "chain" not in st.session_state:

#     ...

#     st.session_state.chain = chain

#     st.success("ChatBot Ready")


if "chain" in st.session_state:

    question = st.chat_input("Ask your Question")

    if question:

        with st.chat_message("user"):
            st.write(question)

        with st.spinner("Thinking..."):
            answer = st.session_state.chain.invoke(question)

        with st.chat_message("assistant"):
            st.write(answer)
            
            
            
with st.sidebar:

    st.header("⚙ Settings")

    model = st.selectbox(
        "Model",
        ["llama3.2", "mistral", "phi3"]
    )

    chunk_size = st.slider(
        "Chunk Size",
        200,
        2000,
        700
    )

    overlap = st.slider(
        "Chunk Overlap",
        0,
        500,
        100
    )

    top_k = st.slider(
        "Top K",
        1,
        10,
        3
    )

    if st.button("🧹 Clear Chat"):

        st.session_state.messages=[]

        st.rerun()
        
        
        
        
st.info(
"""
📚 LangChain

🦙 Ollama

🗂 ChromaDB

🤗 HuggingFace Embeddings
"""
)