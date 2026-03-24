class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        uniqcnt, runsum = 0, 0
        for num in nums[:k]:
            runsum += num
            if freq[num] == 0:
                uniqcnt += 1
            freq[num] += 1
        ans, left = 0, 0
        if uniqcnt == k:
            ans = runsum
        for right in range(k, len(nums)):
            runsum += nums[right] - nums[left]
            if freq[nums[right]] == 0:
                uniqcnt += 1
            freq[nums[right]] += 1
            if freq[nums[left]] == 1:
                uniqcnt -= 1
            freq[nums[left]] -= 1
            if uniqcnt == k:
                ans = max(ans, runsum)
            left += 1
        return ans
        