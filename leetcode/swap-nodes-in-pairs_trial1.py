# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(-1, head)
        while prev and prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
        return dummy.next