"""
剑指 Offer 29. 顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。



示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
"""
""" 题解
四个while循环，分别为右、左、下、上，走下一步前先进行判断。
1  2  3  4
5  6  7  8
9 10 11  12
"""


class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        i, j, k = 0, -1, 0
        n, m = len(matrix), len(matrix[0])
        mark = [[0]*m for _ in range(n)]
        res = []
        while 1:
            if len(res) == n * m:
                return res
            while j+1>=0 and j+1<m and not mark[i][j+1]:
                j += 1
                mark[i][j] = 1
                res.append(matrix[i][j])
            while i+1>=0 and i+1<n and not mark[i+1][j]:
                i += 1
                mark[i][j] = 1
                res.append(matrix[i][j])
            while j-1>=0 and j-1<m and not mark[i][j-1]:
                j -= 1
                mark[i][j] = 1
                res.append(matrix[i][j])
            while i-1>=0 and i-1<n and not mark[i-1][j]:
                i -= 1
                mark[i][j] = 1
                res.append(matrix[i][j])


matrix = []
solution = Solution()
print(solution.spiralOrder(matrix))
