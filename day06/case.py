# coding:utf-8

# 将以下字符串转换成字典。
# a = "k:1|k1:2|k2:3|k3:4"
# new_li = a.split("|")
# print(new_li)
# dic = {}
# for i in new_li:
#     k, v = i.split(":")
#     dic[k] = int(v)
# print(dic)


# 以下列表的元素，如果大于66，则放到字典的k1的value里，如果小于66，则放到字典k2的value里。
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99,]
# dic = {'k1': [], 'k2': []}
# for i in li:
#     if i == 66:
#         continue
#     elif i > 66:
#         dic.setdefault('k1').append(i)
#     elif i < 66:
#         dic.setdefault('k2').append(i)
#     else:
#         print('输入错误')
# print(dic)


# 输出商品列表。用户输入序号，显示用户选中的商品 商品列表：

goods = [{"name": "电脑", "price": "1999"}, {"name": "鼠标", "price": "10"}, {"name": "游艇", "price": "20"},
         {"name": "美女", "price": "998"}, ]
'''
1、要求显示 序号+商品名称+商品价格。如：
    1 电脑 1999
    2 鼠标 10
2、用户输入选择的商品序号，然后打印商品名称及商品价格。
3、如果用户输入的商品序号有误，则提示输入有误，并重新输入。
4、用户输入Q或者q，退出程序
'''

for i in goods:
    print(goods.index(i)+1, i['name'], i['price'])   # goods.index(i) 表示每次索引的下标。下标从0开始，这里加1为了方便看。
while True:
    str_input = input("请输入您要选择的商品序号，输入Q退出：")
    if str_input.isdigit() and 0 < int(str_input) <= len(goods):   # 判断是否在区间，注意这里要加等于
        i_index = int(str_input)-1   # 把输入值转换成数字。然后减去1即为goods对应的下标。
        print(goods[i_index]['name'], goods[i_index]['price'])    # 打印对应下标的数据
    elif str_input.upper() == 'Q':
        break
    else:
        print("输入有误，请重新输入。")