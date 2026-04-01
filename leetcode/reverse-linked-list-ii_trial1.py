# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = prev = ListNode(-1, head)
        for i in range(left-1):
            prev = prev.next
        rhead = prev.next
        for i in range(right-left):
            rest = rhead.next
            rhead.next = rest.next
            rest.next = prev.next
            prev.next = rest
        return dummy.next
