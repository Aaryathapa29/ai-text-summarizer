import streamlit as st
from transformers import pipeline

# Page settings
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="centered"
)

# Title
st.title("📝 AI Text Summarizer")
st.write("Turn long paragraphs into short, meaningful summaries.")

# Load AI model
@st.cache_resource
def load_model():
    summarizer = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )
    return summarizer

# User input
text = st.text_area(
    "Enter your text here:",
    height=250,
    placeholder="Paste a long article or paragraph..."
)

# Summary length
summary_length = st.selectbox(
    "Choose summary length:",
    ["Short", "Medium", "Detailed"]
)

# Button
if st.button("✨ Summarize"):

    if text.strip() == "":
        st.warning("Please enter some text first.")

    elif len(text.split()) < 30:
        st.warning("Please enter at least 30 words.")

    else:
        with st.spinner("AI is summarizing your text..."):

            summarizer = load_model()

            word_count = len(text.split())

            if summary_length == "Short":
                max_length = 50
                min_length = 15

            elif summary_length == "Medium":
                max_length = 100
                min_length = 30

            else:
                max_length = 150
                min_length = 50

            result = summarizer(
                text,
                max_length=max_length,
                min_length=min_length,
                do_sample=False,
                truncation=True
            )

            summary = result[0]["summary_text"]

        # Display result
        st.subheader("Your Summary")
        st.success(summary)

        # Word counts
        st.write("Original words:", word_count)
        st.write("Summary words:", len(summary.split()))

        # Copy-friendly output
        st.text_area(
            "Copy your summary:",
            value=summary,
            height=150
        )