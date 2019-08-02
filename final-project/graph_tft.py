# coding: utf-8
#!python
# graph_tft.py
# By Timofey Makhlay (github.com/timomak/cs-2.2)

import json

class Champion(object):

    def __init__(self, json):
        """
        Creating champion object from JSON data.
        """
        self.id = json['id']
        self.key_ = json['key'].lower() # name
        self.name = json['name']
        self.origin1 = json['origin'] # Array of 2 at most
        self.origin2 = None # Not all Champs have 2 Origins
        self.class1 = json['class'] # Array of 2 at most
        self.class2 = None # Not all Champs have 2 Classes
        self.cost = json['cost']
        self.ability = json['ability']
        self.stats = json['stats']
        self.items = json['items']
        self.classes = []

        # Adjusting for characters with more than one class or origin attributes.
        if len(self.origin1) > 1:
            self.origin2 = self.origin1[1].lower()
            self.origin1 = self.origin1[0].lower()
            self.classes + [self.origin1, self.origin2]

        else:
            self.origin1 = self.origin1[0].lower()
            self.classes.append(self.origin1)

        if len(self.class1) > 1:
            self.class2 = self.class1[1].lower()
            self.class1 = self.class1[0].lower()
            self.classes + [self.class2, self.class1]

        else:
            self.class1 = self.class1[0].lower()
            self.classes.append(self.class1)



    def __repr__(self):
        """Return a string represenation of this Champion"""
        return 'Champion(key: {!r}, classes: {})'.format(self.key_, self.classes)


def main(filename):
    """
    Makes the world go round.
    Runtime: O(n)
    """
    champions = create_champ_obj(filename)
    print("Number of champs:",len(champions))



def create_champ_obj(filename):
    """
    Using the JSON file and the champions class, make a list containing all the champions.
    """
    champions = []
    with open(filename) as json_file: # Open JSON File
        data = json.load(json_file) # Get the JSON
        count = 0
        for champ_obj in data.items(): # O(n) ('aatrox' : { **aatrox data** } )
            new_champ = Champion(champ_obj[1])
            champions.append(new_champ)
            count += 1
    return champions

# def _classes_dict(filename):
#     """
#     Open JSON file and read the data for the Classes (and Origins).
#     filename - the file name as a string.
#     Runtime: O(n)
#     """
#     class_dict = {} # {'robot': ['blitzcrank']}
#     class_bonus_dict = {}
#     dict = { 1: {}, 2: {}, 3: {}, 4 : {}, 6 : {}} # { 1 : { 'robot' : set['blitzcrank'], 'exile' : set['yasuo'] }, 2 : ... }
#     with open(filename) as json_file:
#         data = json.load(json_file)
#         for class_obj in data.items(): # O(n)
#
#             key = class_obj[1]['key'] # String
#             name = class_obj[1]['name'] # String
#             description = class_obj[1]['description'] # String
#             accentChampionImage = class_obj[1]['accentChampionImage'] # URL as String
#             bonuses = class_obj[1]['bonuses'] # Array [{'needed': int, 'effect': string}]
#             needed = bonuses[-1]['needed'] # Check the highest number for needed. (In this case it's the last item in the array)
#
#             class_dict[key] = []
#             class_bonus_dict[key] = needed
#             dict[needed].update({class_obj[0]: []})
#
#     return dict

if __name__ == '__main__':
    main('champions.json')
