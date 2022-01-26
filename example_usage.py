import requests, pyttsx3
engine = pyttsx3.init()

def respond(string):
    string = string.replace(" ", "%20")
    
    # Use API
    url = f"http://127.0.0.1:3000/chatbot/?input=\"{string}\""
    response = requests.get(url)
    output = response.text
    speak(output)
    return output

def speak(string):
    engine.say(string)
    engine.runAndWait()

if __name__ == '__main__':
    while True:
        # Get user input
        user_input = input("> ")
        print(respond(user_input))