import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="AI Spam Detector",
    page_icon="🤖",
    layout="wide"
)

# CARREGAR MODELOS
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# SIDEBAR
st.sidebar.title("🤖 AI Spam Detector")
st.sidebar.markdown("Projeto de Machine Learning para detecção de spam.")

st.sidebar.info("""
Tecnologias:
- Python
- Scikit-learn
- NLP
- Streamlit
""")

# TÍTULO
st.title("📧 AI Spam Detector Dashboard")

st.markdown("""
Detecte automaticamente mensagens de spam usando Inteligência Artificial.
""")

# ENTRADA
message = st.text_area(
    "Digite uma mensagem:",
    height=150
)

# BOTÃO
if st.button("🔍 Analisar Mensagem"):

    if message.strip() != "":

        data = vectorizer.transform([message])

        prediction = model.predict(data)[0]

        probabilities = model.predict_proba(data)[0]

        classes = model.classes_

        spam_index = list(classes).index('spam')

        spam_prob = probabilities[spam_index] * 100

        st.subheader("Resultado")

        if prediction == 'spam':
            st.error(f"🚨 SPAM DETECTADO ({spam_prob:.2f}%)")
        else:
            st.success(f"✅ NÃO É SPAM ({100 - spam_prob:.2f}%)")

        # GRÁFICO
        st.subheader("Probabilidades")

        labels = ['Spam', 'Não Spam']
        values = [spam_prob, 100 - spam_prob]

        fig, ax = plt.subplots()

        ax.bar(labels, values)

        ax.set_ylabel('Probabilidade (%)')

        st.pyplot(fig)

    else:
        st.warning("Digite uma mensagem.")