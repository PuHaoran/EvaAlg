"""
剑指 Offer 33. 二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。



参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
"""
""" 题解
[1,3,2,6,5]
找到第一个大于根节点的值，若i==r，说明没问题。
1 3 2    6 5
二叉搜索树的左子树都比最后一个节点(根节点)小，右子树都比根节点大；满足当前条件 & 左子树 & 右子树。
"""


class Solution:
    def verifyPostorder(self, postorder):
        def recur(arr, l, r):
            if l >= r:
                return True
            i = l
            while arr[i] < arr[r]:
                i += 1
            m = i
            while arr[i] > arr[r]:
                i += 1
            return i == r and recur(arr, l, m-1) and recur(arr, m, r-1)
        return recur(postorder, 0, len(postorder)-1)


postorder = [1,3,2,6,5]
solution = Solution()
print(solution.verifyPostorder(postorder))