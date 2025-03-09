import nltk
import random
from nltk.chat.util import Chat, reflections

# Download NLTK datasets if not already installed
nltk.download('punkt')

# Define pairs (patterns and responses) for chatbot
pairs = [
    (r"Hi|Hello|Hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]),
    (r"How are you?", ["I'm doing great, thank you!", "I'm good! How about you?"]),
    (r"What's your name?", ["I am a chatbot created to help you.", "You can call me Chatbot!"]),
    (r"Bye", ["Goodbye!", "Take care!"]),
    (r"(.*) your name (.*)", ["I am a chatbot, I don't have a name like humans do."]),
    (r"(.*) help (.*)", ["Sure, how can I assist you?", "I'm here to help! What do you need?"]),
    (r"(.*) (location|city|country) ?", ["I'm a virtual assistant, I don't have a physical location."]),
    (r"(.*) (time|day) ?", ["I don't know the exact time, but it's always a good time to chat!"]),
    (r"(.*) (weather|temperature) ?", ["I can't check the weather, but I hope it's sunny wherever you are!"]),
]

# Create a chatbot using the above patterns and reflections
chatbot = Chat(pairs, reflections)

# Function to interact with the chatbot
def chat():
    print("Chatbot: Hello! Ask me anything or type 'Bye' to end.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: Sorry, I didn't quite understand that.")

if __name__ == "__main__":
    chat()
