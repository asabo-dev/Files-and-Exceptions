# Handling the FileNotFoundError Exception

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/alice.txt'

"""The try-except Block handles the FileNotFoundError gracefully."""
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
