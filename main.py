from dependency.alternativeme import get_crypto_tickers, get_global_market_info, get_fear_and_greed_index, filter_biggest_marketcaps, filter_by_percentage_change_24h, filter_by_percentage_change_7d
from util.formatter import print_disclaimer, state_of_the_crypto, print_tickers, print_market_overview

if __name__ == "__main__":
    tickers = get_crypto_tickers()
    market_info = get_global_market_info()
    fng = get_fear_and_greed_index()

    print_disclaimer()
    state_of_the_crypto(fng)
    print_market_overview(market_info)
    print_tickers("BIG MARKET CAPS", filter_biggest_marketcaps(tickers), "percentage_change_24h")
    print_tickers("WEEKLY MARKET MOVERS", filter_by_percentage_change_7d(tickers, True, 5), "percentage_change_7d")
    print_tickers("WEEKLY MARKET LOSERS", filter_by_percentage_change_7d(tickers, False, 5), "percentage_change_7d")
    print_tickers("DAILY MARKET MOVERS", filter_by_percentage_change_24h(tickers, True, 5), "percentage_change_24h")
    print_tickers("DAILY MARKET LOSERS",filter_by_percentage_change_24h(tickers, False, 5), "percentage_change_24h")
