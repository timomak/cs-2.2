# coding: utf-8
#!python
# graph_tft.py
# By Timofey Makhlay (github.com/timomak/cs-2.2)

import json

class Champion(object):

    def __init__(self, json):
        print(json)
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
            print(self.class2, self.class1)
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
    Runtime: O(n) * O(m) * O(5) (Number of champions * Number of classes * 5)
    """
    champions = []
    with open(filename) as json_file: # Open JSON File
        data = json.load(json_file) # Get the JSON
        for champ_obj in data.items(): # O(n) ('aatrox' : { **aatrox data** } )
            new_champ = Champion(champ_obj[1])
            champions.append(new_champ)

    print(champions)

if __name__ == '__main__':
    main('champions.json')
