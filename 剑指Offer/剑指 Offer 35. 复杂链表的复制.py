"""
剑指 Offer 35. 复杂链表的复制
剑指 Offer 35. 复杂链表的复制
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：

输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
"""
""" 题解
复制链表的各节点在原节点后面，则复制节点的random可以是当前节点random的下一个节点。
# 1->2->3->None
# |_____|
# 1->1->2->2->3->3->None
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node'):
        p = head
        while p:
            p_next = p.next
            q = Node(p.val)
            p.next = q
            q.next = p_next
            p = p_next
        p = head
        new_head = Node(-1)
        h = new_head
        while p:
            q = p.next
            pr = p.random
            q.random = pr.next
            h.next = q
            h = h.next
            p = q.next
        return h.next






