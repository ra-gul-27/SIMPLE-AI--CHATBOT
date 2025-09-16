import random
import nltk
import spacy
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")

import os
try:
    nlp = spacy.load("en_core_web_sm")
except:
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "see you", "good night", "take care"],
    "thanks": ["thanks", "thank you", "thx"],
    "about": ["who are you", "what are you", "tell me about yourself", "introduce yourself"]
}

responses = {
    "greeting": ["Hello! How can I help you?", "Hey there!", "Hi! What’s up?"],
    "goodbye": ["Goodbye! Take care.", "See you soon!", "Bye 👋"],
    "thanks": ["You're welcome!", "No problem!", "Anytime 😊"],
    "about": ["I’m a simple AI chatbot built using Python, NLTK, and spaCy."],
    "unknown": ["Sorry, I didn’t understand that.", "Could you rephrase?", "I'm not sure I got that."]
}
def preprocess(text):
    tokens = word_tokenize(text.lower())  # NLTK tokenization
    doc = nlp(" ".join(tokens))           # Pass tokens through spaCy
    lemmas = [token.lemma_ for token in doc]  # Lemmatization
    return lemmas

def get_intent(user_input):
    user_tokens = preprocess(user_input)
    for intent, patterns in intents.items():
        for pattern in patterns:
            pattern_tokens = preprocess(pattern)
            if set(pattern_tokens).issubset(user_tokens):  # Match words/lemmas
                return intent
    return "unknown"

def chatbot():
    print("🤖 Chatbot is ready! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Bot: Bye! 👋")
            break

        intent = get_intent(user_input)
        response = random.choice(responses[intent])
        print("Bot:", response)

if __name__ == "__main__":
    chatbot()
