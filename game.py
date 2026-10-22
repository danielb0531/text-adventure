# 1. Bring in the libraries we need
import os
import requests
from dotenv import load_dotenv

# 2. Load .env and get the webhook link
load_dotenv()
webhook_url = os.getenv("GAME_WEBHOOK_URL")

# 3. Make an empty list to hold the story history
story = []

# 4. Ask what kind of adventure they want, and add it to the history
first_message = input("What kind of adventure do you want? ")
story.append({"speaker": "Player", "text": first_message})

# 5. Make a variable that says the game is running
game_running = True

# 6. While the game is running:
while game_running:
    #    a. Turn the history into one long text
    transcript = ""
    for turn in story:
        transcript += f"{turn['speaker']}: {turn['text']}\n"

    #    b. Send it to n8n and get the reply
    response = requests.post(webhook_url, json={"message": transcript})
    reply = response.text

    #    c. Print the reply, and add it to the history
    print()
    print(reply)
    story.append({"speaker": "Dungeon Master", "text": reply})

    #    d. Ask the player what they do
    action = input("\n> ")

    #    e. If they type "quit", stop the game
    if action.lower() == "quit":
        game_running = False
    #    f. Otherwise, add their action to the history
    else:
        story.append({"speaker": "Player", "text": action})

# 7. Say goodbye after the loop ends
print("Thanks for playing!")