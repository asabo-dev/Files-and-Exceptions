# Analyzing Text

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/alice.txt'

"""The else block runs if the code in the try block runs successfully."""
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    """
    split() is a string method, which by default splits a string
    wherever it finds any whitespace.
    """
    num_words = len(words)
    print(f"The file 'alice.txt' has about {num_words} words.")
