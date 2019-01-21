class Student():
    sum = 0
    name = "qiyue"
    age = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__class__.sum += 1
        print("当前班级总数为：" + str(self.__class__.sum))
        print("他的名字叫" + self.name + ",他今年" + str(self.age))

    def do_homework(self):
        print("homework")

    @classmethod
    def plus_sum(cls):
        print(cls.sum)


student1 = Student("石敢当",18)
student2 = Student("石兴豪",25)
student3 = Student("石兴凯",37)
# print(self.__class__.sum)
# print(student1.name)
# print(Student.name)
