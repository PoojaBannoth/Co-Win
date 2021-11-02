from django.shortcuts import render,redirect
import requests
from .models import Notified_list
import datetime
from .forms import *
from django.contrib import messages
from django.core.mail import send_mail

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
                  AppleWebKit/537.36 (KHTML, like Gecko) \
                  Chrome/56.0.2924.76 Safari/537.36'}


def user_subscription(request):
     if request.method == 'POST':
        form = Subscribe_User(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'You have now subscribed to notifications, you will be notified when slot is available')
            return redirect('stats')
     else:
        form = Subscribe_User()
     return render(request, 'form.html', locals())


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
                    send_mail(
                            'Vaccine available',
                            'The vaccine is available at your requested pincode. please come back and book',
                            'rakshithh176@gmail.com',
                            [pin.email.to_string],
                        )
