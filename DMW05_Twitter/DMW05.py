import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from textblob import TextBlob
import re
import emoji
import random
import os

# Set working directory to the script's directory so it runs properly from anywhere
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("="*50)
print("Twitter Data Analysis (DMW05)")
print("="*50)

# Download NLTK data quietly if not present
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# File paths
main_dataset = 'ShinzoabeCombinedTweets_20220709-205347.csv.gzip'

print(f"\n[INFO] Loading dataset '{main_dataset}'...")
df = pd.read_csv(main_dataset, compression='gzip')

# Preprocessing
df['text'] = df['text'].astype(str)

print("\n--- Text Mining ---")
# 1) Total number of tweets
total_tweets = len(df)
print(f"1) Total number of tweets: {total_tweets}")

# 2) Total number of unique tweets
unique_tweets = df['text'].nunique()
print(f"2) Total number of unique tweets: {unique_tweets}")

# Helper for sentiment
def get_sentiment(text):
    pol = TextBlob(str(text)).sentiment.polarity
    if pol > 0:
        return 'Positive'
    elif pol < 0:
        return 'Negative'
    else:
        return 'Neutral'

# 3) Particular tweet
sample_idx = random.choice(df.index)
sample_tweet = df.loc[sample_idx]
sample_tweet_id = sample_tweet['tweetid']
sample_tweet_text = sample_tweet['text']
sample_sentiment = get_sentiment(sample_tweet_text)

print(f"\n3) Particular Tweet Analysis:")
print(f"   Index: {sample_idx}")
print(f"   Tweet ID: {sample_tweet_id}")
print(f"   Text: {sample_tweet_text}")
print(f"   Sentiment: {sample_sentiment}")

# 4) Total positive and negative
print("\n[INFO] Calculating sentiments for all tweets... (this will take ~30 seconds)")
# Using TextBlob on all tweets
df['sentiment'] = df['text'].apply(get_sentiment)

sentiment_counts = df['sentiment'].value_counts()
total_pos = sentiment_counts.get('Positive', 0)
total_neg = sentiment_counts.get('Negative', 0)
total_neu = sentiment_counts.get('Neutral', 0)

print(f"\n4) Number of Positive tweets: {total_pos}")
print(f"   Number of Negative tweets: {total_neg}")
print(f"   (Number of Neutral tweets: {total_neu})")

print("\n--- Data Visualization ---")
print("5) Plotting Positive/Negative percentages (Pie & Bar charts)...")
plt.figure(figsize=(12, 5))

plot_data = [total_pos, total_neg]
plot_labels = ['Positive', 'Negative']
colors = ['#4CAF50', '#F44336']

plt.subplot(1, 2, 1)
plt.pie(plot_data, labels=plot_labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title("Percentage of Positive vs Negative Tweets")

plt.subplot(1, 2, 2)
plt.bar(plot_labels, plot_data, color=colors)
plt.title("Count of Positive vs Negative Tweets")
plt.ylabel("Number of Tweets")

plt.tight_layout()
plt.savefig("sentiment_distributions.png")
print("   -> Saved 'sentiment_distributions.png'")
plt.close()

print("\n6) Generating Word Clouds for Positive and Negative tweets...")
pos_text_subset = " ".join(df[df['sentiment'] == 'Positive']['text'].sample(n=min(20000, total_pos), replace=True).tolist())
neg_text_subset = " ".join(df[df['sentiment'] == 'Negative']['text'].sample(n=min(20000, total_neg), replace=True).tolist())

if pos_text_subset:
    pos_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(pos_text_subset)
    plt.figure(figsize=(10, 5))
    plt.imshow(pos_wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Positive Tweets")
    plt.savefig("positive_wordcloud.png")
    plt.close()
    print("   -> Saved 'positive_wordcloud.png'")

if neg_text_subset:
    neg_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(neg_text_subset)
    plt.figure(figsize=(10, 5))
    plt.imshow(neg_wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Negative Tweets")
    plt.savefig("negative_wordcloud.png")
    plt.close()
    print("   -> Saved 'negative_wordcloud.png'")

print("\n--- Data Cleaning ---")
# 7) Select any random retweet and display its actual text by removing RT
retweet_mask = df['text'].str.startswith("RT @")
if retweet_mask.any():
    rand_rt = df[retweet_mask].sample(1).iloc[0]['text']
    cleaned_rt = re.sub(r"^RT @[A-Za-z0-9_]+: ", "", rand_rt)
    cleaned_rt = re.sub(r"^RT ", "", cleaned_rt)
    print(f"7) Random Retweet Original:\n   {rand_rt}")
    print(f"   Cleaned (Removed RT):\n   {cleaned_rt}")
else:
    print("7) No retweets found starting with 'RT @'.")

# 8) Remove hashtags and @handle
rand_tweet = df.sample(1).iloc[0]['text']
cleaned_handles = re.sub(r'@[A-Za-z0-9_]+', '', rand_tweet)
cleaned_handles_tags = re.sub(r'#\w+', '', cleaned_handles)
cleaned_text = cleaned_handles_tags.strip()

print(f"\n8) Random Tweet Original:\n   {rand_tweet}")
print(f"   Cleaned (No @handles or #hashtags):\n   {cleaned_text}")

# 9) Emoji tweet
print("\n9) Searching for a tweet with an emoji...")
tweet_with_emoji = None
for txt in df['text'].sample(min(5000, len(df))):
    if emoji.emoji_count(txt) > 0:
        tweet_with_emoji = txt
        break

if tweet_with_emoji:
    demojized_text = emoji.demojize(tweet_with_emoji)
    print(f"   Original Tweet with Emoji:\n   {tweet_with_emoji}")
    print(f"   Cleaned (Emoji Replaced with Text):\n   {demojized_text}")
else:
    print("   Could not find a tweet with emoji in the sample.")

print("\n--- Language Processing ---")
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print(f"10) English Stopwords ({len(stop_words)} total):")
print(f"    {', '.join(stop_words[:20])}... [truncated]")

raw_text_for_nlp = df.sample(1).iloc[0]['text']
sentences = nltk.sent_tokenize(raw_text_for_nlp)
words = nltk.word_tokenize(raw_text_for_nlp)

print(f"\n11) Tokenization on a random text:")
print(f"    Raw Text:\n    {raw_text_for_nlp}")
print(f"    Statements (Sentences): {sentences}")
print(f"    Words (Tokens): {words}")

print("\n[INFO] Complete!")
