# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        r = [self.val]
        p = self.next
        while p:
            r.append(p.val)
            p = p.next
        return str(r)


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        lists = [l for l in lists if l]
        if not lists:
            return None
        head, tail = None, None
        while lists:
            min_index = 0
            for index, l in enumerate(lists):
                if l.val < lists[min_index].val:
                    min_index = index
            if not head:
                head, tail = lists[min_index], lists[min_index]
            else:
                tail.next = lists[min_index]
                tail = tail.next

            lists[min_index] = lists[min_index].next
            lists = [l for l in lists if l]
        return head


if __name__ == '__main__':
    print(Solution().mergeKLists([
        ListNode(1, next=ListNode(4, next=ListNode(5))),
        ListNode(1, next=ListNode(3, next=ListNode(4))),
        ListNode(2, next=ListNode(6)),
    ]))
