"""
给定两个字符串 A 和 B，现在要将 A 经过若干操作变为 B，可进行的操作有：

删除–将字符串 A 中的某个字符删除。
插入–在字符串 A 的某个位置插入某个字符。
替换–将字符串 A 中的某个字符替换为另一个字符。
现在请你求出，将 A 变为 B 至少需要进行多少次操作。

输入格式
第一行包含整数 n，表示字符串 A 的长度。

第二行包含一个长度为 n 的字符串 A。

第三行包含整数 m，表示字符串 B 的长度。

第四行包含一个长度为 m 的字符串 B。

字符串中均只包含大写字母。

输出格式
输出一个整数，表示最少操作次数。

数据范围
1≤n,m≤1000
输入样例：
10
AGTCTGACGC
11
AGTAAGTAGGC
输出样例：
4
"""
""" 题解
①状态表示 f(i,j) 所有A[i]变为B[j]的操作方式
②状态转移
f(i,j)
a
   i
AGTC
AGT       删
  j
 i
AG
AGT       增
 j-1

AGTC
AGTA

        删           增           改
        f(i-1,j)+1   f(i,j-1)+1  f(i-1,j-1)+1/0

10
AGTCTGACGC
11
AGTAAGTAGGC
输出样例：
4
"""


def main():
    n = int(input())
    s1 = ['0'] + list(input())
    m = int(input())
    s2 = ['0'] + list(input())
    f = [[0]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        f[i][0] = i

    for i in range(m+1):
        f[0][i] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            f[i][j] = min(f[i-1][j]+1, f[i][j-1]+1)
            if s1[i] != s2[j]:
                f[i][j] = min(f[i][j], f[i-1][j-1]+1)
            else:
                f[i][j] = min(f[i][j], f[i - 1][j - 1])
    print(f[n][m])


main()
