cars = ["lamborghini","ferrari","rolls-royce"]
cars.append("mercedes")
for car in cars:
    print(car.title() + ",that's a wonderful car")
    print("I can't wait to buy + car.title() on the next week")

cars = ["lamborghini","rolls-royce","ferrari","mercedes"]
cars.insert(1,"audi")
del cars[1]
poped_car = cars.pop(3)
print("The first car I owned was a" + poped_car.title() + ",but i sold it last year")
last_car = cars.pop(0)
print("so, I bought a " + cars.pop() + " in this year")
print(cars)
cars.insert(1,"lamborghini")
cars.insert(2,"ferrari")
cars.insert(3,"mercedes")
print(cars)
cars.remove("mercedes")
print(cars)

cars = ["lamborghini","rolls-royce","ferrari","mercedes","audi","bmw"]
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars.sort()
print(cars)

too_expensive = "rolls-royce"
cars.remove(too_expensive)
print("\nA " + too_expensive.title() + " is too expensive for me")

cars.reverse()
print(cars)

hoping_travel = ["paris","tokyo","beijing","new york","london"]
print("\nHere is the original list:")
print(hoping_travel)
print("\nHere is the sorted list:")
print(sorted(hoping_travel))
print("\nHere is the original list again:")
print(hoping_travel)
print(sorted(hoping_travel,reverse=True))

print(hoping_travel[0].title() + " is a city of France.")



cars = ["lamborghini","ferrari","rolls-royce","mercedes","audi"]
print("The first three items in the list are:")
for car in cars[0:3]:
    print(car.title())
print("Three items from the middle of the list are:")
for car in cars[1:4]:
    print(car.title())
print("The last three items in the list are:")
for car in cars[2:5]:
    print(car.title())

cars = ["lamborghini","ferrari","rolls-royce","mercedes","bmw"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

cars = ["lamborghini","rolls-royce","ferrari","mercedes","audi","bmw"]
