# Handling the FileNotFoundError Exception

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/alice.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read()
"""
This code is return an error because there no such file named 'alice.txt'.
Use try-except Block to handle the FileNotFoundError gracefully.
"""