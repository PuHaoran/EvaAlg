"""
剑指 Offer 57. 和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
"""
""" 题解
法一：hash。
法二：前后双指针，相加后小于target，i++；否则，j--。
"""


class Solution:
    def twoSum(self, nums, target: int):
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
            if nums[i] + nums[j] > target:
                j -= 1
            if nums[i] + nums[j] < target:
                i += 1

# class Solution:
#     def twoSum(self, nums, target: int):
#         d = {}
#         for num in nums:
#             if target-num in d:
#                 return [target-num, num]
#             else:
#                 d[num] = 1
#         return [-1, -1]


nums = [10,26,30,31,47,60]
target = 40
solution = Solution()
print(solution.twoSum(nums, target))