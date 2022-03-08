"""
剑指 Offer 53 - I. 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。



示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
"""
""" 题解
二分，找最左端索引和最右端索引，本质找右区间端点和左区间端点。
"""


class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums) == 0:
            return 0
        def lb_s(l, r, t):
            if l >= r:
                if nums[l] == t:
                    return l
                else:
                    return -1
            x = (l+r) // 2
            if nums[x] >= t:
                r = x
            else:
                l = x+1
            return lb_s(l, r, t)

        def rb_s(l, r, t):
            if l >= r:
                if nums[l] == t:
                    return l
                else:
                    return -1
            x = (l+r+1) // 2
            if nums[x] <= t:
                l = x
            else:
                r = x-1
            return rb_s(l, r, t)

        a, b = lb_s(0, len(nums) - 1, target), rb_s(0, len(nums)-1, target)
        if a == -1:
            return 0
        return b-a+1


nums = [5, 7, 7, 8, 8, 10]
target = 10
solution = Solution()
print(solution.search(nums, target))




