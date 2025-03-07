# EXERCISE 10-10 Count Word repitions in a text file

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/thousnad_nights.txt'

with open(filename) as f:
    content = f.read()
    word_count = content.lower().count('the ')
    print(f"The word 'the' appears {word_count} times in the story.")
    