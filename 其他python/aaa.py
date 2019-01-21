# a = input("告诉我一个数字")
# b = input("告诉我另一个数字")
#
# def add(a,b):
#     while True:
#         a = input("告诉我一个数字")
#         a = int(a)
#         b = input("告诉我另一个数字")
#         b = int(b)
#
#         c = (a + b) * b/2
#         print(c)
#
#     while a == "q":
#         break
#
# add(0,0)

#
# def add():
#     while True:
#         a = input("输入数字 a：")
#         if a == "q":
#             break
#         b = input("输入数字 b：")
#         if b == "q":
#             break
#
#         result = 0
#
#         for i in range(int(a),int(b) + 1):
#             result += str(a) + str(b)
#
#         print(result)
#
# add()

class Student():
    sum = 0

    def __init__(self,name,age,gender,score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score
        if self.gender == "male":
            print("\nHis name is " + self.name.title() + ",his age is " + str(self.age) +
                  ",his gender is " + self.gender + ",his score is " + str(self.score) + ".")
        elif self.gender == "female":
            print("\nHer name is " + self.name.title() + ",her age is " + str(self.age) +
                  ",her gender is " + self.gender + ",her score is " + str(self.score) + ".")

    def examination(self):
        if self.score >= 80:
            print("excellent")
        if 60 < self.score < 80 :
            print("pass")
        if self.score <= 60:
            print("fail")

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        # print(cls.sum)
        print("当前班级人数为：" + str(cls.sum))

student1 = Student("john",17,"male",78)
student1.examination()
Student.plus_sum()
student2 = Student("mary",16,"female",92)
student2.examination()
Student.plus_sum()
student3 = Student("bob",21,"male",43)
student3.examination()
Student.plus_sum()
student4 = Student("kate",18,"female",63)
student4.examination()
Student.plus_sum()
student5 = Student("catherine",15,"male",88)
student5.examination()
Student.plus_sum()


