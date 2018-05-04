# 编程判断是否含有Trump这个词
string = "The high-profile engagement between Chinese President Xi Jinping and his U.S. counterpart Donald Trump on Thursday has caught the spotlight globally. Experts said their meeting has borne remarkable fruit, and the forward-looking attitude of the two heads of state towards bilateral cooperation will bring benefits to the two countries, the Asia-Pacific and the world at large."
# 将文本中的逗号替换为空格，便于后续利用空格字符分割文本
string = string.replace(", ", " ")
# 将文本中的句号替换为空格，便于后续利用空格字符分割文本
string = string.replace(". ", " ")
# 利用空格分割文本，得到一个列表，列表中的每个元素都是一个单词
string_list = string.split(" ")
if "Trump" in string_list:
    print("This article maybe about Trump.")
else:
    print("This article maybe not about Trump.")