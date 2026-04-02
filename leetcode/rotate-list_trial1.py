# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n, cur = 1, head
        while cur.next:
            n += 1
            cur = cur.next
        if k % n == 0:
            return head
        nk = n - (k % n)
        dummy = prev = ListNode(-1, head)
        cur = dummy.next
        for _ in range(nk):
            prev = cur
            cur = cur.next
        nhead = cur
        prev.next = None
        while cur and cur.next:
            cur = cur.next
        cur.next = dummy.next
        return nhead