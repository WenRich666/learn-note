class Student():
    name = " qiyue"
    age = 0
    sum = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__score = 0
        self.__class__.sum += 1
        print(self.name + "今年" + str(self.age) + "，他喜欢做作业")

    def do_homework(self):
        print("do homework")

    def marking(self,score):
        self.score = score
        print(self.name + "同学本次考试分数为：" + str(self.score))

    @classmethod
    def plus_sum(cls):
        print(cls.sum)

student = Student("小学生","10")
# student.marking(69)
# student.__score = -1
# print(student.__score)
# student.plus_sum()
student.do_homework()


