import requests

def get_crypto_tickers():
    r = requests.get("https://api.alternative.me/v2/ticker/")
    return list(r.json()["data"].values())

def get_global_market_info():
    r = requests.get("https://api.alternative.me/v2/global")
    return r.json()["data"]

def get_fear_and_greed_index():
    r = requests.get("https://api.alternative.me/fng/?limit=7")
    return r.json()

def filter_biggest_marketcaps(tickers):
    return sorted(tickers, key=lambda x: x["quotes"]["USD"]["market_cap"], reverse=True)[:5]

def filter_by_percentage_change_24h(tickers, isReverse, numToDisplay):
    return sorted(tickers, key=lambda x: x["quotes"]["USD"]["percentage_change_24h"], reverse=isReverse)[:numToDisplay]

def filter_by_percentage_change_7d(tickers, isReverse, numToDisplay):
    return sorted(tickers, key=lambda x: x["quotes"]["USD"]["percentage_change_7d"], reverse=isReverse)[:numToDisplay]