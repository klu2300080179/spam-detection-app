import streamlit as st
import joblib

model = joblib.load("best_svm_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("📩 Email Spam Detection App")
st.write("Enter a message below and the model will classify it as **Spam** or **Not Spam**.")

user_input = st.text_area("Enter your message here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        transformed = vectorizer.transform([user_input])
        prediction = model.predict(transformed)[0]

        if prediction == 1:
            st.error("🚨 This message is classified as **SPAM**!")
        else:
            st.success("✔ This message is classified as **NOT SPAM**.")
