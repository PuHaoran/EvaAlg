"""
剑指 Offer 28. 对称的二叉树
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
"""
""" 题解
题解一：先对树进行翻转，然后判断翻转后的树与原树是否对称。
题解二：直接运用递归求解，不是判断根节点的左右孩子，而是判断最左边的节点和最右边的节点是否相等。
            /  \
            L   R
            /\  /\ 
           L.L  R.R
"""
import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def curr(l, r):
            if not l and not r:
                return True
            if not l or not r or l.val != r.val:
                return False
            return curr(l.left, r.right) and curr(l.right, r.left)
        return curr(root.left, root.right)

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         def reverse_tree(root):
#             if not root:
#                 return
#             root.left, root.right = root.right, root.left
#             reverse_tree(root.left)
#             reverse_tree(root.right)
#         dup_root = copy.deepcopy(root)
#         reverse_tree(dup_root)
#
#         def is_same_tree(root, dup_root):
#             if not root and not dup_root:
#                 return True
#             if (not root and dup_root) or (root and not dup_root) or root.val != dup_root.val:
#                 return False
#             return is_same_tree(root.left, dup_root.left) and is_same_tree(root.right, dup_root.right)
#         return is_same_tree(root, dup_root)


