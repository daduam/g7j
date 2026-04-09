class Solution:
    def firstUniqChar(self, s: str) -> int:
        order = deque()
        count = defaultdict(int)
        for i in range(len(s)):
            ch = s[i]
            count[ch] += 1
            if count[ch] == 1:
                order.append(i)
        
        while order:
            if count[s[order[0]]] == 1:
                return order[0]
            order.popleft()
        
        return -1