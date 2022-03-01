"""
给定一个m x n 二维字符网格board 和一个字符串单词word 。如果word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

"""
""" 题解
dfs函数传入u作为递归终止条件，数组mark记录走过的路径并回溯，使用剪枝提前终止递归。
当需要判断True/False时，考虑res = dfs() and/or dfs()。
A B C E
S F C S
A D E E

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
"""


class Solution:
    def exist(self, board, word):
        if len(board) == 0:
            return False
        m, n = len(board), len(board[0])
        mark = [[0] * n for _ in range(m)]
        word_len = len(word)

        def dfs(u, i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[u] or mark[i][j]:
                return False
            if u == word_len - 1:
                return True
            mark[i][j] = 1
            res = dfs(u + 1, i - 1, j) or dfs(u + 1, i + 1, j) or dfs(u + 1, i, j - 1) or dfs(u + 1, i, j + 1)
            mark[i][j] = 0
            return res

        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True
        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
solution = Solution()
print(solution.exist(board=board, word=word))