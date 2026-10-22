# 1. Bring in the libraries we need
import os
import requests
from dotenv import load_dotenv

# 2. Load the private settings from .env
load_dotenv()

# 3. Get the webhook link
webhook_url = os.getenv("GAME_WEBHOOK_URL")

# 4. Ask the player what they want to say
player_message = input("Say something to the Dungeon Master: ")

# 5. Send it to n8n
response = requests.post(webhook_url, json={"message": player_message})

# 6. Print the AI's reply
print(response.text)