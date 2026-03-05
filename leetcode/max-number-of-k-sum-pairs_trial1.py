class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        ans = 0
        for key in freq:
            if key == k - key:
                ans += freq[key] // 2
            else:
                ans += min(freq[key], freq[k - key])
                freq[key] = 0
        return ans
