import json

data = json.load(open("data.json"))


def get_translation(w):
    """
    This function gets translation.
    """
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word is not in a dictionary."

word = input("Enter a word: ")

print(get_translation(word))
