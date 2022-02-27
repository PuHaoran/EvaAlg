"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target=5 true
traget=20 false
"""
""" 题解
利用矩阵单调性解题，左上角的元素一定是对应列的最小值，一定是对应行的最大值，通过该特性可以不断缩小搜索范围。
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target=5 true
traget=20 false
"""


class Solution:
    def findNumberIn2DArray(self, matrix, target):
        if len(matrix) == 0:
            return False
        n, m = len(matrix), len(matrix[0])
        row, col = 0, m-1
        while col >= 0 and row < n:
            t = matrix[row][col]
            if t == target:
                return True
            elif t > target:
                col -= 1
            elif t < target:
                row += 1
        return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 20
solution = Solution()
print(solution.findNumberIn2DArray(matrix, target))
