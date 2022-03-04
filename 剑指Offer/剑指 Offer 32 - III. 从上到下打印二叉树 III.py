"""
剑指 Offer 32 - III. 从上到下打印二叉树 III
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。



例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
"""
""" 题解
BFS实现层次遍历，输出时根据奇偶打印。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        from queue import Queue
        if not root:
            return []
        res = []
        q = Queue()
        q.put(root)
        while q.qsize():
            temp = []
            for _ in range(q.qsize()):
                t = q.get()
                temp.append(t.val)
                if t.left:
                    q.put(t.left)
                if t.right:
                    q.put(t.right)
            res.append(temp)
        return [res[i] if i % 2 else res[i][::-1] for i in range(len(res))]
