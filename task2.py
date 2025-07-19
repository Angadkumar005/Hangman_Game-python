# Enhanced Chatbot for Jupyter Notebook
import random
import datetime

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_date():
    today = datetime.datetime.now()
    return today.strftime("%A, %B %d, %Y")

def greet_user():
    greetings = ["Hello!", "Hi there!", "Hey!", "Nice to see you!", "Greetings!"]
    return random.choice(greetings)

def handle_input(user_input, name):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return greet_user()
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking!"
    elif "your name" in user_input:
        return "I'm your simple chatbot friend!"
    elif "time" in user_input:
        return f"The current time is {get_time()}."
    elif "date" in user_input:
        return f"Today is {get_date()}."
    elif "bye" in user_input:
        return "Goodbye! Have a great day! 👋"
    elif "my name is" in user_input:
        new_name = user_input.split("my name is")[-1].strip().capitalize()
        return f"Nice to meet you, {new_name}!"
    elif "thank" in user_input:
        return "You're welcome!"
    else:
        return "I'm not sure how to respond to that. Try asking about the time or date!"

def chatbot():
    print("🤖 ChatBot: Hello! What's your name?")
    name = input("You: ").strip().capitalize()

    print(f"🤖 ChatBot: Nice to meet you, {name}! Type something to chat (type 'bye' to exit).")

    while True:
        user_input = input(f"{name}: ").strip()
        response = handle_input(user_input, name)
        print(f"🤖 ChatBot: {response}")

        if "bye" in user_input.lower():
            break

# Run it
chatbot()
