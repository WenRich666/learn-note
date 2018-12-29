# def get_formatted_name(first_name,last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + " " + last_name
#     return full_name.title()
#
# musician = get_formatted_name("jimi","hendrix")
# print(musician)


# def get_formatted_name(first_name,last_name,middle_name = ""):
#     """返回整洁的姓名"""
#     if middle_name:
#         full_name = first_name + " " + middle_name + " " + last_name
#     else:
#         full_name = first_name + " " + last_name
#     return full_name.title()
#
# musician = get_formatted_name("jimi","hendrix")
# print(musician)
#
# magician = get_formatted_name("john","hooker","lee")
# print(magician)


def formatted_name(first_name,last_name,middle_name = ""):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
        return full_name.title()

色魔 = formatted_name("立佳","吴")
print(色魔)