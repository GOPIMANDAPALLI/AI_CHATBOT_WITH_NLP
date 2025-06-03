# AI_CHATBOT_WITH_NLP

*COMPANY* : CODETECH IT SOLUTIONS

*NAME* : MANDAPALLI GOPI

*INTERN ID* : CT04DN1772

*DURATION* : 4-WEEKS

*MENTOR* : NEELA SANTOSH

*DESCRIPTION FOR USING SPACY FOR THE TASK* :

The given Python program is a simple keyword-based chatbot developed using the spaCy library, which is known for natural language processing (NLP) capabilities. Although spaCy is imported and a language model (en_core_web_sm) is loaded, in this particular implementation, spaCy isn’t directly used for text processing or NLP tasks. Instead, the chatbot uses a dictionary of predefined keywords (tags) and associated responses to interact with users in a conversational manner.

At the beginning of the program, the spacy module is imported and the small English language model (en_core_web_sm) is loaded using spacy.load(). This setup is typical in NLP applications, where models are used for tasks like named entity recognition, part-of-speech tagging, and dependency parsing. However, in this specific case, the loaded model isn’t actively utilized in the chatbot’s logic. It seems to be included for future enhancement or as a placeholder for extending NLP capabilities.

The core logic of the chatbot is driven by a dictionary named tags, which contains a set of keywords or phrases as keys and corresponding responses as values. These responses are simple and predefined, offering a way to simulate basic conversation. For example, if a user types a message containing the word “hello,” the bot responds with “Hello! How can I help you?” Similarly, keywords like “weather,” “your name,” or “joke” trigger responses relevant to those topics. If none of the keywords match the user’s input, the bot replies with a default message: “Sorry, I didn’t understand that. Can you rephrase?”

The generate_response() function is responsible for analyzing the user’s input. It first converts the input text to lowercase to ensure case-insensitive matching. Then, it loops through the keywords in the tags dictionary and checks if any of those keywords are present in the user’s input. If a match is found, the corresponding response is returned. If no keyword matches, the function returns a fallback response indicating that the chatbot did not understand the input.

The actual interaction between the user and the chatbot takes place in the chat() function. This function prints a welcome message and enters into an infinite loop where it continuously prompts the user for input. If the user types “exit,” the loop breaks and the chatbot terminates the conversation with a goodbye message. Otherwise, the user’s input is passed to the generate_response() function, and the returned response is printed to the screen.

Overall, this chatbot program serves as a basic introduction to building rule-based conversational agents in Python. While it lacks the complexity of AI-powered chatbots that use machine learning or deep learning, it is an effective way to demonstrate how simple keyword matching can be used to simulate dialogue. The inclusion of the spaCy model suggests potential for future development, such as using NLP techniques to enhance user input processing, improve intent recognition, or support more dynamic responses. For beginners, this code provides a clear foundation on which more advanced chatbot features can be built.



*OUTPUT VIDEO* :


*OUTPUT PHOTO* :









