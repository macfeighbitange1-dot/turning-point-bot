from brain_engine import get_brain_response

def start_test():
    print("--- Agrovet Bot Local Test Mode ---")
    print("Type 'quit' to stop the test.\n")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['quit', 'exit', 'stop']:
            print("Test ended.")
            break
        
        # Get the reply from your knowledge base
        reply = get_brain_response(user_input)
        print(f"Bot: {reply}\n")

if __name__ == "__main__":
    start_test()