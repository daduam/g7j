# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lhead = ltail = ListNode(-1)
        rhead = rtail = ListNode(-1)
        cur = head
        while cur:
            if cur.val < x:
                ltail.next = cur
                ltail = ltail.next
            else:
                rtail.next = cur
                rtail = rtail.next
            cur = cur.next
        ltail.next = rhead.next
        rtail.next = None
        return lhead.next