import pandas as pd
from textblob import TextBlob

# Read the CSV file with 'latin-1' encoding
df = pd.read_csv('tweet.csv', encoding='latin-1')

# Rest of the code remains the same
print(df.head())

df['sentiment'] = df['tweet'].apply(lambda tweet: TextBlob(tweet).sentiment.polarity)

def get_sentiment_label(score):
    if score > 0:
        return 'positive'
    elif score < 0:
        return 'negative'
    else:
        return 'neutral'

df['sentiment_label'] = df['sentiment'].apply(get_sentiment_label)

print(df[['tweet', 'sentiment', 'sentiment_label']])
