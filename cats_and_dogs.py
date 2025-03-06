# EXERCISE 10-8: Cat and Dog names.

filename1 = '/Users/quanefiom/desktop/github_projects/Chapter 10/cats.txt'
filename2 = '/Users/quanefiom/desktop/github_projects/Chapter 10/dogs.txt'

print("Cats: ")
try:
    with open(filename1, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print("The file you are looking for cannot be found.")
else:
    print(f"{contents}\n")


print("Dogs: ")
try:
    with open(filename2, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print("The file you are looking for cannot be found.")
else:
    print(contents)