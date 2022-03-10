"""
剑指 Offer 57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。



示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
"""
""" 题解
法一：前缀和，然后找到所有两数相减等于target的区间。
0 1 2 3 4   5   6   7   8   9
0 1 3 6 10  15  21  28  36  45
法二：滑动窗口，i、j分别指向第一个和第二个位置。
0 1 2 3 4 5 6 7 8 9 
  i j  1+2<9,j++
0 1 2 3 4 5 6 7 8 9  
  i   j  1+2+3<9,j++
0 1 2 3 4 5 6 7 8 9  
  i     j  1+2+3+4>9,i++
0 1 2 3 4 5 6 7 8 9  
    i   j  2+3+4==9,保存,i++,j++
...
"""


class Solution:
    def findContinuousSequence(self, target: int):
        res = []
        f = [0] * target
        for i in range(target):
            f[i] = f[i-1] + i
        d = {}
        for i in range(len(f)):
            d[f[i]] = i
            if f[i] - target in d:
                res.append(list(range(d[f[i]-target]+1, i+1)))
        return res


target = 15
solution = Solution()
print(solution.findContinuousSequence(target))
