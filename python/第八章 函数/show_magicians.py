def show_magicians(names):
    """显示魔术师的名字"""
    for name in names:
        msg = name.title() + "'s great magician!"
        print(msg)
magicians = ["harry","david","micheal",'lucas']
show_magicians(magicians)

