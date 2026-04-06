# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow =  fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            rest = slow.next
            slow.next = prev
            prev = slow
            slow = rest
        ans = 0
        chead = head
        rhead = prev
        while chead and rhead:
            ans = max(ans, chead.val + rhead.val)
            chead = chead.next
            rhead = rhead.next
        return ans