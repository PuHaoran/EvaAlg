"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。



示例 1:

输入: [0,1,3]
输出: 2
示例2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
"""
""" 题解
二分，找到满足nums[i] != i的右区间端点
"""


class Solution:
    def missingNumber(self, nums):
        def bin_search(l, r):
            if l >= r:
                if l == nums[-1]:
                    return l+1
                return l

            x = (l+r) // 2
            if nums[x] != x:
                r = x
            else:
                l = x + 1
            return bin_search(l, r)
        return bin_search(0, len(nums)-1)


nums = [0, 1, 3]
solution = Solution()
print(solution.missingNumber(nums))
