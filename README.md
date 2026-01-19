# RAG_IBM
Building RAG applications

Demo link for simple LLM chatbot: https://drive.google.com/file/d/1OF-h5MzXSEsfLPAT4p0AEGJDgy-TMjd-/view?usp=sharing

Demo link for RAG enabled LLM chatbot: https://drive.google.com/file/d/197eF2m_Yl6d4dKwUsXIThlvPYAoBGN7P/view?usp=sharing

# 📄 RAG-Based PDF Question Answering Chatbot

This project is a **Retrieval-Augmented Generation (RAG) chatbot** that allows users to upload a **PDF document** and ask natural-language questions about its content.  
The chatbot retrieves relevant sections from the document and generates accurate, context-aware answers using a large language model.

The application is built using **LangChain**, **IBM watsonx.ai**, **Chroma vector store**, and **Gradio** for the user interface.

---

## 🚀 Features

- 📂 Upload any PDF document
- 🔍 Automatically splits and embeds document text
- 🧠 Uses Retrieval-Augmented Generation (RAG) for grounded responses
- 💬 Ask free-form natural language questions
- 🖥️ Simple web UI powered by Gradio
- 🔐 Suppresses noisy runtime warnings for a clean user experience

---

## 🧱 Architecture Overview

1. **PDF Loading**
   - PDF is loaded using `PyPDFLoader`

2. **Text Chunking**
   - Text is split into manageable chunks using `RecursiveCharacterTextSplitter`

3. **Embeddings**
   - Document chunks are embedded using **IBM watsonx embeddings**

4. **Vector Store**
   - Embeddings are stored in **Chroma**

5. **Retrieval + Generation**
   - Relevant chunks are retrieved and passed to the LLM via `RetrievalQA`

6. **User Interface**
   - Gradio UI enables file upload and interactive querying

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **IBM watsonx.ai**
  - Watsonx LLM
  - Watsonx Embeddings
- **Chroma** (Vector Database)
- **Gradio** (UI)
- **PDF Processing** (`PyPDFLoader`)
