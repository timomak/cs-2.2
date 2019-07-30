# https://solomid-resources.s3.amazonaws.com/blitz/tft/data/champions.json
# https://solomid-resources.s3.amazonaws.com/blitz/tft/data/classes.json
# https://solomid-resources.s3.amazonaws.com/blitz/tft/data/items.json
# https://solomid-resources.s3.amazonaws.com/blitz/tft/data/origins.json
# https://solomid-resources.s3.amazonaws.com/blitz/tft/data/tierlist.json
# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

"""
Final Project: Team Fight Tactics (League of Legends) Team Picker

Goal: Get a team with as many possible class boosts.

    • Has to print out all the options for which characters to buy.
        • Has to color code late game champions.
    • Has to show which classes those heroes are in.

Stretch Challenges:
    • Multiple classes choices.
    • Round by round reccomendations.
"""

""" Class Struct
"demon": {
    "key": "demon",
    "name": "Demon",
    "description": "Attacks from Demons have a chance to burn all of an enemy's mana and deal that much true damage.",
    "accentChampionImage": "https://cdn.blitz.gg/blitz/centered/Aatrox_Splash_Centered_0.jpg",
    "bonuses": [
      {
        "needed": 2,
        "effect": "25% chance on hit to Mana Burn"
      },
      {
        "needed": 4,
        "effect": "50% chance on hit to Mana Burn"
      },
      {
        "needed": 6,
        "effect": "85% chance on hit to Mana Burn"
      }
    ]
}
"""

import json

def make_classes(filename):
    """
    Open JSON file and read the data for the Classes (and Origins).
    filename - the file name as a string.
    Runtime:
    """
    with open(filename) as json_file:
        data = json.load(json_file)
        for p in data['people']:
            print('Name: ' + p['name'])
            print('Website: ' + p['website'])
            print('From: ' + p['from'])
            print('')
