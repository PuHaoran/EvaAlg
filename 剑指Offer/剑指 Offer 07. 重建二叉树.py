"""
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

示例 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
示例 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""
""" 题解
用四个变量代表当前前序遍历和中序遍历的元素区间，先通过前序确定根节点，然后中序确定左右子树，递归操作。
root = new TreeNode(根)
root.left = build(前左，中左)
root.right = build(前右，中右)

 3 9 20 15 7
 pl        pr
 9 3 15 20 7
 il        ir
  idx

# 左子树前序、中序
#pl+1  pl+idx-il        il idx-1
# 右子树前序、中序
#pr-(ir-idx-1)  pr            idx+1 ir

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
示例 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        def build(preorder, inorder, pl, pr, il, ir):
            if pl > pr or il > ir:
                return None
            root_value = preorder[pl]
            root = TreeNode(root_value)
            idx = inorder_dict[root_value]

            # 左子树的前序左右索引、中序左右索引
            root.left = build(preorder,
                              inorder,
                              pl + 1,
                              pl + idx - il,
                              il,
                              idx - 1)
            root.right = build(preorder,
                               inorder,
                               pr - (ir - idx - 1),
                               pr,
                               idx + 1,
                               ir)
            return root

        inorder_dict = {}
        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i
        return build(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)
