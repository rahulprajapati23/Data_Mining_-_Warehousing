import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from textblob import TextBlob
import re
import emoji
import random
import os

# 1. Setup and Resource Download
os.chdir(os.path.dirname(os.path.abspath(__file__)))
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

# 2. Loading the Dataset
main_dataset = 'ShinzoabeCombinedTweets_20220709-205347.csv.gzip'
df = pd.read_csv(main_dataset, compression='gzip')
df['text'] = df['text'].astype(str)

# 3. Simple Sentiment Analysis Function
def get_tweet_sentiment(text_content):
    analysis = TextBlob(text_content)
    score = analysis.sentiment.polarity
    if score > 0:
        return 'Positive'
    elif score < 0:
        return 'Negative'
    else:
        return 'Neutral'

# --- Output Report Starts ---
print("=" * 60)
print("             Twitter Data Analysis (DMW05)")
print("=" * 60)

# 1-2) Text Mining Basics
total_tweets = len(df)
unique_tweets = df['text'].nunique()
print(f"\n1) Total count of tweets: {total_tweets}")
print(f"2) Total count of unique tweets: {unique_tweets}")

# 3) Particular Tweet Analysis
random_row = df.sample(1).iloc[0]
raw_text = random_row['text']
# Clean newlines for pretty printing (using a separate variable for simple syntax)
printable_text = raw_text.replace('\n', ' ')
sentiment_result = get_tweet_sentiment(raw_text)

print(f"\n3) Particular Tweet Analysis:")
print(f"   Tweet ID:  {random_row['tweetid']}")
print(f"   Full Text: {printable_text[:120]}...")
print(f"   Sentiment: {sentiment_result}")

# 4) Sentiment Distribution Calculation
print("\n[INFO] Calculating sentiments for all tweets... (takes about 30 seconds)")
df['sentiment'] = df['text'].apply(get_tweet_sentiment)
counts = df['sentiment'].value_counts()

pos_total = counts.get('Positive', 0)
neg_total = counts.get('Negative', 0)
neu_total = counts.get('Neutral', 0)

print(f"4) Sentiment Statistics:")
print(f"   Number of Positive: {pos_total}")
print(f"   Number of Negative: {neg_total}")
print(f"   Number of Neutral:  {neu_total}")

# 5) Data Visualization (Charts)
print("\n5) Generating Sentiment Charts...")
plt.figure(figsize=(10, 5))

# Subplot 1: Pie Chart
plt.subplot(1, 2, 1)
pie_labels = ['Positive', 'Negative']
pie_values = [pos_total, neg_total]
plt.pie(pie_values, labels=pie_labels, autopct='%1.1f%%', colors=['#4CAF50', '#F44336'])
plt.title("Sentiment Percentage (%)")

# Subplot 2: Bar Chart
plt.subplot(1, 2, 2)
plt.bar(['Positive', 'Negative'], [pos_total, neg_total], color=['#4CAF50', '#F44336'])
plt.title("Sentiment Counts")
plt.ylabel("Tweet Count")

plt.tight_layout()
plt.savefig("sentiment_distributions.png")
plt.close()

# 6) Word Cloud Generation
print("6) Generating Word Clouds for Moods...")
for mood in ['Positive', 'Negative']:
    mood_filter = df[df['sentiment'] == mood]
    mood_sample = mood_filter['text'].sample(min(len(mood_filter), 5000))
    combined_words = " ".join(mood_sample)
    
    wordcloud_img = WordCloud(width=800, height=400, background_color='white').generate(combined_words)
    wordcloud_img.to_file(f"{mood.lower()}_wordcloud_hai.png")
    print(f"   -> Created {mood.lower()}_wordcloud_hai.png")

# 7-9) Data Cleaning Examples
print("\n--- Data Cleaning Samples ---")

# 7) Clean a Retweet
rt_df = df[df['text'].str.startswith("RT @")]
if not rt_df.empty:
    orig_rt = rt_df.sample(1).iloc[0]['text']
    # Clean up for printing
    print_orig_rt = orig_rt.replace('\n', ' ')
    # Remove 'RT @user: ' pattern
    cleaned_rt = re.sub(r"^RT @\w+: ", "", orig_rt)
    cleaned_rt = re.sub(r"^RT ", "", cleaned_rt)
    print_cleaned_rt = cleaned_rt.replace('\n', ' ')
    
    print(f"7) Cleaned Retweet:")
    print(f"   Original: {print_orig_rt[:80]}...")
    print(f"   Cleaned:  {print_cleaned_rt[:80]}...")

# 8) Remove Handles and Hashtags
sample_tweet_raw = df.sample(1).iloc[0]['text']
# Clean @handles and #hashtags
clean_step1 = re.sub(r"@\w+", "", sample_tweet_raw)
clean_step2 = re.sub(r"#\w+", "", clean_step1)
final_clean = clean_step2.strip()

print_orig_sample = sample_tweet_raw.replace('\n', ' ')
print_final_clean = final_clean.replace('\n', ' ')

print(f"8) Removing Handles and Hashtags:")
print(f"   Original: {print_orig_sample[:80]}...")
print(f"   Cleaned:  {print_final_clean[:80]}...")

# 9) Emoji Handling (Replacement)
emoji_tweet_found = None
for text_val in df['text'].sample(min(5000, len(df))):
    if emoji.emoji_count(text_val) > 0:
        emoji_tweet_found = text_val
        break

if emoji_tweet_found:
    text_with_words = emoji.demojize(emoji_tweet_found)
    print_emoji_orig = emoji_tweet_found.replace('\n', ' ')
    print_emoji_clean = text_with_words.replace('\n', ' ')
    
    print(f"9) Emoji Conversion:")
    print(f"   Original: {print_emoji_orig[:80]}...")
    print(f"   As Text:  {print_emoji_clean[:80]}...")

# 10-11) Language Processing
print("\n--- Language Processing ---")
from nltk.corpus import stopwords
all_stops = stopwords.words('english')
print(f"10) English Stopwords Sample: {', '.join(all_stops[:10])}...")

nlp_sample_text = df.sample(1).iloc[0]['text'].replace('\n', ' ')
sentences = nltk.sent_tokenize(nlp_sample_text)
words_list = nltk.word_tokenize(nlp_sample_text)

print(f"11) Tokenization on random text:")
print(f"    Text:      {nlp_sample_text[:80]}...")
print(f"    Sentences: {sentences[:2]}")
print(f"    Words:     {words_list[:10]}...")

print("\n" + "=" * 60)
print("             Processing Successfully Completed!")
print("=" * 60)
