from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from brain_engine import get_menu_response
import os

app = Flask(__name__)

# Dictionary to keep track of user steps (Memory)
user_sessions = {}

@app.route("/", methods=['GET'])
def home():
    # This tells Python to look for the HTML file in the templates folder
    return render_template("index.html")

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    sender_id = request.values.get('From')
    incoming_msg = request.values.get('Body', '')
    
    reply_text = get_menu_response(sender_id, incoming_msg, user_sessions)
    
    resp = MessagingResponse()
    resp.message(reply_text)
    
    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
