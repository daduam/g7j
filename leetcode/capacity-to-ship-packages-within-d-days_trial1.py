class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(maxw: int) -> bool:
            curdays, cursum = 0, 0
            for w in weights:
                if cursum + w <= maxw:
                    cursum += w
                else:
                    curdays += 1
                    cursum = w
            curdays += int(cursum > 0)
            return curdays <= days

        lo, hi = max(weights), sum(weights)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        
        return lo