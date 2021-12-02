import requests
from bs4 import BeautifulSoup

def get_bitcoin_news():
    response = requests.get("https://cryptonews.com/news/bitcoin-news")
    return find_articles(response)

def get_eth_news():
    response = requests.get("https://cryptonews.com/news/ethereum-news")
    return find_articles(response)

def get_alt_news():
    response = requests.get("https://cryptonews.com/news/altcoin-news")
    return find_articles(response)

def find_articles(request):
    soup = BeautifulSoup(request.text, 'html.parser')
    headlines = soup.find("body").find_all("a", {"class": "article__title"})[:5]
    results = []
    for x in headlines:
        headline = x.get_text().strip(" \n")
        if headline.casefold() not in (result[0].casefold() for result in results):
            results.append([headline, "https://cryptonews.com" + x["href"]])
    return results