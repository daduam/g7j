# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz, cur = 0, head
        while cur:
            sz += 1
            cur = cur.next
        if n > sz:
            return head
        dummy = prev = ListNode(-1, head)
        for i in range(sz - n):
            prev = prev.next
        if prev and prev.next:
            prev.next = prev.next.next
        return dummy.next
