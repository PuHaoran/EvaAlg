"""
在一个 3×3 的网格中，1∼8 这 8 个数字和一个 x 恰好不重不漏地分布在这 3×3 的网格中。

例如：

1 2 3
x 4 6
7 5 8
在游戏过程中，可以把 x 与其上、下、左、右四个方向之一的数字交换（如果存在）。

我们的目的是通过交换，使得网格变为如下排列（称为正确排列）：

1 2 3
4 5 6
7 8 x
例如，示例中图形就可以通过让 x 先后与右、下、右三个方向的数字交换成功得到正确排列。

交换过程如下：

1 2 3   1 2 3   1 2 3   1 2 3
x 4 6   4 x 6   4 5 6   4 5 6
7 5 8   7 5 8   7 x 8   7 8 x
现在，给你一个初始网格，请你求出得到正确排列至少需要进行多少次交换。

输入格式
输入占一行，将 3×3 的初始网格描绘出来。

例如，如果初始网格如下所示：

1 2 3
x 4 6
7 5 8
则输入为：1 2 3 x 4 6 7 5 8

输出格式
输出占一行，包含一个整数，表示最少交换次数。

如果不存在解决方案，则输出 −1。

输入样例：
2  3  4  1  5  x  7  6  8
输出样例
19
"""
"""
2  3  4  1  5  x  7  6  8
输出样例
19
"""
from queue import Queue


def swap(s, i, j):
    l = list(s)
    l[i], l[j] = l[j], l[i]
    return ''.join(l)


def bfs(s):
    end = '12345678x'
    d = {}
    d[s] = 0
    q = Queue()
    q.put(s)
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    while q.qsize():
        t = q.get()
        if t == end:
            return d[t]
        # 状态转移
        k = t.find('x')
        kx, ky = k // 3, k % 3
        dist = d[t]
        for i in range(4):
            x, y = kx+dx[i], ky+dy[i]
            if x >= 0 and x < 3 and y >= 0 and y < 3:
                # 状态还原，交换位置
                t = swap(t, k, x*3+y)
                if t not in d:
                    d[t] = dist+1
                    q.put(t)
                # 回溯
                t = swap(t, k, x * 3 + y)
    return -1


def main():
    s = ''.join(input().split(' '))
    print(bfs(s))


main()
