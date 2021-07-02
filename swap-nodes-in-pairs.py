# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        if not head:
            return None
        if head.next is None:
            return head

        index = 0
        p = head

        left = None
        while p:
            right = p.next

            if index % 2 == 0 and right:
                if left is None:
                    p.next = right.next
                    right.next = p
                    head = right

                else:
                    left.next = right
                    p.next = right.next
                    right.next = p

                left = right

            # left = p
            # p = p.next
            # index += 1

            else:
                left = p
                p = p.next

            index += 1

        return head
