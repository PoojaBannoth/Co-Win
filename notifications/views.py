from django.shortcuts import render
import requests
from .models import Notified_list
import datetime

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
                  AppleWebKit/537.36 (KHTML, like Gecko) \
                  Chrome/56.0.2924.76 Safari/537.36'}

def search_availability():

    #RUN ACCORDING TO API rate limit
    for pin in Notified_list:
        url=f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pin.pincode}'
        result = requests.get(url, headers=header)
        response_json = result.json()
        data = response_json["centers"]
        a = []
        for each in data:
            for every in each["sessions"]:
                if (every["available_capacity"] > 0) and (every["min_age_limit"] == 18):
                    a.append(each["name"])
                    a.append(each["pincode"])
                    a.append(every["vaccine"])
                    a.append(every["available_capacity"])
                    day = datetime.datetime.now()
                    # send mail to pin.email with details
