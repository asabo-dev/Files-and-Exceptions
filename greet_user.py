# Retrieve Data stored in json
import json

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")