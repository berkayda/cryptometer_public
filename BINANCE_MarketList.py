import requests
import datetime
from pycryptometer import Cryptometer
c = Cryptometer("YOURAPIKEY")


def binance_market_list():
    binanceInfo = c.infos.market_list("binance")  # PARSE
    print("Binance MARKET LIST: ")
    print()
    for item in binanceInfo:
        print(f"Pair: {item['pair']}")
        print(f"Market Pair: {item['market_pair']}")
        print("-----------------------------------------")


binance_market_list()
