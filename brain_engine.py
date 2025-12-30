import json
import csv
import os
from datetime import datetime
import re

# 1. Save Customer Data
def save_customer(phone, message):
    file_exists = os.path.isfile('customers.csv')
    name = extract_name(message) or "Unknown"
    location = extract_location(message) or "Unknown"
    
    with open('customers.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Phone', 'Name', 'Location', 'Last_Message', 'Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()
        
        writer.writerow({
            'Phone': phone,
            'Name': name,
            'Location': location,
            'Last_Message': message,
            'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

def extract_name(message):
    match = re.search(r"(?:I'm|I am|name is|jina ni|naitwa|naitwa)\s*([A-Za-z]+)", message, re.IGNORECASE)
    return match.group(1) if match else None

def extract_location(message):
    locations = ['nairobi', 'kirinyaga', 'nanyuki', 'nakuru', 'central', 'rift valley', 'kiambu', 'nyeri', 'laikipia', 'meru']
    msg_lower = message.lower()
    for loc in locations:
        if loc in msg_lower:
            return loc.capitalize()
    return None

# 2. Language Detection – Very Strong for Swahili/Sheng
def detect_language(text):
    swahili_sheng_triggers = ['sasa', 'niaje', 'uko', 'wapi', 'ngapi', 'bei', 'nataka', 'mbolea', 'maziwa', 'kuku', 'ngombe', 
                              'aki', 'wazi', 'duka', 'bei gani', 'ushauri', 'dalili', 'shida', 'rafiki', 'mko', 'gani', 'poa', 
                              'leo', 'bidhaa', 'aina', 'mnauza', 'mna', 'vipi', 'sema', 'bro', 'mbona', 'pole', 'asante',
                              'karibu', 'sawa', 'mzuri', 'mbaya', 'haraka']
    if any(word in text.lower() for word in swahili_sheng_triggers):
        return 'swahili'
    return 'english'

# 3. Main Brain Logic
def get_brain_response(user_input, phone):
    save_customer(phone, user_input)
    
    user_input_lower = user_input.lower()
    lang = detect_language(user_input_lower)
    
    with open('knowledge_base.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 0. Greetings
    greeting_keywords = ['niaje', 'sasa', 'mambo', 'hello', 'hi', 'habari', 'jambo', 'karibu', 'sema']
    if any(key in user_input_lower for key in greeting_keywords):
        return data['business_info']['greetings'][lang]

    # 1. Consultation / Farming Advice
    for advice in data['consultation']:
        if any(key in user_input_lower for key in advice['keywords']):
            return f"USHURI: {advice['response'][lang]}"

    # 2. FAQ (Hours, Payment)
    for item in data['faq']:
        if any(key in user_input_lower for key in item['keywords']):
            return item['response'][lang]

    # 3. Locations & Delivery
    if any(w in user_input_lower for w in ['location', 'where', 'wapi', 'mahali', 'place', 'duka', 'branches', 'iko wapi']):
        return data['business_info']['locations'][lang]
    
    if any(w in user_input_lower for w in ['deliver', 'delivery', 'kuleta', 'tuma', 'transport', 'sends']):
        return data['business_info']['delivery'][lang]

    # 4. Specific Product Inquiry
    for product in data['products']:
        if any(key in user_input_lower for key in product['keywords']):
            if lang == 'swahili':
                return f"Tuko na {product['name']} bei yake ni KES {product['price']}. Andika 'Buy' kama unataka kununua sasa hivi!"
            else:
                return f"We have {product['name']} at KES {product['price']}. Type 'Buy' to purchase via M-Pesa now!"

    # 5. General Product List Request
    if any(key in user_input_lower for key in data['general_keywords']['products_list']):
        product_list = [f"{p['name']} - KES {p['price']}" for p in data['products']]
        list_str = "\n".join(product_list)
        if lang == 'swahili':
            return f"Hii hapa orodha ya bidhaa zetu:\n\n{list_str}\n\nUliza bei au maelezo zaidi, au andika 'Buy [jina la bidhaa]' kununua."
        else:
            return f"Here are our available products:\n\n{list_str}\n\nAsk for details or type 'Buy [product name]' to purchase."

    # 6. Final Fallback – Friendly & Helpful
    if lang == 'swahili':
        return "Pole sana rafiki, sijaelewa vizuri 😅\nJaribu kuuliza kuhusu:\n• Mbolea au dawa\n• Ushauri wa kuku/ng'ombe/mahindi\n• Bei au delivery\n• Saa za kufungua\nNi nini haswa unahitaji?"
    else:
        return "Sorry, I didn't catch that clearly 😅\nYou can ask about:\n• Fertilizers or pesticides\n• Advice for chickens/cows/maize\n• Prices or delivery\n• Opening hours\nWhat exactly do you need?"