# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k) -> ListNode:
        if not head:
            return None
        if k == 1:
            return head
        p = head
        left = None
        index = 0
        s = [None for _ in range(k)]
        while p:
            if index % k == 0:
                q = p
                count = 0
                while count < k and q:
                    s[count] = q
                    count += 1
                    q = q.next
                if count < k:
                    break
                right = q
                sub_head = s[k-1]
                r = sub_head
                count -= 2
                while count >= 0:
                    r.next = s[count]
                    r = s[count]
                    count -= 1
                sub_tail = s[0]
                if left is None:
                    head = sub_head
                else:
                    left.next = sub_head
                sub_tail.next = right

                left = sub_tail

                p = sub_tail.next
                index += k
            else:
                left = p
                p = p.next
                index += 1
        return head
