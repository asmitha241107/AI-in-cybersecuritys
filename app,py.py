from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import streamlit as st

# Training data
messages = [
    "Congratulations! You won a prize. Click this link now",
    "Your bank account is blocked. Verify your account immediately",
    "Urgent! You have won a lottery",
    "Click here to claim your free gift",
    "Your password has expired. Login immediately",

    "Hi, can we meet tomorrow?",
    "Your college assignment is due tomorrow",
    "The meeting is scheduled at 10 AM",
    "Please send me the project report",
    "Happy birthday! Have a great day"
]

# 1 = Phishing, 0 = Safe
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# Convert text into numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(messages)

# Train AI model
model = LogisticRegression()
model.fit(X, labels)

# Streamlit app
st.title("🛡️ AI Cybersecurity - Phishing Detector")

st.write("Enter a message or email below:")

user_message = st.text_area("Message")

if st.button("Check Message"):

    if user_message.strip() == "":
        st.warning("Please enter a message.")

    else:
        message_vector = vectorizer.transform([user_message])
        prediction = model.predict(message_vector)[0]

        if prediction == 1:
            st.error("⚠️ Warning: Possible Phishing Message!")
        else:
            st.success("✅ Message looks Safe.")