class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("这个餐厅叫" + self.restaurant_name + "，"
              + "它是个" + self.cuisine_type + "店")

    def open_restaurant(self):
        print("这个餐厅正在营业")

# restaurant = Restaurant("麦当劳","快餐")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

