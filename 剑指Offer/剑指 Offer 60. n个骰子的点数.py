"""
剑指 Offer 60. n个骰子的点数
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。



你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。



示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
"""
""" 题解
①状态表达。f(i)点数集合i出现的概率。
②状态转移。t=[0, 1.0/6,...], temp(i+j)+=f(i)*arr(j) f=temp。
"""


class Solution:
    def dicesProbability(self, n: int):
        arr = [0, 1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6]
        f = [0, 1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6]
        for i in range(1, n):
            temp = [0] * (6*n+1)
            for j in range(i, i*6+1):
                for k in range(1, 7):
                    temp[j+k] += f[j] * arr[k]
            f = temp
        return f[n:]


n = 5
solution = Solution()
print(solution.dicesProbability(n))
