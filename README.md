# 📚 Semantic Book Recommender using LLMs

A smart book recommendation system that understands **natural language queries** using **Hugging Face sentence embeddings**, **LangChain**, and **Chroma vector database** — without relying on OpenAI APIs.

---

## 🚀 Features

- 🔎 **Semantic search**: Ask things like *"Books for kids who love animals"*
- 🤖 **LLM-ready**: Uses `sentence-transformers/all-MiniLM-L6-v2` for deep semantic matching
- 🧱 **Vector DB**: Stores and retrieves documents via `Chroma`
- 🧰 **Modular**: Built with LangChain components for extensibility
- 🖥️ **Gradio UI** (optional): User-friendly interface for live querying

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python | Core language |
| 🔗 LangChain | Text splitting, embedding pipeline |
| 🤗 Hugging Face | Local sentence embeddings |
| 💾 ChromaDB | Local vector store |
| 📊 Pandas | Data preprocessing |
| 🖼️ Gradio | (Optional) Web UI |

---

## 🧪 Example Queries

> “A book for a 10-year-old who loves science and adventure”  
> “Something educational and nature-themed for kids”  
> “Short bedtime story about kindness”

---
-Text data cleaning (code in the notebook data-exploration.ipynb)
-Semantic (vector) search and how to build a vector database (code in the notebook vector-search.ipynb). This allows users to find the most similar books to a natural language query (e.g., "a book about a person seeking revenge").
-Doing text classification using zero-shot classification in LLMs (code in the notebook text-classification.ipynb). This allows us to classify the books as "fiction" or "non-fiction", creating a facet that users can filter the books on.
-Doing sentiment analysis using LLMs and extracting the emotions from text (code in the notebook sentiment-analysis.ipynb). This will allow users to sort books by their tone, such as how suspenseful, joyful or sad the books are.
-Creating a web application using Gradio for users to get book recommendations (code in the file gradio-dashboard.py).

the following dependencies are required:

-kagglehub
-pandas
-matplotlib
-seaborn
-python-dotenv
-langchain-community
-langchain-opencv
-langchain-chroma
-transformers
-gradio
-notebook
-ipywidgets


