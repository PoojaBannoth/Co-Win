from django.shortcuts import render
import requests
# Create your views here.

url = 'https://api.covid19india.org/v4/min/data.min.json'
complete_data = requests.get(url)

def statewise(request, state_id):
    state_stats = complete_data[state_id]
    return(request,'',locals())


