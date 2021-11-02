from django.shortcuts import render
import requests
# Create your views here.

url = 'https://api.covid19india.org/v4/min/data.min.json'
complete_data = requests.get(url)

def statewise(request):
    URL='https://cdn-api.co-vin.in/api/v2/admin/location/states'
    states = requests.get(url=URL)
    state_list=states.json()
    state_list=state_list['states']
    url = 'https://api.covid19india.org/v4/min/data.min.json'
    complete_data = requests.get(url=url)
    complete_data = complete_data.json()
    z={}
    state_names=[]
    for x in state_list:
        state_names.append(x['state_name'])
    for (i,j) in zip(list(complete_data.keys()), state_names): 
        z[i]=j
    return render(request,'dashboard.html',locals())


