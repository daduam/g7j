class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        ans = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid * mid <= x:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans