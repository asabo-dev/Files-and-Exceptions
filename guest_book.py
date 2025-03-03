# EXERCISE 10-4

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/guest_book.txt'

print("Please enter the guest names.")
print("Enter 'q' anytime to quit.")

while True:
    name = input("Enter guest name: ")

    if name == 'q':
        break
    else:
        print(f"Hello {name.title()}, you are welcome.")
        with open(filename, 'a') as file_object:
            file_object.write(f"{name.title()}, visited yesterday.\n")

print("---The End---")
   

