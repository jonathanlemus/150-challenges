# Update program 027 so that it will display the answer to two decimal places.

num = float(input("Enter a number with decimal: "))
answer = num * 2

print(answer)
print(round(answer, 2))