"""
一共有 n 个数，编号是 1∼n，最开始每个数各自在一个集合中。

现在要进行 m 个操作，操作共有两种：

M a b，将编号为 a 和 b 的两个数所在的集合合并，如果两个数已经在同一个集合中，则忽略这个操作；
Q a b，询问编号为 a 和 b 的两个数是否在同一个集合中；
输入格式
第一行输入整数 n 和 m。

接下来 m 行，每行包含一个操作指令，指令为 M a b 或 Q a b 中的一种。

输出格式
对于每个询问指令 Q a b，都要输出一个结果，如果 a 和 b 在同一集合内，则输出 Yes，否则输出 No。

每个结果占一行。

数据范围
1≤n,m≤105
输入样例：
4 5
M 1 2
M 3 4
Q 1 2
Q 1 3
Q 3 4
输出样例：
Yes
No
Yes
"""
""" 题解
1）将两个集合合并
2）询问两个元素是否在一个集合当中

并差集原理：每个集合通过一棵树来表示，树根编号是整个集合的编号，每个节点存储它的父节点。
查询：根节点编号一样，则两个元素在同一个集合中，否则不在同一集合。
合并：两个集合的编号分别为a,b，合并操作pre[b] = a。
"""

pre = [i for i in range(100010)]


def merge(a, b):
    pre[find(b)] = find(a)


def find(a):
    if pre[a] != a:
        pre[a] = find(pre[a])
    return pre[a]


def main():
    n, m = map(int, input().split())
    for _ in range(m):
        op, a, b = input().split()
        a, b = int(a), int(b)
        if op == 'M':
            merge(a, b)
        else:
            if find(a) == find(b):
                print('Yes')
            else:
                print('No')


main()
