class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        print(restaurant_name + "的烹饪方式是" + cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + "正在营业")

a_restaurant = Restaurant("海底捞","火锅")
a_restaurant.open_restaurant()