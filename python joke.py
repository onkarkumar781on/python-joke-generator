import requests
import json

def get_random_joke():
    """
    Fetches a random joke from the Official Joke API.
    """
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            joke_data = response.json()
            print("\n" + "="*40)
            print("🤣 Here is your daily dose of humor! 🤣")
            print("="*40)
            print(f"👉 Setup:  {joke_data['setup']}")
            print(f"👉 Punchline: {joke_data['punchline']}")
            print("="*40 + "\n")
        else:
            print("❌ Oops! Couldn't fetch a joke right now.")
    except Exception as e:
        print(f"⚠️ Error connecting to the server: {e}")

if __name__ == "__main__":
    print("Welcome to the Ultimate Joke Generator! 🎭")
    get_random_joke()
