import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# Load model
with open('random_forest_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Load the vectorizer
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)


#Load LabelEnocder for inversing the encoding of target variable
with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Basic preprocessor
def preprocess_tweet(text):
    text = re.sub(r'http\S+', '', text)  
    text = re.sub(r'@\w+', '', text)     # Remove mentions
    text = re.sub(r'#\w+', '', text)     # Remove hashtags
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove punctuations and numbers
    text = text.lower().strip()
    return text


# Function to predict sentiment of custom tweet
def predict_sentiment(tweet_text):
    # Transform tweet using saved vectorizer
    vectorized_tweet = vectorizer.transform([tweet_text]).toarray()
    
    # Predict sentiment
    prediction_encoded = loaded_model.predict(vectorized_tweet)[0]
    
    # Decode label to original class
    predicted_label = label_encoder.inverse_transform([prediction_encoded])[0]
    
    return predicted_label

#  Example usage
while True:
    tweet = preprocess_tweet(input("Enter a tweet (or type 'exit' to quit): "))
    if tweet.lower() == 'exit':
        break
    sentiment = predict_sentiment(tweet)
    print(f" Predicted Sentiment: {sentiment}\n")