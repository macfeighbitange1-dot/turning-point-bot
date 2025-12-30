from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from brain_engine import get_menu_response
import os

app = Flask(__name__)

# This dictionary stores what menu each user is currently looking at
# Note: In a professional app, you'd use a Database or Redis here.
user_sessions = {}

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    # Get user phone number and their message
    sender_id = request.values.get('From')
    incoming_msg = request.values.get('Body', '').lower()
    
    # Get the structured response from the brain
    bot_message = get_menu_response(sender_id, incoming_msg, user_sessions)
    
    # Create the Twilio Response
    resp = MessagingResponse()
    resp.message(bot_message)
    
    return str(resp)

if __name__ == "__main__":
    # Render uses the PORT environment variable
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)