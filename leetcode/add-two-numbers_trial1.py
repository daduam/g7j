# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(-1)
        rem = 0
        while l1 and l2:
            cursum = l1.val + l2.val + rem
            rem = cursum // 10
            cursum = cursum % 10
            prev.next = ListNode(cursum)
            prev = prev.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            cursum = l1.val + rem
            rem = cursum // 10
            cursum = cursum % 10
            prev.next = ListNode(cursum)
            prev = prev.next
            l1 = l1.next
        while l2:
            cursum = l2.val + rem
            rem = cursum // 10
            cursum = cursum % 10
            prev.next = ListNode(cursum)
            prev = prev.next
            l2 = l2.next
        if rem > 0:
            prev.next = ListNode(rem)
        return dummy.next