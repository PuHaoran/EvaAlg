"""
剑指 Offer 24. 反转链表
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
""" 题解
p为首节点，q为空节点；遍历p的同时保存p_next=p.next，并将p节点作为q的首节点p.next=q，然后更新p和q。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p, q = head, None
        while p:
            p_next = p.next
            p.next = q
            q = p
            p = p_next
        return q
