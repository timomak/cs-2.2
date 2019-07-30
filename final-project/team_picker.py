# More info on this dict in team_picker_setup.py
dict = {1: {'exile': {'yasuo'}, 'robot': {'blitzcrank'}}, 2: {'dragon': {'aurelionsol', 'shyvana'}, 'phantom': {'karthus', 'mordekaiser', 'kindred'}, 'guardian': {'braum', 'leona'}}, 3: {'pirate': {'pyke', 'graves', 'gangplank', 'twistedfate', 'missfortune'}, 'void': {'kassadin', 'chogath', 'reksai', 'khazix'}, 'elementalist': {'lissandra', 'anivia', 'brand', 'kennen'}, 'shapeshifter': {'gnar', 'nidalee', 'swain', 'shyvana', 'elise'}}, 4: {'imperial': {'katarina', 'draven', 'swain', 'darius'}, 'ninja': {'kennen', 'shen', 'zed', 'akali'}, 'wild': {'gnar', 'nidalee', 'warwick', 'rengar', 'ahri'}, 'brawler': {'chogath', 'warwick', 'blitzcrank', 'reksai', 'volibear'}, 'gunslinger': {'tristana', 'lucian', 'graves', 'gangplank', 'missfortune'}, 'ranger': {'vayne', 'varus', 'ashe', 'kindred'}}, 6: {'demon': {'aatrox', 'swain', 'brand', 'morgana', 'evelynn', 'varus', 'elise'}, 'glacial': {'anivia', 'lissandra', 'ashe', 'braum', 'sejuani', 'volibear'}, 'noble': {'kayle', 'lucian', 'leona', 'fiora', 'vayne', 'garen'}, 'yordle': {'gnar', 'tristana', 'poppy', 'veigar', 'lulu', 'kennen'}, 'assassin': {'katarina', 'zed', 'akali', 'rengar', 'evelynn', 'pyke', 'khazix'}, 'blademaster': {'yasuo', 'aatrox', 'gangplank', 'shen', 'fiora', 'draven'}, 'knight': {'kayle', 'poppy', 'darius', 'sejuani', 'mordekaiser', 'garen'}, 'sorcerer': {'morgana', 'aurelionsol', 'veigar', 'kassadin', 'ahri', 'lulu', 'karthus', 'twistedfate'}}}

champ_dict = {'aatrox': ['demon', 'blademaster'], 'ahri': ['wild', 'sorcerer'], 'akali': ['ninja', 'assassin'], 'anivia': ['glacial', 'elementalist'], 'ashe': ['glacial', 'ranger'], 'aurelionsol': ['dragon', 'sorcerer'], 'blitzcrank': ['robot', 'brawler'], 'brand': ['demon', 'elementalist'], 'braum': ['glacial', 'guardian'], 'chogath': ['void', 'brawler'], 'darius': ['imperial', 'knight'], 'draven': ['imperial', 'blademaster'], 'elise': ['demon', 'shapeshifter'], 'evelynn': ['demon', 'assassin'], 'fiora': ['noble', 'blademaster'], 'gangplank': ['pirate', 'gunslinger', 'blademaster'], 'garen': ['noble', 'knight'], 'gnar': ['wild', 'yordle', 'shapeshifter'], 'graves': ['pirate', 'gunslinger'], 'karthus': ['phantom', 'sorcerer'], 'kassadin': ['void', 'sorcerer'], 'katarina': ['imperial', 'assassin'], 'kayle': ['noble', 'knight'], 'kennen': ['ninja', 'yordle', 'elementalist'], 'khazix': ['void', 'assassin'], 'kindred': ['phantom', 'ranger'], 'leona': ['noble', 'guardian'], 'lissandra': ['glacial', 'elementalist'], 'lucian': ['noble', 'gunslinger'], 'lulu': ['yordle', 'sorcerer'], 'missfortune': ['pirate', 'gunslinger'], 'mordekaiser': ['phantom', 'knight'], 'morgana': ['demon', 'sorcerer'], 'nidalee': ['wild', 'shapeshifter'], 'poppy': ['yordle', 'knight'], 'pyke': ['pirate', 'assassin'], 'reksai': ['void', 'brawler'], 'rengar': ['wild', 'assassin'], 'sejuani': ['glacial', 'knight'], 'shen': ['ninja', 'blademaster'], 'shyvana': ['dragon', 'shapeshifter'], 'swain': ['imperial', 'demon', 'shapeshifter'], 'tristana': ['yordle', 'gunslinger'], 'twistedfate': ['pirate', 'sorcerer'], 'varus': ['demon', 'ranger'], 'vayne': ['noble', 'ranger'], 'veigar': ['yordle', 'sorcerer'], 'volibear': ['glacial', 'brawler'], 'warwick': ['wild', 'brawler'], 'yasuo': ['exile', 'blademaster'], 'zed': ['ninja', 'assassin']}

def help_me(first):
    """
    Given the first champion, output who I should build.
    Runtime:
    """
    # first = input("Name of your first chamption: ").lower()

    starter_classes = champ_dict[first] # List of classes for that hero O(1)





help_me('kennen')
