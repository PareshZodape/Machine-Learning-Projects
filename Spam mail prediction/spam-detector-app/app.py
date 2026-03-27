import streamlit as st
import pickle

# Load saved files
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Title
st.title("📧 Spam Mail Detector")

# Input box
email_text = st.text_area("Enter Email Content")

# Button
if st.button("Predict"):
    if email_text.strip() != "":
        # Convert text
        input_data = vectorizer.transform([email_text])

        # Prediction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0]

        if prediction == 0:
            st.error(f"🚨 Spam Mail (Confidence: {probability[0]*100:.2f}%)")
        else:
            st.success(f"✅ Not Spam (Confidence: {probability[1]*100:.2f}%)")
    else:
        st.warning("Please enter some text")
