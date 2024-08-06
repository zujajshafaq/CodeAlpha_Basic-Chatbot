import nltk
from nltk.chat.util import Chat, reflections

# Sample patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am fine, thank you!', 'Doing well, how about you?']),
    (r'what is your name?', ['I am a chatbot created by you.', 'You can call me ChatBot.']),
    (r'how can you help me?', ['I can chat with you!', 'I can answer your questions to the best of my abilities.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'(.*)', ['Tell me more!', 'I see.', 'Interesting!', 'Can you elaborate on that?'])
]

# Reflections dictionary
reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'm"        : "you are",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
}

# Create Chat object
chat = Chat(patterns, reflections)

# Function to start the chatbot
def chatbot():
    print("Hi, I'm your chatbot. How can I help you today?")
    while True:
        user_input = input('> ')
        if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:
            print('Goodbye!')
            break
        response = chat.respond(user_input)
        print(response)

# Start the chatbot
chatbot()