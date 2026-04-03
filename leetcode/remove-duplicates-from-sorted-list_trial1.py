# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev, cur = head, head.next
        while cur:
            if prev.val != cur.val:
                prev = prev.next
            prev.next = cur.next
            cur = cur.next
        return head