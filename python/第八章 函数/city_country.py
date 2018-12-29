def city_country(city,country):
    """返回一个国家和城市的信息"""
    a_place = city + " " + country
    return a_place.title()

a = city_country("beijing","china")
b = city_country("new york","north america")
c = city_country("paris","france")

print(a)
print(b)
print(c)