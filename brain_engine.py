def get_menu_response(user_id, message, user_sessions):
    msg = message.strip().lower()
    
    # Initialize session if new user
    if user_id not in user_sessions:
        user_sessions[user_id] = "MAIN_MENU"
        return (
            "Welcome to Turning Point Agrovet! 🌱\n"
            "How can we help you today?\n\n"
            "1. Purchase Products 🛒\n"
            "2. Get Consultation 🩺\n"
            "3. M-Pesa Payment Help 💸\n"
            "4. Contact an Agent 📞\n\n"
            "Reply with a number (1, 2, 3, or 4)."
        )

    state = user_sessions[user_id]

    # --- MAIN MENU LOGIC ---
    if state == "MAIN_MENU":
        if msg == "1":
            user_sessions[user_id] = "PURCHASE"
            return "What would you like to buy?\n\n1. Fertilizers\n2. Seeds\n3. Animal Feed\n0. Back to Main Menu"
        elif msg == "2":
            user_sessions[user_id] = "CONSULT"
            return "Choose consultation type:\n\n1. Crop Management\n2. Livestock Health\n0. Back to Main Menu"
        elif msg == "3":
            return "To pay via M-Pesa:\n1. Go to Lipa na M-Pesa\n2. Select Paybill 174379\n3. Account: Your Name\n\nReply '0' for Main Menu."
        elif msg == "4":
            return "An agent will call you shortly at this number. Reply '0' for Main Menu."
        else:
            return "Please select a valid option (1-4) or '0' to restart."

    # --- PURCHASE MENU LOGIC ---
    elif state == "PURCHASE":
        if msg == "1":
            return "DAP Fertilizer (50kg) - KSH 2,500\nCAN Fertilizer (50kg) - KSH 1,800\n\nReply '0' for Main Menu."
        elif msg == "0":
            user_sessions[user_id] = "MAIN_MENU"
            return "Back to Main Menu. Choose an option: 1. Buy, 2. Consult, 3. Pay, 4. Agent."
        else:
            return "Selection not recognized. Reply '1' for Fertilizers or '0' for Main Menu."

    # --- CONSULTATION MENU LOGIC ---
    elif state == "CONSULT":
        if msg == "1":
            return "For crops, ensure soil testing is done. We offer testing at KSH 500. Reply '0' for Main Menu."
        elif msg == "0":
            user_sessions[user_id] = "MAIN_MENU"
            return "Back to Main Menu. Choose: 1. Buy, 2. Consult, 3. Pay, 4. Agent."
        
    # Reset trigger
    if msg in ["hi", "hello", "0", "menu"]:
        user_sessions[user_id] = "MAIN_MENU"
        return "Welcome back! Please select:\n1. Buy\n2. Consult\n3. Pay\n4. Agent"

    return "I'm sorry, I didn't get that. Reply '0' to see the menu."