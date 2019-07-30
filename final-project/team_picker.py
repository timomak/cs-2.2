# More info on these dicts in team_picker_setup.py
dict = {1: {'exile': {'yasuo'}, 'robot': {'blitzcrank'}}, 2: {'dragon': {'aurelionsol', 'shyvana'}, 'phantom': {'karthus', 'mordekaiser', 'kindred'}, 'guardian': {'braum', 'leona'}}, 3: {'pirate': {'pyke', 'graves', 'gangplank', 'twistedfate', 'missfortune'}, 'void': {'kassadin', 'chogath', 'reksai', 'khazix'}, 'elementalist': {'lissandra', 'anivia', 'brand', 'kennen'}, 'shapeshifter': {'gnar', 'nidalee', 'swain', 'shyvana', 'elise'}}, 4: {'imperial': {'katarina', 'draven', 'swain', 'darius'}, 'ninja': {'kennen', 'shen', 'zed', 'akali'}, 'wild': {'gnar', 'nidalee', 'warwick', 'rengar', 'ahri'}, 'brawler': {'chogath', 'warwick', 'blitzcrank', 'reksai', 'volibear'}, 'gunslinger': {'tristana', 'lucian', 'graves', 'gangplank', 'missfortune'}, 'ranger': {'vayne', 'varus', 'ashe', 'kindred'}}, 6: {'demon': {'aatrox', 'swain', 'brand', 'morgana', 'evelynn', 'varus', 'elise'}, 'glacial': {'anivia', 'lissandra', 'ashe', 'braum', 'sejuani', 'volibear'}, 'noble': {'kayle', 'lucian', 'leona', 'fiora', 'vayne', 'garen'}, 'yordle': {'gnar', 'tristana', 'poppy', 'veigar', 'lulu', 'kennen'}, 'assassin': {'katarina', 'zed', 'akali', 'rengar', 'evelynn', 'pyke', 'khazix'}, 'blademaster': {'yasuo', 'aatrox', 'gangplank', 'shen', 'fiora', 'draven'}, 'knight': {'kayle', 'poppy', 'darius', 'sejuani', 'mordekaiser', 'garen'}, 'sorcerer': {'morgana', 'aurelionsol', 'veigar', 'kassadin', 'ahri', 'lulu', 'karthus', 'twistedfate'}}}

champ_dict = {'aatrox': ['demon', 'blademaster'], 'ahri': ['wild', 'sorcerer'], 'akali': ['ninja', 'assassin'], 'anivia': ['glacial', 'elementalist'], 'ashe': ['glacial', 'ranger'], 'aurelionsol': ['dragon', 'sorcerer'], 'blitzcrank': ['robot', 'brawler'], 'brand': ['demon', 'elementalist'], 'braum': ['glacial', 'guardian'], 'chogath': ['void', 'brawler'], 'darius': ['imperial', 'knight'], 'draven': ['imperial', 'blademaster'], 'elise': ['demon', 'shapeshifter'], 'evelynn': ['demon', 'assassin'], 'fiora': ['noble', 'blademaster'], 'gangplank': ['pirate', 'gunslinger', 'blademaster'], 'garen': ['noble', 'knight'], 'gnar': ['wild', 'yordle', 'shapeshifter'], 'graves': ['pirate', 'gunslinger'], 'karthus': ['phantom', 'sorcerer'], 'kassadin': ['void', 'sorcerer'], 'katarina': ['imperial', 'assassin'], 'kayle': ['noble', 'knight'], 'kennen': ['ninja', 'yordle', 'elementalist'], 'khazix': ['void', 'assassin'], 'kindred': ['phantom', 'ranger'], 'leona': ['noble', 'guardian'], 'lissandra': ['glacial', 'elementalist'], 'lucian': ['noble', 'gunslinger'], 'lulu': ['yordle', 'sorcerer'], 'missfortune': ['pirate', 'gunslinger'], 'mordekaiser': ['phantom', 'knight'], 'morgana': ['demon', 'sorcerer'], 'nidalee': ['wild', 'shapeshifter'], 'poppy': ['yordle', 'knight'], 'pyke': ['pirate', 'assassin'], 'reksai': ['void', 'brawler'], 'rengar': ['wild', 'assassin'], 'sejuani': ['glacial', 'knight'], 'shen': ['ninja', 'blademaster'], 'shyvana': ['dragon', 'shapeshifter'], 'swain': ['imperial', 'demon', 'shapeshifter'], 'tristana': ['yordle', 'gunslinger'], 'twistedfate': ['pirate', 'sorcerer'], 'varus': ['demon', 'ranger'], 'vayne': ['noble', 'ranger'], 'veigar': ['yordle', 'sorcerer'], 'volibear': ['glacial', 'brawler'], 'warwick': ['wild', 'brawler'], 'yasuo': ['exile', 'blademaster'], 'zed': ['ninja', 'assassin']}

