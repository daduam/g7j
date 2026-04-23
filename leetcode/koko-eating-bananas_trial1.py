class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k: int) -> bool:
            curh = 0
            for pile in piles:
                curh += (pile // k) + int(pile % k != 0)
            return curh <= h
        
        lo, hi = 1, max(piles)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo