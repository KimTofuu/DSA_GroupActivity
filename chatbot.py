import random

predefRespo = {
    "hello": [
        "Hello! How can I assist you today?",
        "Hi there! What can I do for you?",
        "Greetings! How may I help you today?"
    ],
    "hi": [
        "Hi! How can I help you?",
        "Hello! What would you like to know?",
        "Hey! How’s your day going so far?"
    ],
    "good morning": [
        "Good morning! How can I make your day better?",
        "Morning! Need any assistance?",
        "Good day! What can I do for you today?"
    ],
    "good afternoon": [
        "Good afternoon! How can I assist you?",
        "Hi there! Need any help this afternoon?",
        "Good afternoon! What can I help you with?"
    ],
    "good evening": [
        "Good evening! How may I assist you tonight?",
        "Evening! What can I help you with?",
        "Good evening! Is there something you need help with?"
    ],
    
    "goodbye": [
        "Goodbye! Have a great day!",
        "Take care! Feel free to reach out anytime.",
        "Goodbye! Hope to assist you again soon!"
    ],
    "bye": [
        "Bye! Take care!",
        "Goodbye! Looking forward to our next chat.",
        "See you later! Have a wonderful day."
    ],
    "see you later": [
        "See you later! Don’t hesitate to come back if you need anything.",
        "Catch you later! I’ll be here when you return.",
        "See you! Take care until next time!"
    ],
    
    "thank you": [
        "You're welcome! Always here to help.",
        "No problem at all! Glad I could assist.",
        "You're welcome! If you need anything else, just ask."
    ],
    "thanks": [
        "Anytime! Happy to help.",
        "You're welcome! Let me know if you need anything else.",
        "No worries! Glad to assist."
    ],
    "thanks a lot": [
        "You're very welcome! Feel free to ask if you need more help.",
        "No problem at all! It was my pleasure to help.",
        "Glad I could help! Reach out if you need anything else."
    ],

    "can you help me": [
        "Of course! What do you need help with?",
        "Definitely! How can I assist you today?",
        "Yes, I can! Please tell me what you need help with."
    ],
    "i need help": [
        "I'm here to assist. What do you need?",
        "No problem! What can I help you with?",
        "Sure! Let me know what you need assistance with."
    ],
    "i have a question": [
        "Feel free to ask! I'm here to answer any questions you have.",
        "Go ahead! I'm ready to answer your question.",
        "Ask away! I’ll do my best to provide the information you need."
    ],
    
    "what's your name": [
        "I'm your friendly chatbot, always here to assist!",
        "My name is Chatbot, and I’m here to help you.",
        "I'm your virtual assistant, ready to answer your questions."
    ],
    "who are you": [
        "I'm a chatbot designed to assist you with any questions or tasks.",
        "I'm your virtual assistant, here to help with whatever you need.",
        "I’m a chatbot, created to assist and provide information!"
    ],
    "what can you do": [
        "I can answer questions, provide information, and assist with various tasks. How can I help today?",
        "I can help you with questions, provide recommendations, and assist with tasks. What do you need?",
        "I’m capable of answering questions, giving info, and helping you with tasks. Let me know how I can assist!"
    ],

    "what are your office hours": [
        "Our office hours are Monday to Friday, 9 AM to 5 PM.",
        "We’re available from Monday to Friday, between 9 AM and 5 PM.",
        "You can reach us from 9 AM to 5 PM, Monday to Friday."
    ],
    "where are you located": [
        "We are located at [Insert Location]. Feel free to visit during office hours.",
        "You can find us at [Insert Location]. Drop by any time during office hours!",
        "We are located at [Insert Location], and we’re open for visits during office hours."
    ],

    "i don't understand": [
        "I'm sorry, I didn't quite catch that. Could you rephrase?",
        "Apologies, I didn’t understand that. Could you please say it another way?",
        "I’m not sure I understood. Could you clarify your question?"
    ],
    "can you repeat that": [
        "Sure! Could you clarify your question or ask it again?",
        "No problem! Can you ask your question again, please?",
        "I’d be happy to! Could you repeat that for me?"
    ],
    
    "how are you": [
        "I'm just a chatbot, but I'm here and ready to help!",
        "I don't have feelings, but I'm here to assist you!",
        "I’m doing great, thanks for asking! How can I assist you today?"
    ],
    "what is your purpose": [
        "My purpose is to assist you with any questions or tasks you have.",
        "I’m here to provide answers, assist with tasks, and make things easier for you.",
        "My goal is to help you with any queries or needs you have. How can I assist?"
    ],
    "tell me a joke": [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why did the bicycle fall over? It was two-tired!"
    ]
}

UnknRespo = [
    "I'm not sure I understand, can you please rephrase?",
    "Sorry, I don't have an answer for that. Can you try asking in another way?",
    "I'm not familiar with that. Could you ask something else?",
    "I’m not sure how to answer that yet. Maybe try another question?",
    "That’s a bit beyond my expertise! How about asking something else?"
]

def response(U_input):
    U_input = U_input.lower().strip()

    for q in predefRespo:
        if q in U_input:
            return random.choice(predefRespo[q])
    
    return random.choice(UnknRespo)

def chatRun():
    print("Hi! I'm your chatbot friend. Ask me a question.\n*Send bye to exita.")

    while True:
        userIn = input("\nUser: ")

        if 'bye' in userIn.lower():
            print('\nChatbot: Goodbye!')
            break

        chatRes = response(userIn)
        print(f'\nChatbot: {chatRes}')

chatRun()