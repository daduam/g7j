class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        # Find the index / point at which the height drops off from
        # the current height, that is, all heights in the half open
        # range from (found_idx, right] are gte heights[right]
        idx_stack = []
        starts_at = [-1] * n
        for right in range(len(heights)):
            while idx_stack and heights[right] < heights[idx_stack[-1]]:
                idx_stack.pop()
            starts_at[right] = idx_stack[-1] if idx_stack else -1
            idx_stack.append(right)
            
        # Find the index / point at which the height drops off from
        # the current height, that is, all heights in the half open
        # range from [left, found_idx) are gte heights[left]
        idx_stack.clear()
        ends_at = [n] * n
        for left in range(len(heights)-1, -1, -1):
            while idx_stack and heights[idx_stack[-1]] >= heights[left]:
                idx_stack.pop()
            ends_at[left] = idx_stack[-1] if idx_stack else n
            idx_stack.append(left)
            
        # Now the width of the full open range (starts_at, ends_at) becomes
        # the maxw of the range with heights gte heigts[i]. Maximize area
        # across all heights
        ans = 0
        for i in range(n):
            interval_minh = heights[i]
            interval_maxw = ends_at[i] - starts_at[i] - 1
            ans = max(ans, interval_maxw * interval_minh)
        return ans