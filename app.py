from flask import Flask, render_template, request
import joblib
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)

# Define paths relative to the app.py file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_FOLDER = os.path.join(BASE_DIR, "model")
MODEL_PATH = os.path.join(MODEL_FOLDER, "logistic_model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_FOLDER, "tfidf_vectorizer.pkl")

# Load model and vectorizer safely
try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    logger.info("✅ Model and vectorizer loaded successfully.")
except FileNotFoundError as e:
    logger.error(f"❌ File not found: {e}")
    model = None
    vectorizer = None

@app.route('/')
def index():
    return render_template('test2.html')

@app.route('/detector')
def detector():
    return render_template('test.html')

@app.route('/about')
def about():
    return render_template('test3.html')

@app.route('/contact')
def contact():
    return render_template('test4.html')

# 🟢 Add this new route
@app.route('/predict', methods=['POST'])
def predict():
    if not model or not vectorizer:
        return render_template('test.html', error="Model not loaded. Please try again later.")

    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()

    if not description:
        return render_template('test.html', error="Please enter a job description.")

    try:
        # Transform input using TF-IDF
        features = vectorizer.transform([description])
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][prediction]

        result = "🛑 Fake Job Posting" if prediction == 1 else "✅ Real Job Posting"
        confidence = round(probability * 100, 2)

        return render_template('test.html', prediction=result, probability=confidence, job_title=title, job_description=description)

    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        return render_template('test.html', error=f"Prediction failed: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)