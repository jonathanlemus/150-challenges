# Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.

bill = int(input("What's the total cost of the bill ? "))
people = int(input("How many people are there? "))

each = bill / people

print(f'Each person must pay $ {each}')