squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

cubes = [value ** 3 for value in range(1,11)]
print(cubes)

a = [value for value in range(1,102) if value % 3 ==0]
print(a)