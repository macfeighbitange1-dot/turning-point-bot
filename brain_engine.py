def get_menu_response(user_id, message, user_sessions):
    msg = message.strip().lower()
    
    # 1. GLOBAL COMMANDS (Always work)
    if msg in ["hi", "hello", "0", "menu", "habari"]:
        user_sessions[user_id] = "MAIN_MENU"
        return (
            "Welcome to *Turning Point Agrovet*! 🌱\n"
            "How can we help you today?\n\n"
            "1️⃣ Purchase Products 🛒\n"
            "2️⃣ Get Consultation 🩺\n"
            "3️⃣ M-Pesa Payment Help 💸\n"
            "4️⃣ Contact an Agent 📞\n\n"
            "Reply with **1, 2, 3, or 4**"
        )

    # 2. GET CURRENT STATE (Default to MAIN_MENU if unknown)
    state = user_sessions.get(user_id, "MAIN_MENU")

    # 3. MAIN MENU LOGIC
    if state == "MAIN_MENU":
        if msg == "1":
            user_sessions[user_id] = "PURCHASE"
            return ("*WHAT WOULD YOU LIKE TO BUY?*\n\n"
                    "1. Fertilizers\n"
                    "2. Seeds\n"
                    "3. Animal Feed\n"
                    "0. Back to Main Menu")
        elif msg == "2":
            user_sessions[user_id] = "CONSULT"
            return ("*CONSULTATION SERVICES*\n\n"
                    "1. Crop Management\n"
                    "2. Livestock Health\n"
                    "0. Back to Main Menu")
        elif msg == "3":
            return ("*M-PESA PAYMENT GUIDE*\n\n"
                    "1. Go to Lipa na M-Pesa\n"
                    "2. Paybill: **174379**\n"
                    "3. Account: Your Name\n\n"
                    "Reply **0** for Main Menu")
        elif msg == "4":
            return "An agent will call you shortly at this number. Reply **0** for Main Menu."

    # 4. PURCHASE MENU LOGIC
    elif state == "PURCHASE":
        if msg == "1":
            return ("*FERTILIZER PRICES:*\n"
                    "- DAP (50kg): KSH 2,500\n"
                    "- CAN (50kg): KSH 1,800\n\n"
                    "Reply **0** for Main Menu.")
        elif msg == "2":
            return ("*SEED PRICES:*\n"
                    "- Maize (2kg): KSH 600\n"
                    "- Beans (2kg): KSH 450\n\n"
                    "Reply **0** for Main Menu.")
        elif msg == "3":
            return "Dairy Meal (50kg): KSH 2,200. Reply **0** for Main Menu."

    # 5. CONSULTATION MENU LOGIC
    elif state == "CONSULT":
        if msg == "1":
            return "We offer soil testing at KSH 500. Visit us today! Reply **0** for Main Menu."
        elif msg == "2":
            return "Our vet is available Mon-Fri. Visit us for deworming services. Reply **0** for Main Menu."

    # 6. FALLBACK (If input doesn't match numbers)
    return "I didn't quite get that. Please reply with a **number** from the list or **0** to see the Main Menu."