# Data Mining & Warehousing: Library and Function Notes

This document provides a detailed explanation of the Python libraries and their specific functions used across the simplified project scripts.

---

## 1. Core Data Manipulation & Analysis

### **Pandas (`import pandas as pd`)**
Used for data structures and data analysis tools.
- **`pd.read_csv()`**: Loads data from a CSV file. Used in `DMW05_Twitter`.
- **`pd.read_excel()`**: Loads data from an Excel file (.xlsx). Used in `P02_NBA` and `P03_Employee`.
- **`pd.DataFrame()`**: Creates a 2D table-like structure (DataFrame) from dictionaries or lists.
- **`df.head()`**: Returns the first n rows of a DataFrame (default is 5).
- **`df.nunique()`**: Counts the number of unique values in a column or across the whole DataFrame.
- **`df.value_counts()`**: Counts the unique occurrences of values in a specific column.
- **`df.groupby()`**: Groups data based on a column to perform aggregate operations (like sum, mean, max).
- **`df.loc[]`**: Accesses a group of rows and columns by labels or a boolean array.
- **`df.sample()`**: Returns a random sample of rows from the DataFrame.
- **`df.to_excel()`**: Exports the DataFrame to an Excel file.
- **`pd.cut()`**: Segments and sorts data values into bins (used for categorization).
- **`pd.to_numeric()`**: Converts arguments to a numeric type (float or int).

### **NumPy (`import numpy as np`)**
Used for scientific computing and handling multidimensional arrays.
- **`np.linspace()`**: Creates an evenly spaced sequence of numbers over a specified range (used for binning).
- **`np.array_split()`**: Splits an array into multiple sub-arrays (used for equal frequency binning).
- **`np.median()`**: Calculates the median value of a dataset.

---

## 2. Web Scraping

### **Requests (`import requests`)**
Used for making HTTP requests to fetch web content.
- **`requests.get()`**: Sends a GET request to a specified URL to retrieve the page content.
- **`response.raise_for_status()`**: Checks if the request was successful; raises an error if the status code indicates failure.

### **BeautifulSoup (`from bs4 import BeautifulSoup`)**
Used for parsing HTML and XML documents and extracting data.
- **`BeautifulSoup(text, "html.parser")`**: Creates a parse tree for the HTML text.
- **`soup.find_all()`**: Searches the HTML for all occurrences of a specific tag or class.
- **`tag.text.strip()`**: Extracts the text from an HTML tag and removes leading/trailing whitespace.
- **`tag.get('attribute')`**: Retrieves the value of a specific HTML attribute (like 'title' or 'href').

---

## 3. Natural Language Processing (NLP) & Sentiment Analysis

### **NLTK (`import nltk`)**
The Natural Language Toolkit, used for text processing and linguistic analysis.
- **`nltk.download()`**: Downloads specific datasets or models (like stopwords or tokenizers).
- **`nltk.sent_tokenize()`**: Breaks a block of text into individual sentences.
- **`nltk.word_tokenize()`**: Breaks a sentence or text into individual words (tokens).
- **`stopwords.words('english')`**: Retrieves a list of common English words that are usually filtered out (e.g., "is", "the", "and").

### **TextBlob (`from textblob import TextBlob`)**
A simple library for processing textual data, including sentiment analysis.
- **`TextBlob(text)`**: Creates a TextBlob object for processing.
- **`.sentiment.polarity`**: Calculates a score from -1 (Negative) to +1 (Positive) representing the sentiment of the text.

### **WordCloud (`from wordcloud import WordCloud`)**
Used for creating visual representations of word frequencies.
- **`WordCloud().generate(text)`**: Creates a word cloud based on the frequency of words in the provided string.
- **`wordcloud.to_file()`**: Saves the generated word cloud image to a file.

### **Emoji (`import emoji`)**
Used for handling and converting emojis in text.
- **`emoji.emoji_count()`**: Counts the number of emojis present in a string.
- **`emoji.demojize()`**: Replaces emojis with their text-based descriptive names (e.g., 😄 becomes `:grinning_face_with_smiling_eyes:`).

---

## 4. Visualization & Utilities

### **Matplotlib (`import matplotlib.pyplot as plt`)**
A plotting library for creating static, animated, and interactive visualizations.
- **`plt.figure()`**: Creates a new figure for plotting.
- **`plt.subplot()`**: Adds multiple plots in a single figure.
- **`plt.pie()`**: Creates a pie chart.
- **`plt.bar()`**: Creates a bar chart.
- **`plt.title()`, `plt.ylabel()`**: Adds labels and titles to the charts.
- **`plt.savefig()`**: Saves the entire figure to an image file.
- **`plt.close()`**: Closes a figure window to free up memory.

### **Re (`import re`)**
The Regular Expression library for advanced pattern matching and string substitution.
- **`re.sub(pattern, replacement, string)`**: Searches for a pattern and replaces it with a specified string (used for cleaning hashtags, handles, and RT prefixes).

### **Random (`import random`)**
Used for generating random numbers and selecting random elements.
- **`random.choice()`**: Selects a random element from a non-empty sequence.

### **OS (`import os`)**
Provides a way to use operating system dependent functionality.
- **`os.chdir()`**: Changes the current working directory.
- **`os.path.dirname(os.path.abspath(__file__))`**: Finds the directory where the current script is located.
