import streamlit as st
import joblib

# Load model & vectorizer
svm_model = joblib.load("models/svm_model.pkl")
tfidf = joblib.load("models/tfidf.pkl")


st.set_page_config(page_title="Support Ticket Classifier", layout="centered")

st.title("🎫 Support Ticket Priority Classifier")
st.write("Automatically predicts ticket priority using NLP & ML")

# User input
ticket_text = st.text_area(
    "Enter support ticket text:",
    height=150,
    placeholder="Describe the issue here..."
)

if st.button("Predict Priority"):
    if ticket_text.strip() == "":
        st.warning("Please enter ticket text")
    else:
        text_tfidf = tfidf.transform([ticket_text])
        prediction = svm_model.predict(text_tfidf)[0]

        st.success(f"🔮 Predicted Priority: **{prediction}**")
