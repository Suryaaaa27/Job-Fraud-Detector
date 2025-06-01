🎯 Project Title: Job Fraud Detector

🔍 A web-based tool that detects whether a job posting is real or fraudulent using machine learning and Flask.
Built with ❤️ to help job seekers avoid scams and fake job postings online.

📌 Features
✅ Job Description Analysis : Paste any job description and get an instant prediction.
🧠 Powered by a trained ML model (logistic_model.pkl) and TF-IDF Vectorizer.
🌙 Dark Mode Toggle : Persistent dark mode using localStorage.
🧱 Fully responsive and modern UI using HTML/CSS/JS (no frameworks).
🚀 Easy to deploy — works locally and in production environments like Render or Heroku.

🖥️ How It Works
User enters a job title and description.
The input is transformed using a TF-IDF vectorizer.
Logistic regression model predicts if the job is real or fake.
Confidence percentage is shown alongside the result.
Dark mode toggle persists across page reloads.

🛠 Tech Stack
Python 3.x
Flask – Lightweight backend framework
HTML5 , CSS3 , JavaScript – For frontend UI
joblib – To load .pkl model files
Jinja2 Templates – For dynamic rendering
Numpy – For numerical operations

📁 Folder Structure
GAN/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── templates/
│   ├── test.html           # Detection Form Page
│   ├── test2.html          # Landing / Home Page
│   ├── test3.html          # About Page
│   └── test4.html          # Contact Page
├── model/
│   ├── logistic_model.pkl  # Trained model
│   └── tfidf_vectorizer.pkl # TF-IDF Vectorizer
└── static/                 # Static assets (optional)
    ├── css/
    └── js/

💻 Local Setup

Clone the repo:
git clone https://github.com/yourusername/job-fraud-detector.git 

Install dependencies:
pip install -r requirements.txt

Run the app:
python app.py

Visit:
http://localhost:5000

📝 Requirements.txt
Flask==3.0.0
numpy==2.0.0
joblib==1.3.2
gunicorn==21.2.0

📌 Sample Screenshot
![Screenshot 2025-05-30 210636](https://github.com/user-attachments/assets/53aa47ee-f901-49c3-a185-4acd245d6093)
![Screenshot 2025-05-30 210539](https://github.com/user-attachments/assets/8bfcfe88-c8c7-46be-bbaa-e495f885edcb)




🤝 Contributing:
Contributions are welcome! Please read the contributing guidelines first.

📬 Feedback or Issues?:
Have feedback or found a bug? Open an issue or reach out!

👨‍💻 Author:
Surya Kumar Srivastava
LinkedIn: linkedin.com/in/surya-kumar-srivastava
GitHub: github.com/Suryaaaa27

📜 License:
MIT © Surya Kumar Srivastava
