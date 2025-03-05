# Working with Multiple Files.

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
        """
        'pass' statement explicitly tell Python to do nothing in the except block.
        Thereby allowing the code to fail silently without any report in the output.
        """
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file 'alice.txt' has about {num_words} words.")

filenames = [
    '/Users/quanefiom/desktop/github_projects/Chapter 10/alice.txt',
    '/Users/quanefiom/desktop/github_projects/Chapter 10/siddhartha.txt',
    '/Users/quanefiom/desktop/github_projects/Chapter 10/moby_dick.txt',
    '/Users/quanefiom/desktop/github_projects/Chapter 10/little_women.txt'
]
for filename in filenames:
    count_words(filename)