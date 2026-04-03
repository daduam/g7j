# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(-1)
        carry = 0
        while l1 or l2:
            cursum = carry
            cursum += l1.val if l1 else 0
            cursum += l2.val if l2 else 0
            carry = cursum // 10
            cursum = cursum % 10
            prev.next = ListNode(cursum)
            prev = prev.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        prev.next = ListNode(carry) if carry > 0 else None
        return dummy.next