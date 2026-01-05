import streamlit as st
import joblib
import os

# Cargar modelo y vectorizador
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, './models/svm_model.pkl')
vectorizer_path = os.path.join(BASE_DIR, './models/svm_vectorizer.pkl')

@st.cache_resource
def load_assets():
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer

model, vectorizer = load_assets()

# Interfaz
st.title("Detector de URLs Spam (SVM)")
url_input = st.text_input("Introduce la URL para analizar:")

if st.button("Analizar"):
    if url_input:
        # 1. Transformar la URL usando el vectorizador cargado
        data_vectorized = vectorizer.transform([url_input]).toarray()
        
        # 2. Predecir
        prediction = model.predict(data_vectorized)
        
        if prediction[0] == 1: # Suponiendo 1 = Spam
            st.error("🚨 ¡Cuidado! Esta URL parece ser SPAM.")
        else:
            st.success("✅ Esta URL parece segura.")