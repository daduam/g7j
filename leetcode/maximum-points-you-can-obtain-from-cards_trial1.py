class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        psum = [0] * (n+1)
        for i in range(n):
            psum[i+1] = psum[i] + cardPoints[i]
        ans = 0
        for left in range(k+1):
            right = k - left
            total = psum[left] + psum[n] - psum[n - right]
            ans = max(ans, total)
        return ans
