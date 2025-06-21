# 🐦 Twitter Sentiment Analyzer

This project performs sentiment analysis on tweets fetched using the **Tweepy v2 API**, classifying them as **Positive**, **Negative**, or **Neutral** using machine learning models and natural language processing techniques.

---

## 📌 Features

- 🔗 Fetch tweets in real-time using **Tweepy v2 API**
- 🧹 Clean and preprocess tweet texts (removal of mentions, hashtags, URLs, etc.)
- 🧠 Train and test ML models using **scikit-learn**
- 🧾 Validate predictions using **TextBlob**
- 📊 Display sentiment distribution and insights
- 💾 Export results to CSV

---

## 🛠 Tech Stack

- Python
- Tweepy v2 (Twitter API v2)
- scikit-learn
- TextBlob
- Pandas, NumPy
- Matplotlib / Seaborn (for optional visualization)
- Jupyter Notebook / Python Script

---

## 🚀 How to Run

1. **Clone the Repository**

```bash
git clone https://github.com/<your-username>/twitter-sentiment-analyzer.git
cd twitter-sentiment-analyzer

2. **Create Virtual Environment**
python -m venv venv
venv\Scripts\activate     # Windows
# or
source venv/bin/activate  # macOS/Linux

3. **Install Dependencies**
pip install -r requirements.txt

4.**Set Up Twitter API Keys**
Create a .env file or set environment variables for:

TWITTER_BEARER_TOKEN

You can get this from your Twitter Developer account (Elevated access required).

5.  **Run the Script/Notebook**
python sentiment_analyzer.py
# or
jupyter notebook sentiment_analysis.ipynb
