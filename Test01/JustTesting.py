import requests

response = requests.get('https://randomuser.me/api/?results=10')

data = response.json()


def greet(greeting, name):
    """returns a greeting

    Arguments:
        greeting {string} -- greeting name
        name {string} -- person name

    Returns:
        greeting -- returns greeting.
    """
    return f'{greeting} {name}'
