import time
import os
import random
import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from brain_engine import get_brain_response
from mpesa_handler import initiate_stk_push
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

def send_typing_indicator(channel_sid, member_sid):
    """Sends 'Typing...' via Twilio (Beta API as of 2025)"""
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    chat_service_sid = os.getenv('TWILIO_CHAT_SERVICE_SID')  # Add this to .env if needed
    url = f"https://chat.twilio.com/v3/Services/{chat_service_sid}/Channels/{channel_sid}/Members/{member_sid}/Typing"
    
    response = requests.post(url, auth=(account_sid, auth_token))
    if response.status_code != 204:
        print("Typing indicator failed; using delay fallback.")  # Log for debugging

@app.route("/whatsapp", methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '')
    sender_phone = request.values.get('From', '')  # whatsapp:+254...
    message_sid = request.values.get('MessageSid', '')
    channel_sid = request.values.get('ChannelSid', '')  # For typing indicator
    member_sid = request.values.get('MemberSid', '')    # For typing indicator
    clean_phone = sender_phone.replace('whatsapp:', '')
    
    # 1. Send 'Typing...' immediately
    send_typing_indicator(channel_sid, member_sid)
    
    # 2. Human-like randomized delay (1-4 seconds)
    time.sleep(random.uniform(1, 4))
    
    resp = MessagingResponse()
    
    if "buy" in incoming_msg.lower():
        stk_response = initiate_stk_push(clean_phone, 1)  # Test with KES 1
        if stk_response.get('ResponseCode') == "0":
            resp.message("Perfect! I've sent the STK push to your phone. Enter your M-Pesa PIN to complete.")
        else:
            resp.message(f"Oops, something went wrong: {stk_response['ResponseDescription']}. Try again or contact support.")
    else:
        reply_text = get_brain_response(incoming_msg, clean_phone)
        resp.message(reply_text)
        
    return str(resp)

if __name__ == "__main__":
    print("--- Turning Point Agrovet Bot v2.0 is Live ---")
    app.run(port=5000)