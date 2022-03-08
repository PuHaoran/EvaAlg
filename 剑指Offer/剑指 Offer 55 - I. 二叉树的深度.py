"""
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度3 。
"""
""" 题解
BFS，初始化队列q，while q.qsize(): for q.size(): t=q.get()，扩展t。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        from queue import Queue
        q = Queue()
        q.put(root)
        depth = 0
        while q.qsize():
            for i in range(q.qsize()):
                t = q.get()
                if t.left:
                    q.put(t.left)
                if t.right:
                    q.put(t.right)
            depth += 1
        return depth
