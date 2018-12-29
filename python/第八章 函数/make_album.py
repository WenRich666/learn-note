def make_album(singer_name,album):
    """记录一个歌手和他的专辑"""
    a_singer = {"singer_name":name,"album":album}
    return a_singer

a = make_album{"周杰伦","七里香"}
# b = make_album("eminem","infinity")
# c = make_album("dr.dre","2001")

print(a)