# 前缀和
"""
输入一个长度为 n 的整数序列。

接下来再输入 m 个询问，每个询问输入一对 l,r。

对于每个询问，输出原序列中从第 l 个数到第 r 个数的和。

输入格式
第一行包含两个整数 n 和 m。

第二行包含 n 个整数，表示整数数列。

接下来 m 行，每行包含两个整数 l 和 r，表示一个询问的区间范围。

输出格式
共 m 行，每行输出一个询问的结果。

数据范围
1≤l≤r≤n,
1≤n,m≤100000,
−1000≤数列中元素的值≤1000
输入样例：
5 3
2 1 3 6 4
1 2
1 3
2 4
输出样例：
3
6
10
"""
""" 题解
①构建前缀和数组。
②利用前缀和数组求区间和。
2 1 3 6 4
=>
2 3 6 12 16
sum_arr[r] - sum_arr[l-1]
输入样例：
5 3
2 1 3 6 4
1 2
1 3
2 4
输出样例：
3
6
10
"""


def prefix_sum(sum_arr, l, r):
    if l == 1:
        return sum_arr[r-1]
    return sum_arr[r-1] - sum_arr[l-2]


def main():
    _ = [int(i) for i in input().split()]
    m, n = _[0], _[1]
    arr = [int(i) for i in input().split()]
    sum_arr = [0] * len(arr)
    for i in range(len(arr)):
        sum_arr[i] = arr[i]
        if i != 0:
            sum_arr[i] += sum_arr[i-1]
    for i in range(n):
        lr = [int(i) for i in input().split()]
        l, r = lr[0], lr[1]
        res = prefix_sum(sum_arr, l, r)
        print(res)


main()
