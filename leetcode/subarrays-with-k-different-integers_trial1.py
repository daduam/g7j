class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithAtMostKDistinct(nums, k) - self.subarraysWithAtMostKDistinct(nums, k-1)
    
    def subarraysWithAtMostKDistinct(self, nums: List[int], k: int) -> int:
        freq = Counter()
        ans, left = 0, 0
        for right in range(len(nums)):
            if freq[nums[right]] == 0:
                k -= 1
            freq[nums[right]] += 1
            while k < 0:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    k += 1
                left += 1
            ans += right - left + 1
        return ans
