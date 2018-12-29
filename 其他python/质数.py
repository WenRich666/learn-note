def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

a = []
for i in range(1,1000):
    if isPrime(i):
        a.append(i)

print(len(a))