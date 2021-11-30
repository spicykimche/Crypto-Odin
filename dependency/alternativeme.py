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

def find_biggest_winners(tickers):
    return filter_by_percentage_change_24h(tickers, True, 5)

def find_biggest_losers(tickers):
    return filter_by_percentage_change_24h(tickers, False, 5)

def filter_by_percentage_change_24h(tickers, isReverse, numToDisplay):
    return sorted(tickers, key=lambda x: x["quotes"]["USD"]["percentage_change_24h"], reverse=isReverse)[:numToDisplay]
