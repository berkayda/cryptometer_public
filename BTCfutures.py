import requests
import datetime
from pycryptometer import Cryptometer
c = Cryptometer("YOURAPIKEY")


def BTC_futures():
    print("Exchange for BTC Futures: ")
    Exchange = input()
    btcFutures = c.infos.today_longs_shorts(Exchange, "BTC")  # PARSE
    print("TODAY'S LONG-SHORTS: ")
    print(btcFutures)
    print("\n")


BTC_futures()
