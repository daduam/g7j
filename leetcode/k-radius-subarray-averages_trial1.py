class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n, runsum = len(nums), 0
        ans = [-1] * n
        for ptr in range(len(nums)):
            runsum += nums[ptr]
            if ptr < 2 * k:
                continue
            if ptr > 2 * k:
                runsum -= nums[ptr - (2 * k + 1)]
            ans[ptr - k] = runsum // (2 * k + 1)
        return ans
        