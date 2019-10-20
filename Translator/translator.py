import json
from difflib import get_close_matches
from sys import argv
data = json.load(open("data.json"))


def print_nicely(w):
    counter = 0
    for i in data[w]:
        counter += 1
        print(str(f"{counter}:"), i)
    return ""


def get_translation(w):
    w = w.lower()
    if w in data:
        print_nicely(w)
    elif len(get_close_matches(w, data.keys())) > 0:
        confirmation = input(
            f"Did you mean {get_close_matches(w, data.keys())[0]} instead? [Y/n]: ").lower()
        if confirmation == "y":
            result = data[get_close_matches(w, data.keys())[0]]
            counter = 0
            print(f"   {get_close_matches(w, data.keys())[0].capitalize()}")
            for i in result:
                counter += 1
                print(str(f"{counter}:"), i)
        else:
            return "The word is not in a dictionary."
    else:
        return "The word is not in a dictionary."
    return ""


word = argv[1]

print(get_translation(word))
