# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans, cur = None, head
        while cur:
            rest = cur.next
            cur.next = ans
            ans = cur
            cur = rest
        return ans