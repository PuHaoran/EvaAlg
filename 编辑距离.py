"""
给定 n 个长度不超过 10 的字符串以及 m 次询问，每次询问给出一个字符串和一个操作次数上限。

对于每次询问，请你求出给定的 n 个字符串中有多少个字符串可以在上限操作次数内经过操作变成询问给出的字符串。

每个对字符串进行的单个字符的插入、删除或替换算作一次操作。

输入格式
第一行包含两个整数 n 和 m。

接下来 n 行，每行包含一个字符串，表示给定的字符串。

再接下来 m 行，每行包含一个字符串和一个整数，表示一次询问。

字符串中只包含小写字母，且长度均不超过 10。

输出格式
输出共 m 行，每行输出一个整数作为结果，表示一次询问中满足条件的字符串个数。

数据范围
1≤n,m≤1000,

输入样例：
3 2
abc
acd
bcd
ab 1
acbd 2
输出样例：
1
3
"""
""" 题解：
编辑距离的应用，动态转移方程的考虑增、删、改(改/不动)四种情况
3 2
abc
acd
bcd
ab 1
acbd 2
输出样例：
1
3
"""


def get_opt_num(a, b, l):
    f = [[0]*(len(b)+1) for _ in range((len(a)+1))]
    for i in range(len(a)):
        f[i][0] = i
    for i in range(len(b)):
        f[0][i] = i

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            f[i][j] = min(f[i-1][j]+1, f[i][j-1]+1)
            if a[i] == b[j]:
                f[i][j] = min(f[i][j], f[i-1][j-1])
            else:
                f[i][j] = min(f[i][j], f[i-1][j-1]+1)

    if f[len(a)-1][len(b)-1] <= l:
        return 1
    else:
        return 0


def main():
    n, m = map(int, input().split())
    query = []
    for i in range(n):
        query.append(['0'] + list(input()))

    for i in range(m):
        s, _l = input().split(' ')
        s = ['0'] + list(s)
        l = int(_l)
        cnt = 0
        for j in range(n):
            cnt += get_opt_num(query[j], s, l)
        print(cnt)


main()
