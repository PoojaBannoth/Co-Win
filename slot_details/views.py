from django.shortcuts import render
import requests
import json
# Create your views here.

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
                  AppleWebKit/537.36 (KHTML, like Gecko) \
                  Chrome/56.0.2924.76 Safari/537.36'}


def state_list(request):
    URL='https://cdn-api.co-vin.in/api/v2/admin/location/states'
    states = requests.get(url=URL)
    state_list=states.json()
    state_list=state_list['states']
    return render(request,'find_detail.html',locals())
