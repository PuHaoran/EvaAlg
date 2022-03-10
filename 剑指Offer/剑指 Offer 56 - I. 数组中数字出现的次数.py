"""
剑指 Offer 56 - I. 数组中数字出现的次数
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。



示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
"""
""" 题解
先将数组所有元素异或，得到x & y，然后找到x & y的lowbit（最低位为1的数）。然后将根据这个数将数据分为二组，一组与lowbit数在对应位上相等，一组不相等，这两组数异或之后剩下的就是x,y。
"""


class Solution:
    def singleNumbers(self, nums):
        xy = 0
        for num in nums:
            xy = xy ^ num
        lowbit = xy & -xy
        a, b = 0, 0
        for num in nums:
            if num & lowbit:
                a ^= num
            else:
                b ^= num
        return [a, b]


nums = [4,1,4,6]
solution = Solution()
print(solution.singleNumbers(nums))
