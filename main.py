from dependency.alternativeme import get_crypto_tickers, get_global_market_info, get_fear_and_greed_index, find_biggest_losers, find_biggest_winners
from util.formatter import state_of_the_crypto, market_movers, market_losers

if __name__ == "__main__":
    tickers = get_crypto_tickers()
    market_info = get_global_market_info()
    fng = get_fear_and_greed_index()

    state_of_the_crypto(market_info, fng)
    market_movers(find_biggest_winners(tickers))
    market_losers(find_biggest_losers(tickers))
