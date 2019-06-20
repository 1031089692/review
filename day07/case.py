# coding:utf-8


# 问题。念数字。给一个字典。key是数子，value是发音，包括相关符号。
# 然后用户输入一个数字，比如-127。print fu yibai ershi  qi(还可以考虑下小数位)





# ----未完待续

# 问题 给出一下车牌。根据车牌的信息，分析出歌声的车牌持有量。
cars = ["鲁A123456", "沪B45678", "黑A123456", "黑A123456"]
locals = {"鲁": "山东", "沪": "上海", "黑": "黑龙江"}
result = {}

for car in cars:
    first_name = car[0]
    location = locals[first_name]   # 山东
    # 开始统计
    if result.get(location) == None:  # 所有不同地方第一次统计
        result[location] = 1
    else:
        result[location] = result[location] + 1
print(result)