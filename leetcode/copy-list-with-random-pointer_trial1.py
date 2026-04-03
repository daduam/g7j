"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = ListNode(-1)
        node2copy = dict()
        cur = head
        while cur:
            node = Node(cur.val)
            node2copy[cur] = node
            cur = cur.next
            
        cur = head
        dummy.next = ncur = node2copy[cur]
        while cur:
            if cur.next:
                ncur.next = node2copy[cur.next]
            ncur = ncur.next
            cur = cur.next
        
        cur, ncur = head, dummy.next
        while cur:
            if cur.random:
                ncur.random = node2copy[cur.random]
            ncur = ncur.next
            cur = cur.next
            
        return dummy.next