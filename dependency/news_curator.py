import requests
from bs4 import BeautifulSoup

def get_crypto_news():
    response = requests.get("https://finance.yahoo.com/topic/crypto/")
    return find_articles(response)

def find_articles(request):
    soup = BeautifulSoup(request.text, 'html.parser')
    headlines = soup.find("body").find_all("a", {"class": "js-content-viewer"})[:10]
    results = []
    for x in headlines:
        headline = x.get_text().strip(" \n")
        if headline.casefold() not in (result[0].casefold() for result in results):
            results.append([headline, "https://finance.yahoo.com/" + x["href"]])
    return results