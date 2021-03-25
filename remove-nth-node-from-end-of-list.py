# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None:
            return None
        p, q = head, head
        m = n
        while m > 0:
            p = p.next
            m -= 1
        if not p:
            return head.next
        while p.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        return head
