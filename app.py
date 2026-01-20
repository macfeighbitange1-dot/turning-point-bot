from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from brain_engine import get_menu_response
import os

app = Flask(__name__)

# Dictionary to keep track of user steps (Memory)
user_sessions = {}

@app.route("/", methods=['GET'])
def home():
    # Your specific product data integrated here
    product_data = {
        "products": [
            {"id": 1, "name": "DAP Fertilizer 50kg", "price": "3,500"},
            {"id": 2, "name": "Cattle Dip 1L", "price": "1,200"},
            {"id": 3, "name": "Hybrid Maize Seeds 2kg", "price": "800"}
        ]
    }
    # Passing the list of products to index.html
    return render_template("index.html", products=product_data["products"])

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    # Get details from Twilio request
    sender_id = request.values.get('From')
    incoming_msg = request.values.get('Body', '')
    
    # Process the message through your logic engine
    reply_text = get_menu_response(sender_id, incoming_msg, user_sessions)
    
    # Build Twilio TwiML response
    resp = MessagingResponse()
    resp.message(reply_text)
    
    return str(resp)

if __name__ == "__main__":
    # Get port from environment or default to 10000 for Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
