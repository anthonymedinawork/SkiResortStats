import requests, json
from bs4 import BeautifulSoup

from . import resort

RESORT_NAME = "Winter Park"
COUNTRY = "USA"
REGION = "Colorado"
PASSES = "Ikon"


def GetData():

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    resort_num = 5
    url = "https://mtnpowder.com/feed?resortId={num}".format(num=resort_num)

    json_resp = json.loads(requests.get(url).content)

    snow_report = json_resp["SnowReport"]
    lifts_open = snow_report["TotalOpenLifts"]
    lifts_total = snow_report["TotalLifts"]
    trails_open = snow_report["TotalOpenTrails"]
    trails_total = snow_report["TotalTrails"]

    snow_stats = snow_report["BaseArea"]
    snow_overnight = snow_stats["SinceLiftsClosedIn"]
    snow_24hrs = snow_stats["Last24HoursIn"]
    snow_48hrs = snow_stats["Last48HoursIn"]
    snow_72hrs = snow_stats["Last72HoursIn"]
    snow_7days = snow_stats["Last7DaysIn"]
    snow_30days = None
    snow_total = snow_report["SeasonTotalIn"]
    snow_base_depth = snow_stats["BaseIn"]
    return resort.ResortActiveRecord(RESORT_NAME, snow_overnight, snow_24hrs,
                                     snow_48hrs, snow_72hrs, None, None,
                                     snow_total, snow_base_depth, lifts_open, lifts_total,
                                     trails_open, trails_total, COUNTRY,
                                     REGION, PASSES)
