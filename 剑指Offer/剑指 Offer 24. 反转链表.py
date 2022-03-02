"""
剑指 Offer 24. 反转链表
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
""" 题解
q和p指向第一个和第二个节点，然后先保存p_next节点并将p节点指向q节点，更新p节点为q，p_next节点为p，直到p节点指向空。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        q, p = head, head.next
        if p is None:
            return q
        q.next = None
        while p:
            p_next = p.next
            p.next = q
            q = p
            p = p_next
        return q