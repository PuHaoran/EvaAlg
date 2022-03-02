"""
剑指 Offer 13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20
"""
""" 题解
// 初始化队列
while q.qsize():
    t = q.get()
    // 扩展t，入队列
0 0
0 0
0 0

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
"""
from queue import Queue


class Solution:
    def movingCount(self, m: int, n: int, k: int):
        def get_digit_sum(a):
            s = 0
            while a:
                s += a % 10
                a //= 10
            return s

        def bfs(q, mark, res, m, n, k):
            dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
            while q.qsize():
                t = q.get()
                for i in range(4):
                    x, y = t[0] + dx[i], t[1] + dy[i]
                    if x >= 0 and x < m and y >= 0 and y < n and get_digit_sum(x) + get_digit_sum(y) <= k and not mark[x][y]:
                        res += 1
                        q.put((x, y))
                        mark[x][y] = 1
            return res

        mark = [[0]*n for _ in range(m)]
        mark[0][0] = 1
        q = Queue()
        q.put((0, 0))
        res = bfs(q, mark, 1, m, n, k)
        return res


m, n, k = 1, 2, 0
solution = Solution()
print(solution.movingCount(m, n, k))
