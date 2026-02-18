import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load and prepare data
data_path = "mail_data.csv"
df = pd.read_csv(data_path)
df = df.where((pd.notnull(df)), ' ')
df.loc[df['Category'] == 'spam', 'Category'] = 0
df.loc[df['Category'] == 'ham', 'Category'] = 1

X = df['Message']
y = df['Category'].astype('int')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)

vectorizer = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_train_features, y_train)

# Streamlit UI
st.title("📧 Spam Mail Classifier")
st.write("Enter your mail to check whether it is Spam or Ham")

# Session state
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

st.session_state.user_input = st.text_area("Your message:", value=st.session_state.user_input)

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Classify Message"):
        if st.session_state.user_input.strip():
            input_data = vectorizer.transform([st.session_state.user_input])
            prediction = model.predict(input_data)
            result = "Ham mail" if prediction[0] == 1 else "Spam mail"
            st.success(f"Prediction: {result}")
        else:
            st.warning("Please enter a message before clicking the button.")

with col2:
    if st.button("Check another mail"):
        st.session_state.user_input = ""
        st.rerun()
