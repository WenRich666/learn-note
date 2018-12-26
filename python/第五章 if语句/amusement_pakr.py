age = 12
if age < 4:
    print("your admission cost in $0.")
elif age < 18:
    print("Your admission is cost $5.")
else:
    print("Your admission is cost $10.")

age = 80
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission is $" + str(price) + ".")

age = 36
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age > 65:
    price =5
else:
    price = 10
print("Your admission is $" + str(price) + ".")


age = 70
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age > 65:
    price = 5
print("Your admission is $" + str(price) + ".")