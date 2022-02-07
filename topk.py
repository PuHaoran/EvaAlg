# 排序 topk
"""
给定一个长度为 n 的整数数列，以及一个整数 k，请用快速选择算法求出数列从小到大排序后的第 k 个数。

输入格式
第一行包含两个整数 n 和 k。

第二行包含 n 个整数（所有整数均在 1∼109 范围内），表示整数数列。

输出格式
输出一个整数，表示数列的第 k 小数。

数据范围
1≤n≤100000,
1≤k≤n
输入样例：
5 3
2 4 1 5 3
输出样例：
3
"""
""" 题解
快速选择算法
1) 选定一个q[l], q[r], q[(l+r)//2]作为x。
2）Left < x, Right > x, 否则交换i j。
3）判断k对应的索引在左区间还是右区间。
  k-1 <= j, 递归Left。
  k > j, 递归Right。
"""


def topk(arr, l, r, k):
    if l == r:
        return arr[l]
    i, j = l-1, r+1
    while i < j:
        while 1:
            i += 1
            if arr[l] <= arr[i]:
                break
        while 1:
            j -= 1
            if arr[l] >= arr[j]:
                break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if k-1 <= j:
        return topk(arr, l, j, k)
    else:
        return topk(arr, j+1, r, k)


def main():
    _k = [int(i) for i in input().split()]
    _, k = _k[0], _k[1]
    arr = [int(i) for i in input().split()]
    res = topk(arr, 0, len(arr)-1, k)
    print(res)

main()
