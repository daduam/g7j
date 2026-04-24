class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        
        ans = -float('inf')
        for house in houses:
            found = bisect.bisect_left(heaters, house) 
            radius = float('inf')
            if 0 <= found < len(heaters):
                radius = min(radius, abs(house - heaters[found]))
            if 0 <= found - 1 < len(heaters):
                radius = min(radius, abs(house - heaters[found-1]))
            ans = max(ans, radius)
        
        return ans