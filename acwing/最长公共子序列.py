"""
给定两个长度分别为 N 和 M 的字符串 A 和 B，求既是 A 的子序列又是 B 的子序列的字符串长度最长是多少。

输入格式
第一行包含两个整数 N 和 M。

第二行包含一个长度为 N 的字符串，表示字符串 A。

第三行包含一个长度为 M 的字符串，表示字符串 B。

字符串均由小写字母构成。

输出格式
输出一个整数，表示最大长度。

数据范围
1≤N,M≤1000
输入样例：
4 5
acbd
abedc
输出样例：
3
"""
""" 题解
①状态表示。f(i,j) 所有A[1~i]与B[1~j]的子序列的最长公共子序列。
②状态转移。
划分成若干个子集，看A和B子序列的最后一个元素，这里用0和1表示A[i]和B[j]是否包含在子序列中，eg:
ac
ab   00

acb
abe  10

acbd
ab   01

acb
ab   11

            00            01           10               11
            不包含ai和bj   不含ai,包含bj  包含ai,不包含bj    包含ai和bj
f(i,j)   max(f(i-1,j-1)   f(i-1,j)     f(i,j-1)         f(i-1,j-1)+1)
"""


def main():
    n, m = map(int, input().split())
    s1 = ['0'] + list(input())
    s2 = ['0'] + list(input())
    f = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            f[i][j] = max(f[i-1][j], f[i][j-1])
            if s1[i] == s2[j]:
                f[i][j] = f[i-1][j-1]+1
    print(f[n][m])


main()
