l = [["wenzhi", 18],["aleko", 20],["fox", 22],["maomao", 23], ["pangzi", 23],["cj", 18],["yezi", 20]]
def arrTodic(arr):
    dic = {}
    for i in l:
        key = str(i[1])
        value = i[0]
        if dic.get(key) == None:
            dic[key] = []
        dic[key].append(value)
    return dic


iii = arrTodic(l)

print(iii)


def dicToArr(dic):
    arr1 = []
    for key, arr in iii.items():
        for i in arr:
            arr1.append([i, key])
    return arr1

print(dicToArr(iii))