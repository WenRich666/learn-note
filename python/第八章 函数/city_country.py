def cy(city,country):
    """返回一个国家和城市的信息"""
    a_place = city + " " + country
    return a_place.title()

a = cy("beijing","china")
b = cy("new york","north america")
c = cy("paris","france")

print(a)
print(b)
print(c)