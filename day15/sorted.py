# coding:utf-8

# 数字排序
lst = [2, 5, 1, 3, 8, 4]
a = sorted(lst)
print(a)

# 字符串排序:需自己制定排序规则，如按照长度
lst2 = ['阿尔帕西诺', '腾讯', '西门子', '阿里巴巴', '斯坦尼斯拉夫']
def func(s):
    return len(s)
b = sorted(lst2, key=func, reverse=True)
print(b)


# 关于sorted和lambda的组合
lst3 = [
    {'name': '阿尔帕西诺'},
    {'name': '鬼谷子'},
    {'name': '斯坦尼斯拉夫'}
]
ll = sorted(lst3, key=lambda el: len(el['name']), reverse=True)
print(ll)