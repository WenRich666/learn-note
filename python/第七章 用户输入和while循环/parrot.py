# message = input("Tell me something,and i will repeat it back to you:")
# print(message)

# name = input("Please enter your name:")
# print("Hello," + name + "!")

# prompt = "If you tell us who you are,we can personaliz the message you see."
# prompt += "\nwhat is your first name?"
# name = input(prompt)
# print("\nHello," + name + "!")
#
# age = input("How old are you?")
# print(age)

# prompt = "\nTell me something,and i will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != "quit":
#     message = input(prompt)
#
#     if message != "quit":
#         print(message)

# prompt = "\nTell me something,and i will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
#
# active = True
# while active:
#     message = input(prompt)
#     if message == "quit":
#         active = False
#     else:
#         print(message)

prompt = "\n阿乐是傻逼？"
prompt += "\n是的\n输入'不是'结束这个游戏"
message = ""
message1 = "\n其实他是个大傻逼"

while message != '不是':
    message = input(prompt)
while message == '不是':
    message = input(message1)