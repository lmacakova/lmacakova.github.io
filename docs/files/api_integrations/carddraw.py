import requests
import json

card_api_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(card_api_url) 
deck = response.json() #asking for deck
deck_id = deck['deck_id']
print(deck) # printing deck
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(draw_url) # asking for draw
cards = response.json()['cards'] 
print("Your 5 cards:")
values = []
suits = []
for card in cards:
    value = card['value']
    suit = card['suit']
    print(f"{value} {suit}") # printing cards