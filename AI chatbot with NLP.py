#importing spacy
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# initializing tags from the user
tags= {
    "hello": "Hello! How can I help you?",
    "your name": "My name is ChatBot.",
    "weather": "It's sunny and clear today.",
    "joke": "Sure, here’s a joke for you!",
    "how are you": "I'm doing well, thank you!",
    "bye": "Goodbye! Have a great day!",
    "help": "I can help with basic questions."
}


# Generating  chatbot response using matching keyword
def generate_response(user_input):
    user_input = user_input.lower()
    for keyword in tags:
        if keyword in user_input:
            return tags[keyword]
    return "Sorry, I didn't understand that. Can you rephrase?"

# Chat loop
def chat() -> object:
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
