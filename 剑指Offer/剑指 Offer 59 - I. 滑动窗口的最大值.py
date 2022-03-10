"""
剑指 Offer 59 - I. 滑动窗口的最大值
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""
""" 题解
维持一个单调递减的双端队列，每次遍历时，去掉队列中超出滑动窗口的元素，并保持队列单调递增（根据当前元素，右侧减少或直接增加）。
3 -1
3 -1 -3
5 
5 3
6
7
"""


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        queue = [0] * 100010
        p, q = -1, -1
        res = []
        for i in range(len(nums)):
            if queue[p+1] < i-k+1:
                p += 1
            while p != q and nums[i] > nums[queue[q]]:
                q -= 1
            q += 1
            queue[q] = i
            if i >= k-1:
                res.append(nums[queue[p+1]])
        return res


nums = [1,3,-1,-3,5,3,6,7]
k = 3
solution = Solution()
print(solution.maxSlidingWindow(nums, k))
