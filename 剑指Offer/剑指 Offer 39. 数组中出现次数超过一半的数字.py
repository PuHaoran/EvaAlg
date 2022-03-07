"""
剑指 Offer 39. 数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。



你可以假设数组是非空的，并且给定的数组总是存在多数元素。



示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
"""
""" 题解
先排序，然后去掉任意两个不相等的数据，最后剩下的就是众数。
"""


class Solution:
    def majorityElement(self, nums):
        nums = sorted(nums)
        mark = [0]*len(nums)
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] != nums[j]:
                mark[i] = 1
                mark[j] = 1
            i += 1
            j -= 1

        for i in range(len(nums)):
            if not mark[i]:
                return nums[i]


nums = [1, 2, 2, 2, 2, 5, 4, 2]
solution = Solution()
print(solution.majorityElement(nums))

