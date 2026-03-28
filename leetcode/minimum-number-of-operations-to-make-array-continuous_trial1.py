class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        ans, right = n, 0
        for left in range(n):
            while right < len(nums) and nums[right] < nums[left] + n:
                right += 1
            ans = min(ans, n - right + left)
        return ans