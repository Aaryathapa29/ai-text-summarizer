
# 📝 AI Text Summarizer

An AI-powered text summarization web application that transforms long paragraphs and articles into concise, meaningful summaries using Natural Language Processing (NLP).

Built with Python, Streamlit, and Hugging Face Transformers.

## ✨ Features

- Generate summaries from long text
- Choose between short, medium, and detailed summaries
- View original and summarized word counts
- Simple and interactive web interface
- AI-powered abstractive text summarization

## 🛠️ Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- DistilBART (CNN/DailyMail)

## 🧠 How It Works

The application uses a pretrained Transformer model to understand the input text and generate a shorter version containing its key information.

The summarization process involves:

1. Accepting text from the user
2. Processing the input using a pretrained NLP model
3. Generating a concise summary
4. Displaying the summarized output

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone 

### 2. Navigate to the project directory

```bash
cd ai-text-summarizer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install streamlit transformers torch
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

http://localhost:8501

## 📂 Project Structure

```text
ai-text-summarizer/
│
├── app.py
├── README.md
└── requirements.txt
```

## 📌 Model

This project uses:

`sshleifer/distilbart-cnn-12-6`

A pretrained DistilBART model fine-tuned for summarization on the CNN/DailyMail dataset.

The model is downloaded automatically when the application runs for the first time.

## 🔮 Future Improvements

- PDF and document summarization
- URL-based article summarization
- Multilingual text summarization
- Adjustable summary compression ratio
- Comparison of extractive and abstractive summarization
- Evaluation using ROUGE scores

## 👩‍💻 Author

Aarya Thapa

Software Engineering Student | AI/ML & NLP Enthusiast


This project is part of my journey into Natural Language Processing and Artificial Intelligence.
