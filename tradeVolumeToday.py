import requests
import datetime
from pycryptometer import Cryptometer
c = Cryptometer("YOURAPIKEY")


def trade_volume_today():
    print("Exchange: ")
    Exchange = input()
    print("Coin: ")
    coinName = input() + "USDT"
    tradeVolumeToday = c.volumes.today_trade_volume(Exchange, coinName)
    print("TODAY'S TRADE VOLUME: ")
    print("Buy: " + str(tradeVolumeToday["buy"]))
    print("Sell: " + str(tradeVolumeToday["sell"]))
    print("\n")


trade_volume_today()
