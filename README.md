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
Text data cleaning: Performed in data-exploration.ipynb, where raw book descriptions are cleaned and tagged for downstream processing.

Semantic vector search: Implemented in vector-search.ipynb, enabling users to find books similar to natural language queries (e.g., "a book about a person seeking revenge").

Zero-shot text classification: Implemented in text-classification.ipynb, allowing classification of books into categories like fiction and non-fiction.

Sentiment analysis and emotion extraction: Found in sentiment-analysis.ipynb, enabling users to sort books by tone—such as suspenseful, joyful, or sad.

Gradio-powered web app: A user interface built in gradio-dashboard.py to allow interactive book recommendations based on user input.

To run this project successfully, the following dependencies are required:

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


