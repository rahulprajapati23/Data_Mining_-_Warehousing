import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from textblob import TextBlob
import re, emoji, random, os

# Setup and Data Loading
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("="*50 + "\nTwitter Data Analysis (DMW05)\n" + "="*50)

for res in ['stopwords', 'punkt_tab', 'punkt']:
    try: nltk.data.find(f'tokenizers/{res}' if 'punkt' in res else f'corpora/{res}')
    except LookupError: nltk.download(res, quiet=True)

df = pd.read_csv('ShinzoabeCombinedTweets_20220709-205347.csv.gzip', compression='gzip')
df['text'] = df['text'].astype(str)

def get_sent(t):
    pol = TextBlob(str(t)).sentiment.polarity
    return 'Positive' if pol > 0 else ('Negative' if pol < 0 else 'Neutral')

# 1-3) Text Mining & Sample Analysis
print(f"\n--- Text Mining ---\n1) Total tweets: {len(df)}\n2) Unique tweets: {df['text'].nunique()}")
s_idx = random.choice(df.index)
s_tweet = df.loc[s_idx]
print(f"\n3) Particular Tweet Analysis:\n   Index: {s_idx}\n   ID: {s_tweet['tweetid']}\n   Text: {s_tweet['text']}\n   Sentiment: {get_sent(s_tweet['text'])}")

# 4) Sentiment Calculation
print("\n[INFO] Calculating sentiments... (takes ~30s)")
df['sentiment'] = df['text'].apply(get_sent)
counts = df['sentiment'].value_counts()
pos, neg, neu = counts.get('Positive',0), counts.get('Negative',0), counts.get('Neutral',0)
print(f"\n4) Results: Positive: {pos}, Negative: {neg}, Neutral: {neu}")

# 5) Data Visualization
print("\n--- Data Visualization ---\n5) Plotting distributions...")
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1); plt.pie([pos, neg], labels=['Positive', 'Negative'], autopct='%1.1f%%', colors=['#4CAF50', '#F44336'], startangle=140); plt.title("Sentiment %")
plt.subplot(1, 2, 2); plt.bar(['Positive', 'Negative'], [pos, neg], color=['#4CAF50', '#F44336']); plt.title("Sentiment Counts"); plt.ylabel("Tweets")
plt.tight_layout(); plt.savefig("sentiment_distributions.png"); plt.close()

# 6) Word Clouds
print("6) Generating word clouds...")
for label, filename in [('Positive', 'positive_wordcloud_HAI.png'), ('Negative', 'negative_wordcloud_HAI.png')]:
    text = " ".join(df[df['sentiment'] == label]['text'].sample(n=min(20000, counts.get(label, 0)), replace=True))
    if text:
        WordCloud(width=800, height=400, background_color='white').generate(text).to_file(filename)
        print(f"   -> Saved '{filename}'")

# 7-9) Data Cleaning
print("\n--- Data Cleaning ---")
rt = df[df['text'].str.startswith("RT @")]
if not rt.empty:
    orig = rt.sample(1).iloc[0]['text']
    clean_rt = re.sub(r'^RT @[A-Za-z0-9_]+: |^RT ', '', orig)
    print(f"7) RT Cleaned:\n   Orig: {orig}\n   Clean: {clean_rt}")

rand_t = df.sample(1).iloc[0]['text']
clean_rand = re.sub(r'@[A-Za-z0-9_]+|#\w+', '', rand_t).strip()
print(f"8) Handles/Hashtags Cleaned:\n   Orig: {rand_t}\n   Clean: {clean_rand}")

emoji_t = next((t for t in df['text'].sample(min(5000, len(df))) if emoji.emoji_count(t) > 0), None)
if emoji_t:
    print(f"9) Emoji Cleaned:\n   Orig: {emoji_t}\n   Clean: {emoji.demojize(emoji_t)}")

# 10-11) Language Processing
from nltk.corpus import stopwords
print(f"\n--- Language Processing ---\n10) English Stopwords: {', '.join(stopwords.words('english')[:20])}...")
raw_nlp = df.sample(1).iloc[0]['text']
print(f"\n11) Tokenization:\n    Text: {raw_nlp}\n    Sentences: {nltk.sent_tokenize(raw_nlp)}\n    Words: {nltk.word_tokenize(raw_nlp)}")

print("\n[INFO] Complete!")
