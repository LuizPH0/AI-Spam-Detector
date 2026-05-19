# 🤖 AI Spam Detector Dashboard

Um projeto de Inteligência Artificial capaz de detectar mensagens de spam utilizando Machine Learning e Processamento de Linguagem Natural (NLP).

---

# 📌 Sobre o Projeto

O objetivo deste projeto é identificar automaticamente se uma mensagem é:

- ✅ Normal (Ham)
- 🚨 Spam

O sistema utiliza técnicas de:

- Machine Learning
- NLP (Natural Language Processing)
- Vetorização de texto
- Classificação supervisionada

Tudo isso através de uma interface interativa desenvolvida com Streamlit.

---

## 📈 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy (AVG)| 98% |
| F1-score (AVG) | 98% |

### Validation Method
- 5-Fold Cross Validation

---

# 🧠 Como Funciona?

A Inteligência Artificial aprende padrões presentes em milhares de mensagens reais.

Exemplo:
```txt
🚨 Spam
Congratulations! You won a FREE iPhone!
✅ Não Spam
Hey, are we meeting tomorrow?
```
O modelo transforma o texto em números usando TF-IDF e utiliza Logistic Regression para prever a probabilidade da mensagem ser spam.

## ⚙️ Tecnologias Utilizadas
- Python
- Scikit-learn
- Streamlit
- Pandas
- Matplotlib
- Joblib

## 📊 Dataset

Foi utilizado o dataset:

[SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)


Contendo mais de 5.000 mensagens reais classificadas como:

- spam

- ham (mensagens normais)

## 🧮 Modelo de Machine Learning

O projeto utiliza:

- Logistic Regression

- Modelo de classificação muito utilizado em NLP.

- A função logística utilizada é:

P(y=1)=
1+e
−z
1
	​


Ela calcula a probabilidade de uma mensagem ser spam.

## 🏗️ Estrutura do Projeto
```txt
AI-Spam-Detector/
│
├── app.py
├── spam_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
├── spam.csv
└── treinamento_modelo.ipynb
```
---

## 🚀 Como Executar o Projeto

1️⃣ Clone o repositório
git clone https://github.com/seu-usuario/AI-Spam-Detector-Dashboard.git

2️⃣ Acesse a pasta
cd AI-Spam-Detector-Dashboard

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Execute o dashboard
streamlit run app.py

---

## 📸 Funcionalidades

✅ Detecção automática de spam

✅ Probabilidade da previsão

✅ Dashboard interativo

✅ Interface amigável

✅ Gráfico de probabilidades

✅ Processamento de linguagem natural

---

## 📈 Exemplo de Resultado
|Mensagem |	Resultado |
----------|-------------
|"WINNER!! Claim your FREE prize now!" |	🚨 Spam|
|"Let's meet at 7 PM today." |	✅ Não Spam|

---

## 🧠 Conceitos Aprendidos



Este projeto aborda conceitos importantes de:

- NLP
- Machine Learning
- Classificação de Texto
- Engenharia de Dados
- Vetorização TF-IDF
- Treinamento de Modelos
- Deploy de aplicações de IA

---

## 👨‍💻 Autor

Desenvolvido por Luiz Hatem.

Projeto criado para estudos e desenvolvimento na área de:

- AI Engineer
- Machine Learning Engineer
- Data Science

---

## ⭐ Objetivo

Este projeto foi desenvolvido com foco em aprendizado prático de Inteligência Artificial e construção de portfólio profissional para atuação na área de IA.
