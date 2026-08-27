import os

import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="NoteBot", page_icon="🤖")
st.header("🤖 NoteBot")

if not OPENAI_API_KEY:
    st.error("OPENAI_API_KEY is missing from the .env file.")
    st.stop()

with st.sidebar:
    st.title("My Notes")
    file = st.file_uploader(
        "Upload notes PDF and start asking questions",
        type=["pdf"],
    )

if file is not None:
    pdf = PdfReader(file)

    text = "\n".join(
        page.extract_text() or ""
        for page in pdf.pages
    )

    if not text.strip():
        st.error("No readable text was found in this PDF.")
        st.stop()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        length_function=len,
    )
    chunks = splitter.split_text(text)

    embeddings = OpenAIEmbeddings(
        api_key=OPENAI_API_KEY,
    )
    vector_store = FAISS.from_texts(chunks, embeddings)

    user_query = st.text_input("Type your query here")

    if user_query:
        matching_chunks = vector_store.similarity_search(
            user_query,
            k=4,
        )

        llm = ChatOpenAI(
            api_key=OPENAI_API_KEY,
            model="gpt-4o-mini",
            max_tokens=300,
            temperature=0,
        )

        prompt = ChatPromptTemplate.from_template(
            """You are an assistant tutor.
Answer using only the context below.
If the answer is not in the context, say "I don't know."

Context:
{context}

Question:
{input}"""
        )

        chain = create_stuff_documents_chain(llm, prompt)

        output = chain.invoke(
            {
                "input": user_query,
                "context": matching_chunks,
            }
        )

        st.write(output)
    st.info("Upload a PDF to start chatting.")