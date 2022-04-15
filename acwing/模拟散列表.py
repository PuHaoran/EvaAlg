"""
维护一个集合，支持如下几种操作：

I x，插入一个数 x；
Q x，询问数 x 是否在集合中出现过；
现在要进行 N 次操作，对于每个询问操作输出对应的结果。

输入格式
第一行包含整数 N，表示操作数量。

接下来 N 行，每行包含一个操作指令，操作指令为 I x，Q x 中的一种。

输出格式
对于每个询问指令 Q x，输出一个询问结果，如果 x 在集合中出现过，则输出 Yes，否则输出 No。

每个结果占一行。

数据范围
1≤N≤105
−109≤x≤109
输入样例：
5
I 1
I 2
I 3
Q 2
Q 5
输出样例：
Yes
No
"""
""" 题解
哈希表
通过hash函数将10^9映射到10^5，可能出现若干不同的数映射一个相同的数（冲突），根据应对冲突方式的不同分为：
1）开放寻址法
2）拉链法
h(11) = 3 h(13) = 3 h(9) = 7
0 1 2 3 4 5 6 7 8 9 10 (存储链首节点对应的索引)
      11      9
      \|/    \|/
      13     -1
      \|/
      -1
链的长度可以看做常数，哈希表的时间复杂度为O(1)。
5
I 1
I 2
I 3
Q 2
Q 5
输出样例：
Yes
No
"""
# 模取大于十万的第一个质数
M = 10003
N = 100010
e, ne = [0] * N, [-1] * N
h = [-1] * N
idx = 0


def insert(m):
    """ 当前数值取模之后，存储一条链 """
    global idx, h
    k = (m % M + M) % M
    # 新建一个节点
    e[idx] = m
    # 当前节点指向拉练的最后一个节点
    ne[idx] = h[k]
    # 新建的节点作为最后一个节点
    h[k] = idx
    idx += 1


def find(m):
    global idx, h
    k = (m % M + M) % M
    p = h[k]
    while p != -1:
        if e[p] == m:
            return 1
        p = ne[p]
    return 0


def main():
    n = int(input())
    for i in range(n):
        row = input().split()
        if row[0] == 'I':
            insert(int(row[1]))
        elif row[0] == 'Q':
            if find(int(row[1])):
                print("Yes")
            else:
                print("No")


main()

