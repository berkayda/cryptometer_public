import requests
import datetime
from pycryptometer import Cryptometer
c = Cryptometer("YOURAPIKEY")


def trend_indicator():
    global trend
    trend = c.indicators.trend()  # only this free in indicators
    # print("TREND: ")
    print("Trend Score: " + str(trend["trend_score"]))  # higher is better (bullish)
    print("Buy Pressure: " + str(trend["buy_pressure"]))
    print("Sell Pressure: " + str(trend["sell_pressure"]))
    print("\n")


trend_indicator()
