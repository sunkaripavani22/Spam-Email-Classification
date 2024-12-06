# Email Spam Classification Project

---

## Overview
This project demonstrates a **Machine Learning application for email spam classification**, using a pre-trained model to classify emails as either **spam** or **not spam (ham)**. The application was built using **Streamlit** for an interactive interface and Python for the backend logic.

The notebook included in the repository shows the full pipeline of data preprocessing, feature extraction, model training, evaluation, and deployment. The trained model and vectorizer have been serialized using `pickle` for reusability in the Streamlit app.

---

## Features

1. **Interactive Interface**:
   - Enter an email and click "Classify" to check whether it is spam or not.
   - Results are displayed in real-time with appropriate success/error messages.

2. **End-to-End Workflow**:
   - Data is preprocessed to handle spam labels and message text.
   - Feature extraction is done using `CountVectorizer`.
   - A **Naive Bayes classifier** (MultinomialNB) is trained for classification.

3. **Model Persistence**:
   - The trained model and vectorizer are saved as `pickle` files (`spam123.pkl` and `vec123.pkl`) for easy integration into the application.

---

## Files in the Repository

1. **Streamlit App Script** (`spamdetector.py`):
   The main script for running the email classification application using Streamlit.

2. **IPython Notebook** (`spam Detector.ipynb`):
   - Shows the detailed steps of the machine learning pipeline:
     - Loading and preprocessing data.
     - Splitting the dataset for training and testing.
     - Training the classifier.
     - Saving the trained model and vectorizer.

3. **Trained Model and Vectorizer**:
   - `spam123.pkl`: The serialized Naive Bayes model.
   - `vec123.pkl`: The serialized `CountVectorizer` instance.

---

## How to Run the Project

1. **Run the Streamlit App**:
   - Install the required Python packages: `streamlit`, `scikit-learn`, etc.
   - Run the app with:
     ```bash
     streamlit run spamdetector.py
     ```
   - Open the local URL in a browser to access the app.

2. **Explore the Notebook**:
   - Open `spam Detector.ipynb` to understand the data processing and model training steps.
   - The notebook is fully annotated for educational purposes.

---

## Requirements

- Python 3.7+
- Libraries:
  - `streamlit`
  - `numpy`
  - `pandas`
  - `scikit-learn`
  - `pickle`

---

## Acknowledgments
- This project uses a Naive Bayes classifier and `CountVectorizer` from scikit-learn.
- Streamlit is used for creating the web interface.
