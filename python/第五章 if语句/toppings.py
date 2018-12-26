requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")

requested_toppings = ["mushrooms","extra cheese"]

if "mushrooms" in requested_topping:
    print("Adding mushrooms")
if "pepperoni" in requested_topping:
    print("Adding pepperoni")
if "extra cheese" in requested_topping:
    print("Adding extra cheese")

print("\nFinished making your pizza!")

alien_color = ["green","yellow","red"]
if "green" in alien_color:
    print("Player will get 5 point")
if "yellow" in alien_color:
    print("Player will get 10 point")
if "red" in alien_color:
    print("player will get 15 point")

age = 30
if age < 2:
    print("It is a baby")
if 2 < age < 4:
    print("He is starting walk")
if 4 < age < 13:
    print("He is a child")
if 13 < age < 20:
    print("He is a teenager")
if 20 < age < 65:
    print("He is a adult")
if age > 65:
    print("He is an old people")


requested_toppings = ["mushrooms","green peppers","extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizaa!")


requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you want a plain pizza?")


available_toppings = ["mushrooms","olives","green peppers",
                      "pepperoni","pineapple","extra cheese"]

requested_toppings = ["mushrooms","french fries","extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry ,we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")


