from django.shortcuts import render

def sendOTP(request,phone_num):
    params = {"mobile":phone_num.to_string}
    url = 'https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP'
    txn_id = request.post(url,params)


def confirm_otp(request,otp):
    url = 'https://cdn-api.co-vin.in/api/v2/auth/public/confirmOTP'
    

    

