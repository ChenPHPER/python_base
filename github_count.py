# 考勤数据
list = [22, 23, 20, 19, 21, 22, 22, 23, 24, 20, 20, 22]
# 定义函数check_in，包含一个参数list
def check_in(list):
	# 定义用于计数的变量count
	count = 0
	# for循环，检查每个月的考勤情况
	for days in list:
		if days < 20:
			# 计数变量自加一
			count = count + 1
	# 循环结束，打印结果
	if count != 0:
		print("有"+str(count)+"个月考勤不合格。")
	else:
		print("全年考勤合格。")
check_in(list)