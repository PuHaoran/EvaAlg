"""
给定一个整数 n，将数字 1∼n 排成一排，将会有很多种排列方法。

现在，请你按照字典序将所有的排列方法输出。

输入格式
共一行，包含一个整数 n。

输出格式
按字典序输出所有排列方案，每个方案占一行。

数据范围
1≤n≤7
输入样例：
3
输出样例：
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""
""" 题解：
① DFS分为枚举和回溯过程。
3
输出样例：
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""


def dfs(u):
    if u == n:
        print(' '.join([str(i) for i in path]))
        return
    for i in range(n):
        if not mark[i]:
            path[u] = i+1
            mark[i] = 1
            dfs(u+1)
            mark[i] = 0


def main():
    global n, path, mark
    n = int(input())
    mark = [0] * n
    path = [0] * n
    dfs(0)


main()
