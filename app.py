import streamlit as st
import pickle

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="Emotion Detection",
    page_icon="🧠",
    layout="wide"
)

# ---------------------- LOAD MODEL ----------------------
with open("emotion_pipline.pkl", "rb") as file:
    pipeline = pickle.load(file)

# ---------------------- TITLE ----------------------
st.title("🧠 Emotion Detection from Text")

st.markdown("""
This application predicts the emotion expressed in text using
Natural Language Processing and Machine Learning.
""")

# ---------------------- SIDEBAR ----------------------
st.sidebar.title("📌 About")

st.sidebar.markdown("""
### Model Information

- **Algorithm:** Logistic Regression
- **Vectorizer:** TF-IDF
- **Accuracy:** 89%
- **Classes:** 6

### Detects

- 😊 Joy
- 😢 Sadness
- 😡 Anger
- 😨 Fear
- ❤️ Love
- 😲 Surprise
""")

# ---------------------- INPUT ----------------------
text = st.text_area(
    "Enter your text",
    height=180,
    placeholder="Type your sentence here..."
)

# ---------------------- BUTTON ----------------------
if st.button("🔍 Predict Emotion"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:

        prediction = pipeline.predict([text])[0]

        if prediction == 2:
            st.success("😊 The text expresses **Joy**. The person appears happy, positive, or excited.")

        elif prediction == 4:
            st.info("😢 The text expresses **Sadness**. The person seems disappointed or unhappy.")

        elif prediction == 0:
            st.error("😡 The text expresses **Anger**. The message reflects frustration or irritation.")

        elif prediction == 1:
            st.warning("😨 The text expresses **Fear**. The person appears worried, anxious, or scared.")

        elif prediction == 3:
            st.success("❤️ The text expresses **Love**. The message conveys affection, care, or warmth.")

        elif prediction == 5:
            st.info("😲 The text expresses **Surprise**. The message indicates amazement or unexpected emotions.")