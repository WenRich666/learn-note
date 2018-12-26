# user_0 = {
#     "username":"efermi",
#     "first":"enrico",
#     "last":"fermi",
# }
# for key,value in user_0.items():
#     print("\nKey:" + key)
#     print("Value:" + value)


# a = list(range(1,9))
#
# for i in range(1,len(a),2):
#     print(a[i],end = " | ")
#
# b = a[0:len(a):2]
# print(b)


# a = list(range(2,1001))
# for num in a:
#     if num % num == 0:
#         5 % 2 == 0 or 5 % 3 == 0 or 5 % 4 == 0
#         return
#

sum = 0
num = list(range(1,11))
for i in num:
    sum += i
print(sum)
