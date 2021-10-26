from django.shortcuts import render
import requests
# Create your views here.

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
                  AppleWebKit/537.36 (KHTML, like Gecko) \
                  Chrome/56.0.2924.76 Safari/537.36'}

def district_wise(request,dist_id,date):
    date=date.strftime("%d:%m:%Y")
    params={'district_id': dist_id,'date':date}
    url=f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?dist={dist_id}?date={date}'
    dist_details=requests.get(url,headers=header)
    dist_details = dist_details.json()
    hospital_name = dist_details["sessions"]["name"]
    fee_type = dist_details["sessions"]["fee_type"]
    available = dist_details["sessions"]["available_capacity"]
    
    return render(request,'',locals())

def pincode_wise(request,pin,date):
    
    params={'district_id': pin,'date':date}
    url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pin}?date={date}'
    pincode_details=requests.get(url,headers=header)
    pincode_details = pincode_details.json()
    district_name = pincode_details["sessions"]["district_name"]
    fee_type = pincode_details["sessions"]["fee_type"]
    available = pincode_details["sessions"]["available_capacity"]
    
    return render(request,'',locals())

def state_list(request):
    url='https://cdn-api.co-vin.in/api/v2/admin/location/states'
    states = request.get(url,headers=header)
    states = states.json()
    return render('find_detail.html',locals())