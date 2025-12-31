from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from brain_engine import get_menu_response
import os

app = Flask(__name__)

# Dictionary to keep track of user steps (Memory)
user_sessions = {}

@app.route("/", methods=['GET'])
def home():
    return "Turning Point Bot is Live and Healthy!", 200

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    # Get details from Twilio request
    sender_id = request.values.get('From')
    incoming_msg = request.values.get('Body', '')
    
    # Process the message through our logic engine
    reply_text = get_menu_response(sender_id, incoming_msg, user_sessions)
    
    # Build Twilio TwiML response
    resp = MessagingResponse()
    resp.message(reply_text)
    
    return str(resp)

if __name__ == "__main__":
    # Get port from environment or default to 10000 for Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)