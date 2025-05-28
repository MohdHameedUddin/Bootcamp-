"""
News Headlines Sentiment Analyzer (CLI Version)

This script scrapes news headlines from BBC News homepage,
performs sentiment analysis on each headline using TextBlob,
and displays the results in the command line.

Requirements:
- requests (pip install requests)
- beautifulsoup4 (pip install beautifulsoup4)
- textblob (pip install textblob)

Run this with:
python news_headlines_sentiment_cli.py
"""

import requests #For HTTP request
from bs4 import BeautifulSoup #For XML parsing
from textblob import TextBlob #For sentimental analysis

def scrape_bbc_headlines():
    """
    Scrapes the BBC News RSS feed for top news headlines.
    Returns a list of headline strings.
    """
    url = "http://feeds.bbci.co.uk/news/rss.xml"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        )
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "xml")
    items = soup.find_all('item')
    headlines = []

    for item in items:
        title = item.find('title').get_text(strip=True)
        if len(title) > 10:
            headlines.append(title)

    unique_headlines = list(dict.fromkeys(headlines))[:20]
    return unique_headlines

def analyze_sentiment(text):
    """
    Analyzes sentiment polarity of a text.
    Returns 'Positive', 'Negative' or 'Neutral' based on polarity.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

def main(): #Prints header messages
    print("📰 BBC News Headlines Sentiment Analyzer")
    print("Scraping latest headlines from BBC News...\n")

    try:
        headlines = scrape_bbc_headlines()
    except Exception as e:
        print(f"Error fetching headlines: {e}")
        return

    print(f"Found {len(headlines)} headlines:\n")

    for headline in headlines:
        sentiment = analyze_sentiment(headline)
        print(f"{sentiment}: {headline}")

if __name__ == "__main__":
    main() #Runs the main function if the scripts executed directly.
