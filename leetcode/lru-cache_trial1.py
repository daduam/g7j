class ListNode:
    
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2node = dict()
        self.dhead = ListNode(-1, -1)
        self.dtail = ListNode(-1, -1)
        self.dhead.next = self.dtail
        self.dtail.prev = self.dhead

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1        
        node = self.key2node[key]
        self.remove(node)
        self.insert_start(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key2node:
            self.remove(self.key2node[key])
            del self.key2node[key]
            
        if self.capacity == len(self.key2node):
            lru = self.dtail.prev
            del self.key2node[lru.key]
            self.remove(lru)

        node = ListNode(key, value)
        self.key2node[key] = node
        self.insert_start(node)
    
    def insert_start(self, node):
        node.prev = self.dhead
        node.next = self.dhead.next
        self.dhead.next.prev = node
        self.dhead.next = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)