"""
给定一个包含 n 个点（编号为 1∼n）的无向图，初始时图中没有边。

现在要进行 m 个操作，操作共有三种：

C a b，在点 a 和点 b 之间连一条边，a 和 b 可能相等；
Q1 a b，询问点 a 和点 b 是否在同一个连通块中，a 和 b 可能相等；
Q2 a，询问点 a 所在连通块中点的数量；
输入格式
第一行输入整数 n 和 m。

接下来 m 行，每行包含一个操作指令，指令为 C a b，Q1 a b 或 Q2 a 中的一种。

输出格式
对于每个询问指令 Q1 a b，如果 a 和 b 在同一个连通块中，则输出 Yes，否则输出 No。

对于每个询问指令 Q2 a，输出一个整数表示点 a 所在连通块中点的数量

每个结果占一行。

数据范围
1≤n,m≤105
输入样例：
5 5
C 1 2
Q1 1 2
Q2 1
C 2 5
Q2 5
输出样例：
Yes
2
3
"""
"""
题解： 并查集
用一棵树表示集合，用数组存储当前节点的父节点(路径)，集合的合并等同根节点的合并，查找是否同一集合等同根节点是否相等。
"""
N = 100010
pre = [i for i in range(N)]
cnt = [1 for i in range(N)]


def find(m):
    if pre[m] != m:
        pre[m] = find(pre[m])
    return pre[m]


def main():
    n, m = map(int, input().split())
    for _ in range(m):
        row = input().split()
        if row[0] == 'C':
            a, b = int(row[1]), int(row[2])
            a_root, b_root = find(a), find(b)
            if a_root != b_root:
                cnt[a_root] += cnt[b_root]
            pre[find(b)] = find(a)

        elif row[0] == 'Q1':
            a, b = int(row[1]), int(row[2])
            if find(a) == find(b):
                print('Yes')
            else:
                print('No')
        elif row[0] == 'Q2':
            a = int(row[1])
            print(cnt[find(a)])


main()
