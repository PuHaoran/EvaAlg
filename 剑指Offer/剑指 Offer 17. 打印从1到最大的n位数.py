"""
剑指 Offer 17. 打印从1到最大的n位数
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
"""
"""
法一：输出比10**n小的数字列表。
法二：利用DFS对数字进行全排列，dfs输入u步数作为递归终止条件，mark数组标记走过的路径，path存储路径。
"""
# class Solution:
#     def printNumbers(self, n: int):
#         return list(range(1, 10**n))

class Solution:
    def printNumbers(self, n: int):
        res = []
        def dfs(u):
            if u == n:
                res.append(int(''.join(path)))
                return
            for i in range(10):
                if not mark[u][i]:
                    mark[u][i] = 1
                    path[u] = str(i)
                    dfs(u+1)
                    mark[u][i] = 0

        mark = [[0] * 10 for _ in range(n)]
        path = [0] * n
        dfs(0)
        return res[1:]

solution = Solution()
print(solution.printNumbers(1))