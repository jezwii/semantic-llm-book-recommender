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
Text data cleaning
(code in the notebook data-exploration.ipynb)

Semantic (vector) search & vector database
(code in vector-search.ipynb)
→ Enables users to search with queries like:
"a book about a person seeking revenge"

Zero-shot text classification using LLMs
(code in text-classification.ipynb)
→ Classifies books as "fiction" or "non-fiction" to enable faceted filtering

Sentiment analysis & emotion extraction
(code in sentiment-analysis.ipynb)
→ Lets users sort books by tone: suspenseful, joyful, sad, etc.

Gradio web app for recommendations
(code in gradio-dashboard.py)
the following dependencies are required:

kagglehub
pandas
matplotlib
seaborn
python-dotenv
langchain-community
langchain-opencv
langchain-chroma
transformers
gradio
notebook
ipywidgets


