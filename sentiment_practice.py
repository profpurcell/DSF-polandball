# INSTALL FIRST
# Make sure you install the VADER lexicon and sentiment analysis before running this
# Just remove the hashtags from the code below

# Code to install VADER:
# import nltk
# nltk.download('vader_lexicon')
# nltk.download('punkt')


from nltk.sentiment.vader import SentimentIntensityAnalyzer

# next, we initialize VADER so we can use it within our Python script
## basically, turn out SentimentIntensityAnalyzer into an object recognized by Python
sid = SentimentIntensityAnalyzer()

#import pandas and 2020 commentList
import pandas as pd
import warnings

comment_df = pd.read_csv("commentList_201006.csv") 

# Finding sentiments of each comment

negative_sentiment, neutral_sentiment, positive_sentiment = [], [], []

def analyze_sentiment(row):
    body = row["body"]
    scores = sid.polarity_scores(body)
    negative_sentiment.append(scores["neg"])
    neutral_sentiment.append(scores["neu"])
    positive_sentiment.append(scores["pos"])
    return(scores["compound"])

# Create new columns that contain each sentiment score
comment_df["compound_sentiment"] = comment_df.apply(analyze_sentiment, axis = 1)
comment_df["negative_sentiment"] = negative_sentiment
comment_df["neutral_sentiment"] = neutral_sentiment
comment_df["positive_sentiment"] = positive_sentiment

# Generate a new csv with the sentiment columns
comment_df.to_csv("newCommentList201006.csv")
