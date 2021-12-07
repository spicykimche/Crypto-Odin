from dependency.alternativeme import get_crypto_tickers, get_global_market_info, get_fear_and_greed_index, filter_biggest_marketcaps, filter_by_percentage_change_24h, filter_by_percentage_change_7d
from dependency.news_curator import get_crypto_news
from util.formatter import print_disclaimer, print_state_of_the_crypto, print_crypto_news, print_tickers

if __name__ == "__main__":
    tickers = get_crypto_tickers()
    small_tickers = list(filter(lambda t: float(t["quotes"]["USD"]["market_cap"]) <= 500000000, tickers))
    market_info = get_global_market_info()
    fng = get_fear_and_greed_index()

    print_disclaimer()
    print_state_of_the_crypto(market_info, filter_biggest_marketcaps(tickers), fng)
    print_crypto_news(get_crypto_news())
    print_tickers("BIG CAPS", filter_biggest_marketcaps(tickers), "percentage_change_24h")
    print_tickers("WEEKLY MARKET MOVERS (ALL)", filter_by_percentage_change_7d(tickers, True, 5), "percentage_change_7d")
    print_tickers("WEEKLY MARKET LOSERS (ALL)", filter_by_percentage_change_7d(tickers, False, 5), "percentage_change_7d")
    print_tickers("DAILY MARKET MOVERS (ALL)", filter_by_percentage_change_24h(tickers, True, 5), "percentage_change_24h")
    print_tickers("DAILY MARKET LOSERS (ALL)",filter_by_percentage_change_24h(tickers, False, 5), "percentage_change_24h")
    print_tickers("SMALL CAPS (< 500mil)", filter_biggest_marketcaps(small_tickers), "percentage_change_24h")
    print_tickers("WEEKLY MARKET MOVERS (SMALL)", filter_by_percentage_change_7d(small_tickers, True, 5), "percentage_change_7d")
    print_tickers("WEEKLY MARKET LOSERS (SMALL)", filter_by_percentage_change_7d(small_tickers, False, 5), "percentage_change_7d")
    print_tickers("DAILY MARKET MOVERS (SMALL)", filter_by_percentage_change_24h(small_tickers, True, 5), "percentage_change_24h")
    print_tickers("DAILY MARKET LOSERS (SMALL)",filter_by_percentage_change_24h(small_tickers, False, 5), "percentage_change_24h")

