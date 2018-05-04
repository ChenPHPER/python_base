# 批量处理商品价格
data = [120, 90, 150, 200, 80]
new_price = []
for d in data:
    if d > 100:
        new_price.append(d*0.8)
    else:
        new_price.append(d*0.9)
print(new_price)