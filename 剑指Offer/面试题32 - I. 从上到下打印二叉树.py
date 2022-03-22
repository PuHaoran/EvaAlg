"""
面试题32 - I. 从上到下打印二叉树
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。



例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
"""
""" 题解
BFS，初始化队列，while q.qsize():t=q.get(),扩展t。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        from queue import Queue
        q = Queue()
        q.put(root)
        res = []
        while q.qsize():
            t = q.get()
            res.append(t.val)
            if t.left:
                q.put(t.left)
            if t.right:
                q.put(t.right)
        return res
