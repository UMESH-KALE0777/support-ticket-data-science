🎫 Support Ticket Priority Prediction using NLP & Machine Learning
📌 Project Overview

Customer support teams receive thousands of tickets daily, and manually prioritizing them can lead to delays, SLA breaches, and poor customer satisfaction.

This project builds an end-to-end NLP-based Machine Learning system that automatically predicts the priority of support tickets (Critical, High, Medium, Low) based on the ticket text.
The solution focuses not only on model accuracy but also on business impact, such as handling critical tickets effectively.

🎯 Problem Statement

Manually assigning ticket priorities is:

Time-consuming

Error-prone

Inconsistent across agents

Goal:
Automatically classify incoming support tickets into priority levels using Natural Language Processing (NLP) and Machine Learning.

🧠 Solution Approach

The project follows a real-world Data Science lifecycle:

Data Understanding & EDA

Text Preprocessing

Feature Engineering (TF-IDF)

Model Training (Logistic Regression & SVM)

Model Evaluation (Confusion Matrix, Precision, Recall, F1-score)

Deployment using Streamlit

🛠️ Tech Stack

Programming Language: Python

Libraries:

pandas, numpy

scikit-learn

joblib

matplotlib, seaborn

NLP Technique: TF-IDF Vectorization

Model: Linear Support Vector Machine (SVM)

Deployment: Streamlit

Version Control: Git & GitHub


📂 Project Structure
support-ticket-data-science/
│
├── data/
│   └── support_tickets.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_model_training.ipynb
│
├── models/
│   ├── svm_model.pkl
│   └── tfidf.pkl
│
├── app/
│   └── app.py
│
└── README.md


📊 Model Evaluation

Evaluation was done using:

Confusion Matrix

Precision

Recall

F1-Score

Why not accuracy alone?

In multi-class NLP problems:

Text can be ambiguous

Classes can overlap

Business impact matters more than raw accuracy

📌 Focus was placed on Recall & F1-score, especially for Critical tickets, to reduce SLA violations.


Streamlit App

A Streamlit web application allows users to:

Enter a support ticket text

Instantly get the predicted priority level

This makes the project demo-ready for recruiters and interviews.

To run locally:

streamlit run app/app.py

S📈 Business Impact

Faster ticket triaging

Reduced response time for critical issues

Improved customer satisfaction

Scalable solution for large support teams



