# 1. Bring in the libraries we need
import os
import random
import requests
from dotenv import load_dotenv

# 2. Load .env and get the webhook link
load_dotenv()
webhook_url = os.getenv("GAME_WEBHOOK_URL")


# Function: pick a luck number from 1 to 10
def roll_luck():
    return random.randint(1, 10)


# 3. Make an empty list to hold the story history
story = []

# 4. Ask for the player's name
name = input("What is your name?\n> ")

# 5. Ask what they're best at, and keep asking until it's valid
strengths = ["brave", "smart", "sneaky"]
strength = input("\nWhat are you best at? brave, smart, or sneaky\n> ").lower()
while strength not in strengths:
    strength = input("That's not an option. Pick brave, smart, or sneaky.\n> ").lower()

# 6. Ask what kind of adventure they want, and add it to the history
first_message = input("\nWhat kind of adventure do you want?\n> ")
story.append({
    "speaker": "Player",
    "text": f"My name is {name} and I am {strength}. I want {first_message}."
})

# 7. Make a variable that says the game is running
game_running = True

# 8. While the game is running:
while game_running:
    # a. Turn the history into one long text
    transcript = ""
    for turn in story:
        transcript += f"{turn['speaker']}: {turn['text']}\n"

    # b. Send it to n8n and get the reply
    response = requests.post(webhook_url, json={"message": transcript})
    reply = response.text

    # c. Print the reply, and add it to the history
    print()
    print(reply)
    story.append({"speaker": "Narrator", "text": reply})

    # d. Ask the player what they do
    action = input("\n> ")

    # e. If they type "quit", stop the game
    if action.lower() == "quit":
        game_running = False
    # f. Otherwise, roll for luck and add their action to the history
    else:
        luck = roll_luck()
        print(f"🍀 Luck: {luck}")
        story.append({"speaker": "Player", "text": f"(Luck: {luck}) {action}"})

# 9. Say goodbye after the loop ends
print("\nThanks for playing!")