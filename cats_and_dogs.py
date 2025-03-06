# EXERCISE 10-9:  Silent Cat and Dog names.

filename1 = ''
filename2 = '/Users/quanefiom/desktop/github_projects/Chapter 10/dogs.txt'

print("Cats: ")
try:
    with open(filename1, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    pass
    """Fail silently, with no report on the error."""
else:
    print(contents)

print("\n")
print("Dogs: ")
try:
    with open(filename2, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print("The file you are looking for cannot be found.")
else:
    print(contents)