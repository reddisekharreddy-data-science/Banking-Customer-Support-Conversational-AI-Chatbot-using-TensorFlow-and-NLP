# Banking Customer Support Conversational AI Chatbot (TensorFlow + NLP)

This project is an AI-powered **Banking Customer Support Chatbot** that understands customer queries, detects intent, extracts important entities, and retrieves the most relevant answers using deep learning and NLP. It supports common banking topics such as accounts, cards, loans, balances, KYC, and more.

The chatbot uses:

- Bidirectional LSTM for intent classification
- Named Entity Recognition using spaCy
- Retrieval-Augmented Generation (RAG) for answer retrieval
- Universal Sentence Encoder for embeddings
- FAISS for semantic similarity search
- Streamlit web interface for interaction
- TensorFlow backend for model inference

---

## 🎯 Key Features

- Understands real-world natural language banking queries
- Detects user **intent**
- Extracts **entities** like names, amounts, dates, organizations
- Answer retrieval using **semantic similarity**
- Deep learning–based **Bidirectional LSTM** model
- Clean and easy-to-use web chat interface
- Lightweight, modular, deployment-ready architecture

---

## 🧠 High-Level System Architecture

1. User enters a banking question in the Streamlit chat interface
2. Input text is passed to the chatbot backend pipeline
3. The system performs the following sequential steps:
   - Text preprocessing and tokenization
   - Intent classification using **Bidirectional LSTM**
   - Entity extraction using NER
   - Semantic answer retrieval using RAG
4. Final response is returned and displayed to the user

This project contains:

- A Streamlit frontend application
- A TensorFlow-based chatbot pipeline backend

---

## 🏗 Project Structure (Conceptual)

- Streamlit app for chat interface
- NLP + TensorFlow chatbot pipeline
- Trained model and helper files:
  - intent classification model file
  - tokenizer file
  - label encoder file
  - FAISS similarity index file
  - FAQ answers file

---

## 🤖 Core Components Overview

### 1. Intent Classification (Bidirectional LSTM)

The chatbot predicts **what the user wants**, such as:

- balance inquiry
- ATM issue
- credit card problem
- account opening/closing
- loan information
- internet banking help

The intent classifier is built using:

- text tokenization
- sequence padding
- **Bidirectional LSTM network**

#### Why Bidirectional LSTM?

- Reads the sentence **both forward and backward**
- Captures complete context around each word
- Handles complex banking sentences
- Performs better than traditional LSTM or simple RNN

It improves understanding of:

- long sentences
- ambiguous wording
- multi-intent queries

---

### 2. Entity Extraction (NER)

The chatbot identifies important information from user text, such as:

- names
- account numbers
- organizations
- amounts
- dates
- locations

This enables responses like:

- identifying which account user refers to
- finding relevant transaction mentions
- interpreting dates and timelines

---

### 3. Retrieval-Augmented Generation (RAG)

Answer generation combines:

- semantic similarity search
- FAQ knowledge base

Steps in the RAG pipeline:

1. Convert user query into an embedding using Universal Sentence Encoder
2. Search similar questions using FAISS vector index
3. Retrieve the most similar stored answer
4. Return answer as chatbot response

Benefits:

- more accurate responses
- scalable when new FAQs are added
- works better than rule-based chatbots
- reduces hallucinations

---

### 4. Streamlit User Interface

The project includes a **Streamlit web app** to chat with the bot.

Roles of the UI:

- display title and description
- take user text input
- trigger chatbot response pipeline
- display final chatbot reply

The UI communicates directly with the backend chatbot pipeline for inference.

---

## ✅ Requirements

Recommended dependencies:

- Python 3.x
- TensorFlow
- TensorFlow Hub
- spaCy
- spaCy English model (en_core_web_sm)
- NumPy
- joblib
- FAISS
- Streamlit

Required model and support files:

- intent model file (intent_keras.h5)
- tokenizer file
- label encoder file
- FAQ FAISS index file
- FAQ answers file

---

## 🚀 How to Run (Step-by-Step – No Code)

1. Install Python
2. Create and activate a virtual environment (recommended)
3. Install all required libraries
4. Place trained model files in the project folder
5. Download spaCy English model
6. Ensure FAISS index and FAQ answer file exist
7. Launch Streamlit app
8. Open browser and start chatting

---

## 📊 Training Process Overview (Conceptual Only)

Model training involved:

- collecting banking FAQ data
- preprocessing and cleaning text
- tokenization and padding
- assigning intent labels
- training **Bidirectional LSTM** model
- evaluating model accuracy and loss
- generating FAQ embeddings
- building FAISS similarity index

---

## 🔮 Possible Future Enhancements

- Support multi-turn long conversations
- Add voice-based interaction
- Multi-language support
- Deploy to AWS/GCP/Azure
- Integration with real bank databases/APIs
- Add sentiment analysis

---

## 📝 Conclusion

This project demonstrates a functional **banking conversational AI chatbot** using:

- Bidirectional LSTM intent classifier
- NLP entity extraction
- Retrieval-Augmented Generation
- TensorFlow deep learning
- Streamlit interactive UI

It can be used as:

- portfolio project
- academic research project
- enterprise prototype
- real-world banking assistant foundation
