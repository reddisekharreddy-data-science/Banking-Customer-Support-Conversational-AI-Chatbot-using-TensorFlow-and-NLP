# Banking-Customer-Support-Conversational-AI-Chatbot-using-TensorFlow-and-NLP
This project is an AI-powered banking customer support chatbot that understands customer queries, detects intent, extracts key information, and retrieves relevant answers using NLP and deep learning. It supports common banking topics such as accounts, cards, loans, balances, KYC, and more.

The chatbot uses:

Bidirectional LSTM for intent classification

Named Entity Recognition (NER) using spaCy

Retrieval-Augmented Generation (RAG) with:

Universal Sentence Encoder

FAISS similarity search

Streamlit UI for interactive web chat

TensorFlow-based inference pipeline

The project consists of a backend NLP pipeline and a frontend app interface.
The Streamlit UI front-end communicates with the TensorFlow pipeline to produce final responses.

🎯 Key Features

Understands natural language banking queries

Detects intent of the user message

Extracts entities such as names, dates, amounts, etc.

Uses Bidirectional LSTM for intent classification

Retrieves answers using semantic similarity search

Provides real-time chat interface using Streamlit

Lightweight and ready for deployment

🧠 System Architecture (High-Level)

User enters a banking question in the web app

Query is sent to the chatbot pipeline

Pipeline performs:

Text preprocessing and tokenization

Intent prediction using Bi-LSTM model

Entity extraction

Answer retrieval using RAG pipeline

Final response is sent back to the Streamlit UI

The following components are implemented in the uploaded files:

Streamlit UI application 

app_streamlit

TensorFlow chatbot pipeline 

chatbot_pipeline_tf

🏗 Project Structure

A Streamlit application file for UI

A TensorFlow-based processing pipeline file

Pre-trained model and supporting artifacts (external files loaded at runtime):

intent_keras.h5

tokenizer.pkl

label_encoder.pkl

faq_index.faiss

faq_answers.pkl

🤖 Core Components Explained
1. Intent Detection (Bidirectional LSTM)

The chatbot predicts what the user wants (example intents: account opening, credit card status, loan info).

This is performed using:

Word tokenization

Padding to fixed sequence length

Deep neural network built with:

Bidirectional LSTM layers

Why Bidirectional LSTM?

Reads text forward and backward

Captures context before and after a word

Improves understanding of banking queries

Handles long sentences effectively

Output of this module is an intent label such as:

balance inquiry

ATM issue

loan information

account closing

KYC update

2. Entity Recognition (NER)

The system extracts key information such as:

customer names

dates

amounts

account numbers

organizations

It uses spaCy’s pretrained NER model to identify entities inside the query text.

3. Retrieval-Augmented Generation (RAG)

The answer is generated using semantic search instead of just rule-based lookup.

Steps include:

Convert query to embedding using Universal Sentence Encoder

Perform similarity search using FAISS index

Retrieve most relevant FAQ answer

Provide it as the chatbot response

This ensures:

contextual understanding

accurate response mapping

scalability when adding new FAQs

4. Streamlit Chat Application

The frontend interface allows users to ask banking questions.

Key roles:

display application title

collect user input

show chatbot responses

connect UI with backend pipeline

The UI calls the chatbot pipeline function from the backend file to produce answers.

✅ Requirements

You can list these in your requirements.txt.

Python 3.x

TensorFlow

TensorFlow Hub

spaCy

spaCy English model (en_core_web_sm)

NumPy

joblib

FAISS

pickle (standard library)

Streamlit

Model/artifact files required at runtime:

intent_keras.h5

tokenizer.pkl

label_encoder.pkl

faq_index.faiss

faq_answers.pkl

🚀 How to Use (Step-by-Step — No Code)

Install Python

Create a virtual environment (recommended)

Install required libraries listed above

Download or place all model files in project directory

Ensure FAISS index and answer file exist

Download spaCy English model

Run the Streamlit application

Open browser and chat with the bot

📊 Dataset & Training (Conceptual Overview)

The following high-level stages were used when preparing the model:

Collect banking FAQs and queries

Clean and normalize text

Tokenize text and create vocabulary

Encode labels for intents

Train Bidirectional LSTM classifier

Validate and evaluate model performance

Build FAQ embeddings using Universal Sentence Encoder

Index embeddings using FAISS for fast retrieval

🛠 Future Enhancements

Multi-turn conversation support

Voice input integration

Multilingual capability

Deployment on AWS / GCP / Azure

Integration with real bank APIs

📝 Conclusion

This project demonstrates a production-ready banking conversational AI chatbot combining:

Deep learning (Bi-LSTM)

NLP entity recognition

Semantic answer retrieval

Simple web deployment

It can be used as:

portfolio project

research work

real-world prototype

deployment-ready chatbot base
