"""
剑指 Offer 40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。



示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
"""
""" 题解：
堆排序，构建一个1-n的数组，然后从n//2（最后一个分支节点）进行down操作，判断当前节点与孩子节点大小并交换(若交换则继续down)。
"""


class Solution:
    def getLeastNumbers(self, arr, k: int):
        global n
        n = len(arr)
        h = [0] + arr

        def down(i):
            t = i
            if i*2 <= n and h[i*2] < h[t]:
                t = i*2
            if i*2+1 <= n and h[i*2+1] < h[t]:
                t = i*2+1
            if t != i:
                h[i], h[t] = h[t], h[i]
                down(t)

        for i in range(n//2, 0, -1):
            down(i)

        res = []
        for _ in range(k):
            res.append(h[1])
            h[1], h[n] = h[n], h[1]
            n -= 1
            down(1)
        return res


arr = [0,0,0,1,2,2,3,7,6,1]
k = 3
solution = Solution()
print(solution.getLeastNumbers(arr, k))


