import os

def respond(string):
    # Convert string to lowercase and remove punctuation and replace spaces with %20
    string = string.lower().replace(" ", "%20")
    
    # Use API
    url = f"localhost:3000/chatbot/?input=\"{string}\""
    os.system(f"curl {url}")

if __name__ == '__main__':
    while True:
        # Get user input
        user_input = input("> ")
        respond(user_input)
        print("\n")
