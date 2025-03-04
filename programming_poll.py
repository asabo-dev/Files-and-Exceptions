# EXERCISE 10-5

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/programming_poll.txt'

print("What are the reasons you like programming?")
print("Enter 'q' to quit at any point.")

while True:
    answer = input("Why do you like programming?: ")
    if answer == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{answer}\n")