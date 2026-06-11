#program for the Rule-Based Chatbot
print("\U0001F916 ChatBot: Hello! Welcome to the ChatBot!")
print("\U0001F4A1 Type 'help' to see commands or 'bye' to exit.")

while True:
    user_input=input("\U0001F60A You: ").lower()

    #Exit condition
    if user_input=="bye":
        print("\U0001F916 ChatBot: Goodbye! Have a great day!")
        break

    #Greetings
    elif user_input in ["hi", "hello", "hey"]:
        print("\U0001F916 ChatBot: Hello! How can I assist you today?")
    
    #How are you
    elif user_input in ["how are you", "how are you doing"]:
        print("\U0001F916 ChatBot: I'm just a program, but I'm here to help you!")
    
    #Name
    elif user_input in ["what is your name", "who are you"]:
        print("\U0001F916 ChatBot: I'm a Rule-Based ChatBot created to assist you.")

    #Thanks
    elif user_input in ["thank you", "thanks"]:
        print("\U0001F916 ChatBot: You're welcome! If you have any more questions, feel free to ask.")
    
    #Creator
    elif user_input in ["who created you", "who is your creator"]:
        print("\U0001F916 ChatBot: I was created by a programmer using Python and simple if-else statements.")
    
    #Help command
    elif user_input=="help":
        print("\n \U0001F4CB Available Commands:")
        print("\U0001F449 hi/hello/hey")
        print("\U0001F449 how are you/how are you doing")
        print("\U0001F449 what is your name/who are you")
        print("\U0001F449 thank you/thanks")
        print("\U0001F449 who created you/who is your creator")
        print("\U0001F449 bye\n")

    #Unrecognized input
    else:
        print("\U0001F916 ChatBot: I'm sorry, I don't understand that. Please try again or type 'help' for commands.")
        print("\U0001F4A1 Type 'help' to see commands or 'bye' to exit.")

print("\U0001F534 ChatBot: Chat session ended.")
