# 双指针
"""
给定一个长度为 n 的整数序列 a1,a2,…,an 以及一个长度为 m 的整数序列 b1,b2,…,bm。

请你判断 a 序列是否为 b 序列的子序列。

子序列指序列的一部分项按原有次序排列而得的序列，例如序列 {a1,a3,a5} 是序列 {a1,a2,a3,a4,a5} 的一个子序列。

输入格式
第一行包含两个整数 n,m。

第二行包含 n 个整数，表示 a1,a2,…,an。

第三行包含 m 个整数，表示 b1,b2,…,bm。

输出格式
如果 a 序列是 b 序列的子序列，输出一行 Yes。

否则，输出 No。

数据范围
1≤n≤m≤105,
−109≤ai,bi≤109
输入样例：
3 5
1 3 5
1 2 3 4 5
输出样例：
Yes
"""
""" 题解
3 5
1 3 5
1 2 3 4 5

1 3 5
i
1 2 3 4 5
j
1 3 5
  i
1 2 3 4 5
    j
1 3 5
    i
1 2 3 4 5
        j
"""


def check_sub_sequence(a_arr, b_arr):
    m, n = len(a_arr), len(b_arr)
    i, j, cnt = 0, 0, 0
    while i < m and j < n:
        if a_arr[i] == b_arr[j]:
            i += 1
            cnt += 1
        j += 1
    if cnt == m:
        return "Yes"
    return "No"

def main():
    _ = [int(i) for i in input().split()]
    a_arr = [int(i) for i in input().split()]
    b_arr = [int(i) for i in input().split()]
    print(check_sub_sequence(a_arr, b_arr))


main()

