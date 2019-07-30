# https://boards.na.leagueoflegends.com/de/c/teamfight-tactics/pNEWFQMv-teamfight-tactics-developer-api

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

""" Champion Struct
  "Aatrox": {
    "id": "266",
    "key": "Aatrox",
    "name": "Aatrox",
    "origin": ["Demon"],
    "class": ["Blademaster"],
    "cost": 3,
    "ability": {
      "name": "The Darkin Blade",
      "description": "Aatrox cleaves the area in front of him, dealing damage to enemies inside it.",
      "type": "Active",
      "manaCost": 75,
      "manaStart": 0,
      "stats": [{ "type": "Damage", "value": "400 / 700 / 1000" }]
    },
    "stats": {
      "offense": {
        "damage": 65,
        "attackSpeed": 0.65,
        "dps": 42,
        "range": 1
      },
      "defense": {
        "health": 750,
        "armor": 25,
        "magicResist": 20
      }
    },
    "items": [
      "titanichydra",
      "phantomdancer",
      "dragonsclaw"
    ]
  }
"""

import json

def _classes_dict(filename):
    """
    Open JSON file and read the data for the Classes (and Origins).
    filename - the file name as a string.
    Runtime: O(n)
    """
    classes = [] # ['demon', 'assasin', ...] **NOT IN USE**
    dict = { 1: [], 2: [], 3: [], 4 : [], 6 : []} # { 1 : [ { 'robot' : ['blitzcrank'], 'exile' : ['yasuo'] } ], 2 : ... }
    with open(filename) as json_file:
        data = json.load(json_file)
        for class_obj in data.items(): # O(n)

            key = class_obj[1]['key'] # String
            name = class_obj[1]['name'] # String
            description = class_obj[1]['description'] # String
            accentChampionImage = class_obj[1]['accentChampionImage'] # URL as String
            bonuses = class_obj[1]['bonuses'] # Array [{'needed': int, 'effect': string}]
            needed = bonuses[-1]['needed'] # Check the highest number for needed. (In this case it's the last item in the array)

            dict[needed] += [{class_obj[0]: []}]
    return dict

def _champ_dict(dict, filename):
    # print(dict.items())
    with open(filename) as json_file:
        data = json.load(json_file)
        for champ_obj in data.items(): # O(n)
            # print(champ_obj)
            id = champ_obj[1]['id']
            key = champ_obj[1]['key'] # name
            name = champ_obj[1]['name']
            origin = champ_obj[1]['origin'] # [0].lower() # Origin as lower cap String
            origin2 = None # Not all Champs have 2 Origins
            class_ = champ_obj[1]['class'] # [0].lower() # Class as lower cap String
            class2 = None # Not all Champs have 2 Classes
            cost = champ_obj[1]['cost']
            ability = champ_obj[1]['ability']
            stats = champ_obj[1]['stats']
            items = champ_obj[1]['items']


            if len(origin) > 1:
                origin2 = origin[1].lower()
                origin = origin[0].lower()
            else:
                origin = origin[0].lower()

            if len(class_) > 1:
                class2 = class_[1].lower()
                class_ = class_[0].lower()
            else:
                class_ = class_[0].lower()

            print("Name: {}\nOrigin: {}, Origin 2: {}, Class: {}, Class 2: {}".format(name, origin, origin2, class_, class2))



_champ_dict(_classes_dict('classes.json'), 'champions.json')
