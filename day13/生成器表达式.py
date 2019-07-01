# coding:utf-8

# tu = (i for i in range(10))  # 没有元祖推导式。这是生成器表达式
# print(tu)
# print(tu.__next__())


#生成器函数
# def func():
#     print(111)
#     yield 222
#
#
# g = func()
# g1 = (i for i in g)
# g2 = (i for i in g1)
#
# print(list(g))  # [222]这里把源头func的数据拿走了
# print(list(g1))  # 所以从这里开始，源头已经没有数据了
# print(list(g2))


# 进阶题：如下。判断打印的数据
# 求和函数
def add(a, b):
    return a+b


# 生成器函数 0-3
def test():
    for r_i in range(4):
        yield r_i


g = test()

for n in [2, 10]:               # next，find，list 还有for循环函数名这几种方法才会拿值，这里没有拿值
    g = (add(n, i) for i in g)
print(list(g))

# ----------------------------------
'''
解题思路：
    1、拆分循环：
        for n in [2, 10]:              
        g = (add(n, i) for i in g)
        可以拆分为：
        n = 2
            g = (add(n, i) for i in g)
        n = 10
            g = (add(n, i) for i in g)
        变形可得
        n = 10
            g = (add(n, i) for i in (add(n, i) for i in g))
    2、仔细审题：
        这里for循环g并没有取值。直到最后的list(g)才开始拿值。
        g = 0，1，2，3和n = 10带入上述表达式.如g=0
        g = (10+i for i in (10+i for i in 0))
        g = 20
        故最后结果为20,21,22,23
    3、注：为什么要变形？
        需要理解的是，n=2时，这个时候表达式的n并不会把值代入进去，因为g并没有取值。所以n=10时，需要代入的是上面的表达式，而不是一个
        计算出来的结果。变形可以方便理解。
    4、核心考点：惰性机制。不到最后不会拿值
'''

'''
如果for循环再改下。改成for n in [2,10,5]
同理：转化为：
n = 5，g = 0,1,2,3 
带入转换得：g = 15 所以结果为[15,16,17,18 ]
'''


