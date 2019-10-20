import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def get_translation(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        confirmation = input(
            f"Did you mean {get_close_matches(w, data.keys())[0]} instead? [Y/n]: ").lower()
        if confirmation == "y":
            return data[get_close_matches(w, data.keys())[0]]
    else:
        return "The word is not in a dictionary."


word = input("Enter a word: ")

print(get_translation(word))
