class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        nums.sort()
        for i in range(n-1):
            if nums[i] != nums[i+1]:
                ans += n - i - 1
        return ans
