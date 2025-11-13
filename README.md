📩 Spam Detection ML App (NLP + Streamlit)

This is my simple Machine Learning project where I built a Spam Detection App using Python, NLP, and Streamlit.
The model takes an SMS/email message as input and predicts whether it is Spam or Not Spam.

I learned a lot while doing this project like text preprocessing, TF-IDF vectorization, training ML models, saving models, and deploying a web application.

🌐 Live App Link

You can check the working app here:

👉 https://spam-detection-app-beyhgafu59p6iuwe6zctbd.streamlit.app/

📘 What This Project Does

Takes a message as input

Converts it into numerical format using TF-IDF

Predicts whether the message is Spam (1) or Ham/Not Spam (0)

Shows the result on a clean Streamlit UI

The whole app is deployed online

🧠 Machine Learning Models I Tried

I trained many models and compared their accuracy:

Model	Accuracy
Logistic Regression	94%
Naive Bayes	96.8%
Decision Tree	96.8%
Random Forest	97.6%
SVM (Final Model)	97.5%

I selected SVM because it gave the best balance of precision, recall, and F1-score, especially for detecting spam.

🛠️ Technologies I Used
Machine Learning & NLP

Python

TF-IDF Vectorizer

SVM Classifier

Scikit-Learn

App & Deployment

Streamlit

Streamlit Cloud

Joblib (for saving models)

Tools

Google Colab

VS Code

GitHub

📁 Project Files
spam-detection-app/
│
├── app.py                  # Streamlit UI code
├── best_svm_model.pkl      # Saved SVM model
├── tfidf_vectorizer.pkl    # Saved TF-IDF transformer
├── requirements.txt        # Libraries needed to run the app
└── README.md               # Documentation

▶️ How to Run This Project Locally
1. Clone the repository:
git clone https://github.com/klu2300080179/spam-detection-app.git
cd spam-detection-app

2. Install libraries:
pip install -r requirements.txt

3. Run the app:
streamlit run app.py


The app will open on:

http://localhost:8501

📊 Model Performance (SVM)

For the SVM model:

Precision (Spam): 0.97

Recall (Spam): 0.84

F1-score (Spam): 0.90

Overall Accuracy: 97.48%

🎯 What I Learned from This Project

How to clean and preprocess text data

How TF-IDF works

How to train multiple ML models and compare them

How to save and load ML models using pickle/joblib

How to build a web app using Streamlit

How to deploy an app publicly

This was my first full end-to-end ML + Deployment project, and it helped me understand the complete workflow.

👤 About Me

Kadimetla Jagadeeshwar Reddy (2300080179)
Student at KL University
Interested in Machine Learning, AI, and Full Stack Development.

⭐ If you liked this project, please star the repo 😊
