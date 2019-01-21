class Student():
    sum = 0
    name = "qiyue"
    age = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("我叫" + name + "，今年" + str(age) + "岁")
        self.__class__.sum += 1
        print("当前班级人数为：" + str(self.__class__.sum))

    def do_homework(self):
        print("今晚" + self.name + "要做作业")

    # def subject(self,subject1,subject2,subject3):
    #     print("做作业就是为了考" + subject1 + subject2 + subject3)

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

student1 = Student("石敢当",18)
Student.plus_sum()
student2 = Student("喜小乐",18)
Student.plus_sum()
student3 = Student("小诺",18)
Student.plus_sum()
# student1.do_homework()
# student1.subject("语文","数学","英语")

