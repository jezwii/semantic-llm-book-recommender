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
- **Text data cleaning**  
  Code in: `data-exploration.ipynb`

- **Semantic (vector) search**  
  Code in: `vector-search.ipynb`  
  Allows users to find the most similar books to a natural language query (e.g., *"a book about a person seeking revenge"*).

- **Zero-shot text classification using LLMs**  
  Code in: `text-classification.ipynb`  
  Automatically classifies books as *fiction* or *non-fiction*, enabling filtering.

- **Sentiment analysis and emotion extraction**  
  Code in: `sentiment-analysis.ipynb`  
  Sort books by tone such as *suspenseful*, *joyful*, or *sad*.

- **Gradio-based web application**  
  Code in: `gradio-dashboard.py`  
  Provides a simple UI to get real-time book recommendations.

---

## 📦 Required Dependencies

These libraries are used throughout the project:

- `kagglehub`
- `pandas`
- `matplotlib`
- `seaborn`
- `python-dotenv`
- `langchain-community`
- `langchain-opencv`
- `langchain-chroma`
- `transformers`
- `gradio`
- `notebook`
- `ipywidgets`


