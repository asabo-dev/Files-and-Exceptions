# Combine the two files for Exercise 10-11
import json

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/favorite_number.json'

try: 
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
        print(f"I know your favorite number! It's {favorite_number}.")
else:
    print(f"I know your favorite number! It's {favorite_number}.")