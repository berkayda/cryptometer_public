import requests
import datetime
from pycryptometer import Cryptometer
c = Cryptometer("YOURAPIKEY")


def single_ticker():
    print("Coin for Single Ticker (Exchange: Binance): ")
    coinName = input() + "USDT"
    singleTicker = c.infos.single_ticker("binance", coinName)
    # print("SINGLE TICKER: ")
    print("Market Pair: " + singleTicker[1]["market_pair"])
    print("Last: " + str(singleTicker[1]["last"]))
    print("High: " + str(singleTicker[1]["high"]))
    print("Low: " + str(singleTicker[1]["low"]))
    print("Volume (24h): " + str(singleTicker[1]["volume_24"]))
    print("Change % (24h): " + str(singleTicker[1]["change_24h"]))
    print("Change % (1h): " + str(singleTicker[1]["change_1h"]))
    print("Change % (7d): " + str(singleTicker[1]["change_7days"]))
    print("\n")


single_ticker()
