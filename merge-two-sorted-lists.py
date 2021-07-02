# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        p, q = l1, l2
        head, tail = None, None
        while p and q:
            if p.val <= q.val:
                if tail:
                    tail.next = p
                    tail = p
                if not head:
                    head, tail = p, p
                p = p.next
            else:
                if tail:
                    tail.next = q
                    tail = q
                if not head:
                    head, tail = q, q
                q = q.next
            if p:
                tail.next = p
            elif q:
                tail.next = q
        return head
