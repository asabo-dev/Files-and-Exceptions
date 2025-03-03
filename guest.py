# EXERCISE 10-3

filename = '/Users/quanefiom/desktop/github_projects/Chapter 10/guest.txt'

guest_name = input("Enter name of the guest: ")

with open(filename, 'w') as file_object:
    file_object.write(guest_name)