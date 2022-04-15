"""
在给定的 N 个整数 A1，A2……AN 中选出两个进行 xor（异或）运算，得到的结果最大是多少？

输入格式
第一行输入一个整数 N。

第二行输入 N 个整数 A1～AN。

输出格式
输出一个整数表示答案。

数据范围
1≤N≤105,
0≤Ai<231
输入样例：
3
1 2 3
输出样例：
3
"""
""" 题解
先写暴力写法O(n^2)，然后考虑使用Trie树来存储数组中的元素。
                   _
              /        \
             0         1
              \     /     \
              1    0       1
              /    /       /
             0    0        0
             \     \      /
             1(5)   1(9) 0(12)
异或，指二进制位不同为1，相同为0。
9  1001
5  0101
12 1100
假如总共4位(实际二进制有31位)；
对于5而言，找异或最大的元素即最高位为1，然后下一位为0，下下位0(没有1的路径)，下下位1故9异或值更大。
"""
N = 3000010
son = [[0] * 2 for _ in range(N)]
idx = 1


def insert(m):
    global idx
    p = 0
    for i in range(30, -1, -1):
        x = m >> i & 1
        if son[p][x] == 0:
            son[p][x] = idx
            idx += 1
        p = son[p][x]


def query(m):
    global idx
    res, p = 0, 0
    for i in range(30, -1, -1):
        x = m >> i & 1
        if son[p][int(not x)] != 0:
            res += 1 << i  # 2 ** i
            p = son[p][int(not x)]
        else:
            p = son[p][x]
    return res


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        insert(arr[i])

    res = 0
    for i in range(n):
        res = max(query(arr[i]), res)

    print(res)


main()

