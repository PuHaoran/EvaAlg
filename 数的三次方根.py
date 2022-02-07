# 二分
"""
给定一个浮点数 n，求它的三次方根。

输入格式
共一行，包含一个浮点数 n。

输出格式
共一行，包含一个浮点数，表示问题的解。

注意，结果保留 6 位小数。

数据范围
−10000≤n≤10000
输入样例：
1000.00
输出样例：
10.000000
"""

""" 题解
确定一个区间，不断根据条件缩小区间范围，直至满足<epson
"""


def get_root(m):
    l, r = min(m, -1), max(1, m)
    while r - l > 0.00000001:
        mid = (l + r) / 2.0
        if mid ** 3 > m:
            l, r = l, mid
        else:
            l, r = mid, r
    return round(mid, 6)


def main():
    m = float(input())
    print(format(get_root(m), '.6f'))


main()
