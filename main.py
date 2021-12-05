from dependency.alternativeme import get_crypto_tickers, get_global_market_info, get_fear_and_greed_index, filter_biggest_marketcaps, filter_by_percentage_change_24h, filter_by_percentage_change_7d
from dependency.news_curator import get_crypto_news
from util.formatter import print_disclaimer, print_state_of_the_crypto, print_crypto_news, print_tickers, print_market_dominance

if __name__ == "__main__":
    tickers = get_crypto_tickers()
    market_info = get_global_market_info()
    fng = get_fear_and_greed_index()

    print_disclaimer()
    print_state_of_the_crypto(market_info, fng)
    print_market_dominance(filter_biggest_marketcaps(tickers), market_info)
    print_crypto_news(get_crypto_news())
    print_tickers("BIG MARKET CAPS", filter_biggest_marketcaps(tickers), "percentage_change_24h")
    print_tickers("WEEKLY MARKET MOVERS", filter_by_percentage_change_7d(tickers, True, 5), "percentage_change_7d")
    print_tickers("WEEKLY MARKET LOSERS", filter_by_percentage_change_7d(tickers, False, 5), "percentage_change_7d")
    print_tickers("DAILY MARKET MOVERS", filter_by_percentage_change_24h(tickers, True, 5), "percentage_change_24h")
    print_tickers("DAILY MARKET LOSERS",filter_by_percentage_change_24h(tickers, False, 5), "percentage_change_24h")


