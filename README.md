📩 Spam Detection App (ML + NLP + Streamlit)

A machine learning web application that classifies SMS/email messages as Spam or Not Spam using TF-IDF and a Support Vector Machine (SVM) classifier.
The project includes data preprocessing, model training, evaluation, and deployment on Streamlit Cloud.

🚀 Live Demo

🟢 View the live app here:
👉 https://spam-detection-app-beyhgafu59p6iuwe6zctbd.streamlit.app/

📌 Project Overview

This project builds a complete end-to-end Machine Learning pipeline:

✔ Text preprocessing
✔ Label encoding
✔ TF-IDF vectorization
✔ Training 5+ ML models
✔ Selecting best model (SVM)
✔ Saving model with pickle
✔ Developing a Streamlit Web App
✔ Deploying online

The app allows users to enter any message and instantly get a prediction whether it is Spam or Not Spam.

🧠 Machine Learning Models Used

The following ML models were trained and evaluated:

Model	Accuracy
Logistic Regression	94%
Naive Bayes	96.8%
Decision Tree	96.8%
Random Forest	97.7%
SVM (Selected)	97.5%

👉 SVM showed the best balance of accuracy, precision, recall, and F1-score — especially for identifying spam — so it was chosen for deployment.

🛠️ Technologies Used
Machine Learning

Scikit-learn

SVM (Support Vector Machine)

TF-IDF vectorization

NLP (Text Processing)

Tokenization

Cleaning

Removing stopwords

Feature extraction (TF-IDF)

Deployment

Streamlit

Streamlit Cloud

Pickle (model persistence)

Development Tools

Python

Google Colab

GitHub

📂 Project Structure
spam-detection-app/
│
├── app.py                      # Streamlit application
├── best_svm_model.pkl          # Trained SVM model
├── tfidf_vectorizer.pkl        # TF-IDF transformer
├── requirements.txt            # Required Python packages
└── README.md                   # Project documentation

⚙️ How to Run Locally
1️⃣ Clone the repository:
git clone https://github.com/klu2300080179/spam-detection-app.git
cd spam-detection-app

2️⃣ Install dependencies:
pip install -r requirements.txt

3️⃣ Run the Streamlit app:
streamlit run app.py


The app will open at:

http://localhost:8501

📊 Model Evaluation (SVM)
Metric	Ham (0)	Spam (1)
Precision	0.98	0.97
Recall	1.00	0.84
F1-score	0.99	0.90

SVM gave the best recall for spam compared to other models.

🎨 Streamlit App Preview
📩 Email Spam Detection App
Enter a message below and the model will classify it as Spam or Not Spam.


Input box → Predict button → Result displayed as ✔ “Not Spam” or 🚨 “Spam”.

🏁 Conclusion

This project demonstrates:

Text classification using ML

Complete preprocessing & feature engineering

Multi-model comparison

Streamlit UI development

Deployment to a live production environment

It’s a strong portfolio project for ML, NLP, and full-stack data science.

👨‍💻 Author

Kadimetla Jagadeeshwar Reddy (2300080179)
Undergraduate student at KL University
Passionate about Machine Learning, AI, and full-stack development.

⭐ If you like this project

Please star ⭐ the repository on GitHub!
