import requests
import datetime
from pycryptometer import Cryptometer
c = Cryptometer("YOURAPIKEY")


def ticker_list():
    print("Exchange for Ticker List: ")
    exchange = input()
    tickerL = c.infos.tickerlist(exchange)  # PARSE
    print("TICKER LIST: ")
    print("Exchange: " + exchange)
    print("\n")
    for item in tickerL:
        print(f"Market Pair: {item['market_pair']}")
        print(f"Last: {item['last']}")
        print(f"High: {item['high']}")
        print(f"Low: {item['low']}")
        print(f"Volume (24h): {item['volume_24']}")
        print(f"Change % (24h): {item['change_24h']}")
        print(f"Change % (1h): {item['change_1h']}")
        print(f"Change % (7d): {item['change_7days']}")
        print("-----------------------------------------")


ticker_list()
