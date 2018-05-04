data = {
  '芳华' : ['黄轩','苗苗'],
  '战狼2' : ['吴京','吴刚','卢婧姗'],
  '无问西东' : ['章子怡','黄晓明','张震','王力宏'],
  '大兵小将' : ['成龙', '王力宏', '刘承俊']
}
name = input("请输入要查询的演员名：")
for movie in data:
    actors = data[movie]
    if name in actors:
        print(name + "出演了电影《" + movie + "》。")
print('没有该演员记录')