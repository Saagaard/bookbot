def get_word_count(content):
    count = content.split()
    return len(count)

def get_character_count(content):
    characters = {}
    for character in content:
        if character in characters:
            characters[character] = characters[character] + 1
        else:
            characters[character] = 1
    return characters

def sort_on(items):
    return items["num"]

def sort_dictionary(character_counts):
    characters = []  
    for character in character_counts:
        dict = {"char": character, "num": character_counts[character]} 
        characters.append(dict)
    characters.sort(reverse=True, key=sort_on)
    return characters

def print_sorted_dictionary(dictionaries):
    for dictionary in dictionaries:
        char = dictionary["char"]
        num = dictionary["num"]
        print(f"{char}: {num} ")
