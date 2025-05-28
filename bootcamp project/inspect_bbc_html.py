import requests
from bs4 import BeautifulSoup

def fetch_bbc_html():
    url = "https://www.bbc.com/news"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        )
    }
    response = requests.get(url, headers=headers) #Sends a GET request to the BBC News URL with the specified headers.
    response.raise_for_status() #Raises an exception if the HTTP request returned an unsuccessful status code.
    html = response.text #extracts the HTML content from the response as a string.

    soup = BeautifulSoup(html, "html.parser") 
    h3_tags = soup.find_all('h3') #finds all the <h3> tags in html.
    for h3 in h3_tags:
        print(f"Tag: {h3}, Class: {h3.get('class')}")

if __name__ == "__main__":
    fetch_bbc_html() #function to execute the above logic
