class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()        
        ans, bestdiff, n = float('inf'), float('inf'), len(nums)
        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                cursum = nums[i] + nums[left] + nums[right]
                curdiff = abs(cursum - target)
                if curdiff < bestdiff:
                    ans = cursum
                    bestdiff = curdiff
                if cursum < target:
                    left += 1
                else:
                    right -= 1
        return ans