class_dict = {'demon': ['aatrox', 'brand', 'elise', 'evelynn', 'morgana', 'swain', 'varus'], 'dragon': ['aurelionsol', 'shyvana'], 'exile': ['yasuo'], 'glacial': ['anivia', 'ashe', 'braum', 'lissandra', 'sejuani', 'volibear'], 'imperial': ['darius', 'draven', 'katarina', 'swain'], 'noble': ['fiora', 'garen', 'kayle', 'leona', 'lucian', 'vayne'], 'ninja': ['akali', 'kennen', 'shen', 'zed'], 'pirate': ['gangplank', 'graves', 'missfortune', 'pyke', 'twistedfate'], 'phantom': ['karthus', 'kindred', 'mordekaiser'], 'robot': ['blitzcrank'], 'void': ['chogath', 'kassadin', 'khazix', 'reksai'], 'wild': ['ahri', 'gnar', 'nidalee', 'rengar', 'warwick'], 'yordle': ['gnar', 'kennen', 'lulu', 'poppy', 'tristana', 'veigar'], 'assassin': ['akali', 'evelynn', 'katarina', 'khazix', 'pyke', 'rengar', 'zed'], 'blademaster': ['aatrox', 'draven', 'fiora', 'gangplank', 'shen', 'yasuo'], 'brawler': ['blitzcrank', 'chogath', 'reksai', 'volibear', 'warwick'], 'elementalist': ['anivia', 'brand', 'kennen', 'lissandra'], 'guardian': ['braum', 'leona'], 'gunslinger': ['gangplank', 'graves', 'lucian', 'missfortune', 'tristana'], 'knight': ['darius', 'garen', 'kayle', 'mordekaiser', 'poppy', 'sejuani'], 'ranger': ['ashe', 'kindred', 'varus', 'vayne'], 'shapeshifter': ['elise', 'gnar', 'nidalee', 'shyvana', 'swain'], 'sorcerer': ['ahri', 'aurelionsol', 'karthus', 'kassadin', 'lulu', 'morgana', 'twistedfate', 'veigar']}

class_bonus_dict = {'demon': 6, 'dragon': 2, 'exile': 1, 'glacial': 6, 'imperial': 4, 'noble': 6, 'ninja': 4, 'pirate': 3, 'phantom': 2, 'robot': 1, 'void': 3, 'wild': 4, 'yordle': 6, 'assassin': 6, 'blademaster': 6, 'brawler': 4, 'elementalist': 3, 'guardian': 2, 'gunslinger': 4, 'knight': 6, 'ranger': 4, 'shapeshifter': 3, 'sorcerer': 6}

def help_me(first):
    """
    Given the first champion, output who I should build.
    Runtime:
    """
    # first = input("Name of your first chamption: ").lower()

    perfect_team = {}
    remaining_slots = 8

    # MARK: Figure out how many heroes you need of the current class.
    starter_classes = champ_dict[first] # List of classes for that hero O(1)

    for current_class in starter_classes: # O(3) worst case. Because no chamption has more than 3 classes.
        number_of_champs_for_bonus = class_bonus_dict[current_class] - 1
        perfect_team[current_class] = [first] # The first classes we're gonna have.

        # Pick a champ of the same class and add him to the team.
        for i in range(number_of_champs_for_bonus):
            perfect_team[current_class] += [class_dict[current_class][i]]

    print(perfect_team)




help_me('kennen')
