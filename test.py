import os
import shutil
import streamlit as st

from dotenv import load_dotenv

from Src.documentloader import DocumentLoader
from Src.textsplitter import TextSplitter
from Src.vectorstore import vectorstore
from Src.retriever import Retriever
from Src.ragchain import RagChain


# =========================================================
# LOAD ENVIRONMENT
# =========================================================

load_dotenv()


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Multi File ChatBot",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("🤖 Multi File ChatBot")

st.write(
    "Upload any supported file and ask questions"
)


# =========================================================
# SESSION STATE
# =========================================================

# RAG Chain
if "chain" not in st.session_state:
    st.session_state.chain = None


# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# DISPLAY OLD CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# =========================================================
# FILE UPLOADER
# =========================================================

upload_file = st.file_uploader(
    "Choose file",
    type=[
        "pdf",
        "txt",
        "csv",
        "json",
        "md"
    ]
)


# =========================================================
# FILE PROCESSING
# =========================================================

if upload_file:

    # ---------------------------------------------
    # Create Data folder
    # ---------------------------------------------

    os.makedirs(
        "Data",
        exist_ok=True
    )


    # ---------------------------------------------
    # Save Uploaded File
    # ---------------------------------------------

    file_path = os.path.join(
        "Data",
        upload_file.name
    )


    with open(file_path, "wb") as f:

        f.write(
            upload_file.getbuffer()
        )


    st.success(
        f"✅ {upload_file.name} uploaded successfully"
    )


    # ---------------------------------------------
    # Process File
    # ---------------------------------------------

    with st.spinner(
        "Processing file..."
    ):

        try:

            # =====================================
            # 1. DOCUMENT LOADER
            # =====================================

            loader = DocumentLoader(
                file_path
            )

            document = loader.get_fileload()


            # =====================================
            # 2. TEXT SPLITTER
            # =====================================

            splitter = TextSplitter()

            chunks = splitter.split_document(
                document
            )


            # =====================================
            # 3. REMOVE OLD VECTOR DB
            # =====================================

            if os.path.exists("Vector db"):

                shutil.rmtree(
                    "Vector db"
                )


            # =====================================
            # 4. VECTOR STORE
            # =====================================

            vector_store = vectorstore()

            db = vector_store.create_vector_store(
                chunks
            )


            # =====================================
            # 5. RETRIEVER
            # =====================================

            retriever = Retriever(db)

            search_engine = (
                retriever.get_retriever()
            )


            # =====================================
            # 6. RAG CHAIN
            # =====================================

            rag_chain = RagChain(
                search_engine
            )

            chain = rag_chain.create_chain()


            # =====================================
            # 7. SAVE CHAIN
            # =====================================

            st.session_state.chain = chain


            st.success(
                "🤖 ChatBot Ready!"
            )


        except Exception as e:

            st.error(
                f"❌ Error while processing file: {e}"
            )


# =========================================================
# CHAT
# =========================================================

if st.session_state.chain is not None:

    question = st.chat_input(
        "Ask your question..."
    )


    if question:

        # =====================================
        # SAVE USER MESSAGE
        # =====================================

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )


        # =====================================
        # DISPLAY USER MESSAGE
        # =====================================

        with st.chat_message("user"):

            st.write(question)


        # =====================================
        # ASSISTANT RESPONSE
        # =====================================

        with st.chat_message("assistant"):

            placeholder = st.empty()

            full_response = ""


            # =================================
            # STREAMING RESPONSE
            # =================================

            try:

                for chunk in st.session_state.chain.stream(
                    question
                ):

                    # If chain returns string
                    if isinstance(chunk, str):

                        full_response += chunk


                    # If chain returns AIMessageChunk
                    elif hasattr(chunk, "content"):

                        full_response += (
                            chunk.content
                        )


                    # Update Streamlit UI
                    placeholder.markdown(
                        full_response
                    )


            except Exception as e:

                full_response = (
                    f"❌ Error generating response: {e}"
                )

                placeholder.error(
                    full_response
                )


        # =====================================
        # SAVE ASSISTANT MESSAGE
        # =====================================

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": full_response
            }
        )


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("⚙️ Settings")


    # ---------------------------------------------
    # Clear Chat
    # ---------------------------------------------

    if st.button("🧹 Clear Chat"):

        st.session_state.messages = []

        st.rerun()


    # ---------------------------------------------
    # Project Information
    # ---------------------------------------------

    st.divider()

    st.subheader("🛠️ Technologies")

    st.info(
        """
        📚 LangChain

        🦙 Ollama / Llama 3.2

        🗂️ ChromaDB

        🤗 HuggingFace Embeddings

        🔎 RAG

        🦜 LangGraph / LangChain

        🎈 Streamlit
        """
    )

