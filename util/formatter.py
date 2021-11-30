from datetime import datetime

def state_of_the_crypto(market_info, fear_and_greed):
    current_date = datetime.utcnow().strftime("%Y-%m-%d")
    timezone = "UTC"
    fng_current = int(fear_and_greed["data"][0]["value"])
    fng_avg = calculate_fng_avg(fear_and_greed["data"])

    print("#STATE OF THE CRYPTO\n")
    
    print("As of **{} {}**, the Crypto market is in a state of **{}** (**{:.2f}**) (value sourced from: **{}**).".format(current_date, timezone, get_fear_and_greed_index(fng_current), fng_current, fear_and_greed["name"]), end=" ")
    print("This means that the overall momentum of the Crypto market is currently **{}**.\n".format(get_market_momentum(fng_current)))
    
    print("In the past week, the Crypto market was in an average state of **{}** (**{:.2f}**).".format(get_fear_and_greed_index(fng_avg), fng_avg), end=" ")
    print("This indicates that the Crypto market a week ago was in a **{}** sentiment. {}\n".format(get_market_momentum(fng_avg), get_future_expectation(fng_avg, fng_current)))
    
    print("##MARKET OVERVIEW\n")
    
    print("- Active CryptoCurrencies: **{:,}**".format(market_info["active_cryptocurrencies"]))
    print("- Bitcoin Market Percentage: **{:.2f}%**".format(float(market_info["bitcoin_percentage_of_market_cap"])*100))
    print("- Total Market Cap: **${:,.2f} USD**".format(market_info["quotes"]["USD"]["total_market_cap"]))
    print("- Total Market Volume 24h: **{:,}**\n".format(market_info["quotes"]["USD"]["total_volume_24h"]))

def get_fear_and_greed_index(value):
    if value < 25:
        return "Extreme Fear"
    elif value < 50:
        return "Fear"
    elif value == 50:
        return "Neutral"
    elif value > 75:
        return "Extreme Greed"
    elif value > 50:
        return "Greed"
    return "Sugma"

def get_market_momentum(value):
    if value < 50:
        return "Bearish"
    elif value == 50:
        return "Neutral"
    elif value > 50:
        return "Bullish"

def get_future_expectation(past, current):
    message = "We may face some **{}** in the coming days for the overall Crypto market if this current trajectory holds. The **{}** in the fear and greed index is a good indicator."
    status = None
    shift = None
    if past < current:
        status = "healthy gains"
        shift = "change"
    elif past > current:
        status = "dumpiness"
        shift = "change"
    else:
        status = "sideway movements"
        shift = "steadiness"
    return message.format(status, shift)

def calculate_fng_avg(values):
    avg = 0
    for x in values:
        avg += int(x["value"])
    return avg / len(values)

def market_movers(tickers):
    print("#MARKET MOVERS\n")
    index = 1
    for x in tickers:
        format_ticker(index, x)
        index+=1
    print("")

def market_losers(tickers):
    print("#MARKET LOSERS\n")
    index = 1
    for x in tickers:
        format_ticker(index, x)
        index+=1
    print("")

def format_ticker(index, x):
    percentage_movement = get_percentage_movement(x["quotes"]["USD"]["percentage_change_24h"])
    print("{}. **{}** (**{}**) - **${}** (**{}**)".format(index, x["name"], x["symbol"], get_price(x["quotes"]["USD"]["price"]), percentage_movement))
    print("   - Market Cap: **${:,.2f} USD**".format(x["quotes"]["USD"]["market_cap"]))
    print("   - Volume 24h: **{:,}**".format(x["quotes"]["USD"]["volume_24h"]))
    print("   - Circulating Supply: **{:,}**".format(x["circulating_supply"]))
    print("   - Total Supply: **{:,}**".format(x["total_supply"]))
    print("   - Max Supply: **{:,}**".format(x["max_supply"]))

def get_price(price):
    value = max('{:,.2f}'.format(price),'{:,.6f}'.format(price),key=len)
    value = value.rstrip("0")
    if len(value.rsplit('.')[-1]) == 2:
        value = '{:,.2f}'.format(float(value))
    return value

def get_percentage_movement(percentage):
    if int(percentage) > 0:
        return "+{:.2f}%".format(percentage)
    
    return "{:.2f}%".format(percentage)