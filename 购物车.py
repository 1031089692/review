# coding:utf-8

'''
题目1：
1、让用户输入金额
2、选择要购买的商品加入购物车
3、选择完毕时让用户输入N结算，输入Q退出
4、结算时，如果总价超过了输入的金额提示'余额不足'
可以尽可能的详细

题目2：判断下面print的值
print(1.2-1.0==0.2)
'''

goods = [
    {"name": "游艇", "price": "2000"},
    {"name": "键盘", "price": "100"},
    {"name": "鼠标", "price": "80"},
    {"name": "美女", "price": "500"},
    {"name": "鸡蛋", "price": "5"},
]


class ShoppingCart():
    add_list = {}   # 购买的商品列表 。key==索引。value == 商品的数量
    add_money = 0    # 购买需要的钱

    def input_money(self):
        # 判断输入余额是否符合要求
        money = input("请输入您的余额(整数即可):")
        if money.isdigit() and 0 < int(money):
            return money
        else:
            print("请输入正确格式的余额")
            self.input_money()

    def add_goods(self, money):
        for el in range(len(goods)):
            print(el+1, goods[el]['name'], goods[el]['price'])
        while 1:
            choose = input("请选择您要购买的编号(输入N结算，输入Q退出):")
            if choose.isdigit() and 0 < int(choose) <= len(goods):   # 用户输入的编号正常
                list_index = int(choose) - 1   # 通过用户输入的编号来获得goods的索引
                if self.add_list.get(list_index) == None:
                    self.add_list[list_index] = 1
                    print(self.add_list)
                else:
                    self.add_list[list_index] = self.add_list[list_index] + 1
                    print(self.add_list)
                # 把用户选择的商品加入到购物车
            elif choose.upper() == 'Q':
                break
            elif choose.upper() == 'N':
                for f in self.add_list:
                    self.add_money = self.add_money + int(self.add_list[f]) * int(goods[f]['price'])
                print("预计花费%s" % self.add_money)
                if int(money) - int(self.add_money) >= 0:
                    rest_mone = int(money) - int(self.add_money)
                    print("您的余额充足。目前剩余可用余额为%s:" % rest_mone)
                elif int(money) - int(self.add_money) < 0:
                    rest_mone = int(self.add_money)-int(money)
                    print("对不起。您的余额不足。缺少%s元。请充值" % rest_mone)
                else:
                    print("出现了某种未知情况")
                break
            else:
                print("您输入的编号有误,请重新输入!")
                continue



a = ShoppingCart()
b = a.input_money()
a.add_goods(b)