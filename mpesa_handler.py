import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64
import os
from dotenv import load_dotenv

load_dotenv()

def initiate_stk_push(phone_number, amount):
    consumer_key = os.getenv('MPESA_CONSUMER_KEY')
    consumer_secret = os.getenv('MPESA_CONSUMER_SECRET')
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    try:
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        r.raise_for_status()
        access_token = r.json()['access_token']
    except Exception as e:
        return {"ResponseCode": "1", "ResponseDescription": f"Authentication failed: {str(e)}"}

    process_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {access_token}"}
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    shortcode = os.getenv('MPESA_SHORTCODE')
    passkey = os.getenv('MPESA_PASSKEY')
    password = base64.b64encode((shortcode + passkey + timestamp).encode()).decode('utf-8')
    
    if phone_number.startswith('0'): phone_number = '254' + phone_number[1:]
    elif phone_number.startswith('+'): phone_number = phone_number.replace('+', '')

    payload = {
        "BusinessShortCode": shortcode,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": shortcode,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://your-ngrok-url.com/callback",  # Update with real callback
        "AccountReference": "TurningPointAgrovet",
        "TransactionDesc": "Agrovet Purchase"
    }
    
    try:
        response = requests.post(process_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"ResponseCode": "1", "ResponseDescription": f"STK push failed: {str(e)}"}