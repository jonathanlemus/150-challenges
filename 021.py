# Ask the user to enter their first name and then ask them to enter their surname. Join them together with a space between and display the name and the length of whole name.

firstname = input('Enter your firstname: ')
surname = input('Enter your surname: ')

name = firstname + " " + surname
length = len(name)

print(name)
print(length)
