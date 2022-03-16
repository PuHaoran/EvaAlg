"""
剑指 Offer 61. 扑克牌中的顺子
从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。



示例 1:

输入: [1,2,3,4,5]
输出: True


示例 2:

输入: [0,0,1,2,5]
输出: True
"""
""" 题解
去掉0之后，判断是否重复，是否最大值-最小值<=4。
"""


class Solution:
    def isStraight(self, nums) -> bool:
        nums = sorted([i for i in nums if i != 0])
        for i in range(1, len(nums)):
            t = nums[i] - nums[i-1]
            if t == 0:
                return False
        if max(nums) - min(nums) <= 4:
            return True
        return False
