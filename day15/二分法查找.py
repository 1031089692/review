# coding:utf-8

# 使用二分法可以提高效率，前提条件：有序序列。
# lst = [22, 33, 44, 55, 66, 77, 88, 222, 444, 555, 777, 888, 999]
# n = 88
#
# left = 0
# right = len(lst) - 1
#
# while left < right:  # 边界,当右边比左边还小的时候退出循环(这里比较的是索引。当左边界不小于右边界，代表已经重合，即比较完毕)
#     mid = (left + right) // 2  # 必须是整除,索引没有小数
#     if lst[mid] > n:
#         right = mid - 1
#     if lst[mid] < n:
#         left = mid + 1
#     if lst[mid] == n:
#         print("找到了这个数")
#         break
# else:
#     print("没有找到这个数")


# 自定义一个list，用递归来完成二分法,要求如果找到，返回对应的索引，没找到返回-1。
lst = [22, 33, 44, 55, 66, 77, 88, 222, 444, 555, 777, 888, 999]


def fun(n, left, right):
    if left < right:
        mid = (left+right)//2
        if n > lst[mid]:
            left = mid + 1
            # 深坑。函数的返回值返回给调用者。如循环多次，最外层拿不到最里面一层的返回值，故每一次递归都要return
            return fun(n, left, right)
        if n < lst[mid]:
            right = mid - 1
            return fun(n, left, right)
        if n == lst[mid]:
            print('找到了')
            return mid
    else:
        print("没有这个数")
        return -1


fet = fun(66, 0, len(lst)-1)
print(fet)