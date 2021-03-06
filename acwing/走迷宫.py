"""
给定一个 n×m 的二维整数数组，用来表示一个迷宫，数组中只包含 0 或 1，其中 0 表示可以走的路，1 表示不可通过的墙壁。

最初，有一个人位于左上角 (1,1) 处，已知该人每次可以向上、下、左、右任意一个方向移动一个位置。

请问，该人从左上角移动至右下角 (n,m) 处，至少需要移动多少次。

数据保证 (1,1) 处和 (n,m) 处的数字为 0，且一定至少存在一条通路。

输入格式
第一行包含两个整数 n 和 m。

接下来 n 行，每行包含 m 个整数（0 或 1），表示完整的二维数组迷宫。

输出格式
输出一个整数，表示从左上角移动至右下角的最少移动次数。

数据范围
1≤n,m≤100
输入样例：
5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0
输出样例：
8
"""
""" 题解
初始化队列q
while 队列q不为空:
    t = q.get()
    扩展t，入队列

5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0
输出样例：
8
"""
from queue import Queue


def bfs():
    x, y = 0, 0
    # 上下左右
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    q = Queue()
    q.put((x, y))
    mark[0][0] = 0
    while (q.qsize()):
        t = q.get()
        for i in range(4):
            x, y = t[0] + dx[i], t[1] + dy[i]
            if x>=0 and x<n and y>=0 and y<m and mark[x][y] == -1 and arr[x][y] == 0:
                print(x, y)
                mark[x][y] = mark[t[0]][t[1]] + 1
                q.put((x, y))
    return mark[n-1][m-1]


def main():
    global m, n, p, arr, mark, queue
    n, m = map(int, input().split())
    arr, queue = [], []
    for i in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
    mark = [[-1]*m for _ in range(n)]
    print(bfs())


main()
