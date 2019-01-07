# class Car():
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self,make,model,year):
#         """初始化描述汽车的特性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_time = str(self.year) + " " + self.make + " " + self.model
#         return long_time.title()
#
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息"""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self,mileage):
#         """
#         将里程表读数设置为指定的值
#         禁止将里程表读数往回调
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self,mileage):
#         """将里程表读数增加指定的量"""
#         self.odometer_reading += mileage
#
# class ElectricCar(Car):
#     """电动汽车的独特之处"""
#     def __init__(self,make,model,year):
#         """初始化父类的属性"""
#         super().__init__(make,model,year)
#
# my_tesla = ElectricCar("tesla","model's",2016)
# print(my_tesla.get_descriptive_name())

#
# class Car():
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         """初始化描述汽车的特性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_time = str(self.year) + " " + self.make + " " + self.model
#         return long_time.title()
#
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息"""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         """
#         将里程表读数设置为指定的值
#         禁止将里程表读数往回调
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, mileage):
#         """将里程表读数增加指定的量"""
#         self.odometer_reading += mileage
#
#
# class ElectricCar(Car):
#     """电动汽车的独特之处"""
#
#     def __init__(self, make, model, year):
#         """
#         电动汽车的独特之处
#         初始化父类的属性,再初始化电动汽车特有的属性
#         """
#         super().__init__(make, model, year)
#         self.battery_size = 70
#
#     def describe_battery(self):
#         """打印一条描述电瓶容量的消息"""
#         print("This car has a " + str(self.battery_size) + "-kwh battery.")
#
# my_tesla = ElectricCar("tesla", "model's", 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()




class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的特性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_time = str(self.year) + " " + self.make + " " + self.model
        return long_time.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, mileage):
        """将里程表读数增加指定的量"""
        self.odometer_reading += mileage

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self,battery_size = 70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery")

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        电动汽车的独特之处
        初始化父类的属性,再初始化电动汽车特有的属性
        """
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar("tesla", "model's", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()