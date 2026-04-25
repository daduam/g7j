class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()        
        ans = -1
        lo, hi = 1, position[-1] - position[0]
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            last, placed = position[0], 1
            for i in range(1, len(position)):
                curpos = position[i]
                if curpos - last >= mid:
                    last = curpos
                    placed += 1
            if placed >= m:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans