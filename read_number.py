# EXERCISE 10-11 Retrieve favorite number from json.
import json

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/favorite_number.json'

with open(filename) as f:
    favorite_number = json.load(f)

print(f"I know your favorite number! It's {favorite_number}.")