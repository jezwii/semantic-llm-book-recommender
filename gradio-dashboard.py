import numpy as np
import pandas as pd

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader #extract the text from raw source
from langchain_text_splitters import CharacterTextSplitter #splits into chunks
from langchain_openai import OpenAIEmbeddings #convert chunks into doc embeddings
from langchain_chroma import Chroma #opensource vector database

import gradio as gr

books = pd.read_csv('books_with_emotions.csv')
books["large_thumbnail"] = books["thumbnail"] + "&fife=w800"
books["large_thumbnail"] = np.where(
    books["large_thumbnail"].isna(),
    "cover-not-found.jpg",
    books["large_thumbnail"],
)

raw_documents = TextLoader('tagged_description.txt', encoding="utf-8").load()
text_splitter = CharacterTextSplitter(chunk_size=0,chunk_overlap=0,separator="\n")
documents = text_splitter.split_documents(raw_documents)

huggingface_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

db_books = Chroma.from_documents(
    documents,
    embedding=huggingface_embeddings
)

def retrieve_semantic_recommendations(
        query: str,
        category: str = None,
        tone: str = None,
        intial_top_k: int= 50,
        final_top_k: int= 16,
)-> pd.DataFrame:
    recs = db_books.similarity_search(query, k =intial_top_k)
    book_lists = [int(rec.page_content.strip('"').split()[0]) for rec in recs]
    books_rec = books[books["isbn13"].isin(book_lists)].head(final_top_k)

    if category != "All":
        books_rec = books_rec[books_rec["simple_category"] == category].head(final_top_k)
    else:
        books_rec = books_rec.head(final_top_k)

    if tone == "Happy":
        books_rec.sort_values(by="joy", ascending=False, inplace=True)
    elif tone == "Surprising":
        books_rec.sort_values(by="surprise", ascending=False, inplace=True)
    elif tone == "Angry":
        books_rec.sort_values(by="anger", ascending=False, inplace=True)
    elif tone == "Suspenseful":
        books_rec.sort_values(by="fear", ascending=False, inplace=True)
    elif tone == "Sad":
        books_rec.sort_values(by="sadness", ascending=False, inplace=True)

    return books_rec

def recommend_book(
        query: str,
        category: str,
        tone: str,
):
    recommendations = retrieve_semantic_recommendations(query, category, tone)
    results=[]

    for _, row in recommendations.iterrows():
        description = row["description"]
        trunc_desc_split = description.split()
        truncated_desc =" ".join(trunc_desc_split[:30]) + "..." #if truncated desc has more than 30 words

        authors_split = row["authors"].split(";")
        if len(authors_split) == 2:
            authors_str = f" {authors_split[0]} and {authors_split[1]}"
        elif len(authors_split) >2:
            authors_str = f"', '.join({authors_split[:-1]},and {authors_split[-1]})"
        else:
            authors_str = row["authors"]

        caption = f"{row["title"]} by {authors_str}: {truncated_desc}"
        results.append((row["large_thumbnail"],caption))
    return results

categories = ["All"] + sorted(books["simple_category"].unique())
tone = ["All"] + ["Happy","Surprising","Angry","Suspenseful","Sad"]

with gr.Blocks(theme= gr.themes.Glass()) as dashboard:
    gr.Markdown("Semantic Book Recommender")

    with gr.Row():
        user_query = gr.Textbox(label = "Please enter a description of a book:",
                                placeholder = "e.g., A book about a boy with magic")
        category_dropdown = gr.Dropdown(choices = categories,label = "Select a category",value = "All")
        tone_dropdown = gr.Dropdown(choices=tone, label="Select a tone", value="All")
        submit_button = gr.Button("Find Recommendations")

    gr.Markdown("## Recommendations")
    output = gr.Gallery(label="Recommended Books",columns=8,rows=2)

    submit_button.click(fn=recommend_book,
                        inputs=[user_query,category_dropdown,tone_dropdown],
                        outputs=output)

if __name__ == "__main__":
    dashboard.launch()