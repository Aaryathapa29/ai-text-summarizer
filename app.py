
import re

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import pipeline


# --------------------------------
# 1. Page configuration
# --------------------------------

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="centered"
)

st.title("AI Text Summarizer")
st.write(
    "Turn long articles into short, meaningful summaries."
)


# --------------------------------
# 2. Load the Transformer model
# --------------------------------

@st.cache_resource
def load_model():

    summarizer = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )

    return summarizer


# --------------------------------
# 3. TF-IDF Extractive Summarizer
# --------------------------------

def tfidf_summarize(text, number_of_sentences):

    # Split text into sentences
    sentences = re.split(
        r'(?<=[.!?])\s+',
        text.strip()
    )

    # Remove empty sentences
    sentences = [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]

    # Need at least two sentences
    if len(sentences) < 2:
        return text

    # Convert sentences into TF-IDF vectors
    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(
        sentences
    )

    # Calculate the average TF-IDF score
    # of the words in each sentence
    sentence_scores = (
        tfidf_matrix.sum(axis=1).A1
        / (tfidf_matrix.getnnz(axis=1) + 1e-10)
    )

    # Get indexes of the highest-scoring sentences
    ranked_indexes = sentence_scores.argsort()[::-1]

    # Select the most important sentences
    selected_indexes = ranked_indexes[
        :min(number_of_sentences, len(sentences))
    ]

    # Restore original sentence order
    selected_indexes = sorted(selected_indexes)

    # Combine selected sentences
    summary = " ".join(
        sentences[index]
        for index in selected_indexes
    )

    return summary


# --------------------------------
# 4. User input
# --------------------------------

text = st.text_area(
    "Enter your text:",
    height=250,
    placeholder="Paste a long article here..."
)


# --------------------------------
# 5. Summarization options
# --------------------------------

method = st.selectbox(
    "Choose summarization method:",
    [
        "TF-IDF Extractive",
        "Transformer AI (DistilBART)"
    ]
)

summary_length = st.selectbox(
    "Choose summary length:",
    ["Short", "Medium", "Detailed"]
)


# --------------------------------
# 6. Summarize button
# --------------------------------

if st.button("Summarize"):

    if not text.strip():

        st.warning("Please enter some text.")

    else:

        if summary_length == "Short":
            number_of_sentences = 2
            max_length = 50
            min_length = 15

        elif summary_length == "Medium":
            number_of_sentences = 4
            max_length = 100
            min_length = 30

        else:
            number_of_sentences = 6
            max_length = 150
            min_length = 50

        with st.spinner("Generating summary..."):

            # TF-IDF method
            if method == "TF-IDF Extractive":

                summary = tfidf_summarize(
                    text,
                    number_of_sentences
                )

            # Transformer method
            else:

                summarizer = load_model()

                result = summarizer(
                    text,
                    max_length=max_length,
                    min_length=min_length,
                    do_sample=False,
                    truncation=True
                )

                summary = result[0]["summary_text"]

        # --------------------------------
        # 7. Display result
        # --------------------------------

        st.subheader("Your Summary")

        st.write(summary)

        st.write(
            "Original words:",
            len(text.split())
        )

        st.write(
            "Summary words:",
            len(summary.split())
        )

        st.text_area(
            "Copy your summary:",
            value=summary,
            height=150
        )
