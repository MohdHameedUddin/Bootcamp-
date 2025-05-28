# News Headlines Sentiment Analyzer

This project contains two Python scripts related to scraping and analyzing news headlines from BBC News.

---

## Files

### 1. inspect_bbc_html.py

This script fetches the HTML content of the BBC News homepage and parses it to find all `<h3>` tags. It prints each `<h3>` tag along with its CSS class attribute. This can be useful for inspecting the structure of the BBC News webpage and identifying headline elements.

**Usage:**

```bash
python inspect_bbc_html.py
```

---

### 2. news_headlines_sentiment_cli.py

This script scrapes the latest news headlines from the BBC News RSS feed, performs sentiment analysis on each headline using the TextBlob library, and displays the sentiment (Positive, Negative, or Neutral) alongside each headline in the command line interface.

**Requirements:**

- requests
- beautifulsoup4
- textblob

Install dependencies with:

```bash
pip install requests beautifulsoup4 textblob
```

**Usage:**

```bash
python news_headlines_sentiment_cli.py
```

---

## How It Works

- `inspect_bbc_html.py` sends a GET request to the BBC News homepage, parses the HTML, and prints all `<h3>` tags and their classes.
- `news_headlines_sentiment_cli.py` fetches the BBC News RSS feed, extracts headlines, removes duplicates, analyzes sentiment polarity using TextBlob, and prints the results.

---

## Notes

- The scripts use a User-Agent header to mimic a browser request.
- Sentiment polarity thresholds are set to classify headlines as Positive (>0.1), Negative (<-0.1), or Neutral.

---

## License

This project is provided as-is for educational purposes.
