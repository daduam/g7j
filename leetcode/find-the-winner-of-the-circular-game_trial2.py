class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque()
        last = -1
        for i in range(n):
            q.append(i+1)
        while q:
            for _ in range(k-1):
                q.append(q.popleft())
            last = q.popleft()
        return last