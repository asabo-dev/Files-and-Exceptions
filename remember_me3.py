# REFACTORING
import json

def greet_user():
    """Greet the user by name."""
    filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")

greet_user()