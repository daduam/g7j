class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans, left, runsum = 0, 0, 0
        freq = defaultdict(int)
        for right in range(len(nums)):
            num = nums[right]
            freq[num] += 1
            runsum += num
            while freq[num] > 1:
                lnum = nums[left]
                freq[lnum] -= 1
                runsum -= lnum
                left += 1
            ans = max(ans, runsum)
        return ans
        