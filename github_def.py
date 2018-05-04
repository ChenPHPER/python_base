
# 重量数据来源于input输入
weight = int(input("Please enter weight: "))
# 定义函数
def order(weight):
	# 利用if语句判断重量
	if weight > 3 :
		total = weight * 5
	else:
		total = weight * 6
	# 返回计算结果
	return total

# 调用函数
total = order(weight)
# 打印结果
order_string = "You need to pay " + str(total) + "."
print(order_string)