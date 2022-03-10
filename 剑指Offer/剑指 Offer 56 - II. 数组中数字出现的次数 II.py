"""
剑指 Offer 56 - II. 数组中数字出现的次数 II
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。



示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1
"""
""" 题解
011
100
011
011
=>
133对应位%3=100，得出多余的数为2。
a二进制的第31位：a>>31 & 1
"""


class Solution:
    def singleNumber(self, nums) -> int:
        s = 0
        for i in range(31, -1, -1):
            t = 0
            for j in range(len(nums)):
                t += nums[j] >> i & 1
            s = s*2 + t % 3
        return s


nums =  [9,1,7,9,7,9,7]
solution = Solution()
print(solution.singleNumber(nums))
