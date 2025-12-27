import numpy as np
import joblib
import faiss
import pickle
import spacy
import tensorflow as tf
tf.get_logger().setLevel('ERROR')

from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow_hub as hub

nlp = spacy.load("en_core_web_sm")

intent_model = tf.keras.models.load_model("intent_keras.h5")

tokenizer = joblib.load("tokenizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

max_len = 40

rag_model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

faq_index = faiss.read_index("faq_index.faiss")
answers = pickle.load(open("faq_answers.pkl", "rb"))

def predict_intent(text):
    seq = tokenizer.texts_to_sequences([text])
    pad = pad_sequences(seq, maxlen=max_len, padding="post")
    pred = np.argmax(intent_model.predict(pad), axis=1)[0]
    return label_encoder.inverse_transform([pred])[0]

def get_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def rag_answer(text):
    query_emb = rag_model([text]).numpy()
    distances, indices = faq_index.search(query_emb.astype("float32"), k=1)
    return answers[indices[0][0]]

def chatbot_response(user_input):
    intent = predict_intent(user_input)
    ents = get_entities(user_input)
    ans = rag_answer(user_input)

    response = f"Intent: {intent}\n"
    if ents:
        response += f"Entities: {ents}\n"
    response += f"Answer: {ans}"
    return response
