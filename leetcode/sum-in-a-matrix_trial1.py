class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        ans = 0
        for j in range(len(nums[0])):
            curmax = 0
            for i in range(len(nums)):
                curmax = max(curmax, nums[i][j])
            ans += curmax
        return ans
