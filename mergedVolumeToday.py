import requests
import datetime
from pycryptometer import Cryptometer
c = Cryptometer("YOURAPIKEY")


def merged_volume_today():
    print("Coin for Today's Merged Volume: ")
    coinName = input()
    mergedVolumeToday = c.volumes.today_merged_volume(coinName)
    print(f"{coinName.upper()}" + " TODAY'S MERGED VOLUME: ")
    print("Buy: " + str(mergedVolumeToday["buy"]))
    print("Sell: " + str(mergedVolumeToday["sell"]))
    print("\n")


merged_volume_today()
