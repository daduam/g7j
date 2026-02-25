class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        piles.sort(reverse=True)
        print(piles)
        i = 1
        while i < len(piles) - (len(piles) / 3):
            ans += piles[i]
            i += 2
        return ans
        