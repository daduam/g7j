# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        k = n // 2
        sums = [0] * k
        cur = head
        for i in range(k):
            sums[i] += cur.val
            cur = cur.next
        for i in range(k):
            sums[k-1-i] += cur.val
            cur = cur.next
        print(sums)
        return max(sums)