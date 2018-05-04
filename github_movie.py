# 最佳影片提名名单
list = ['泰坦尼克号', '洛城机密', '骄阳似我', '一脱到底', '尽善尽美']
# 定义函数
def star(s):
	# 定义函数内部操作，for循环遍历list数据
	# 设置变量i，用于记录当前循环到列表中的第几个元素
    i = 0
    for name in list:
        if name == s:
        	# 修改list中的元素
            list[i] = '*'+name
        i = i+1
# 调用函数
star('泰坦尼克号')
# 打印结果
print(list)