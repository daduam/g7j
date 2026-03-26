class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        freq = Counter()
        ans = nleft = fleft = uniqcnt = 0
        for right in range(len(nums)):
            if freq[nums[right]] == 0:
                uniqcnt += 1
            freq[nums[right]] += 1
            while uniqcnt > k:
                freq[nums[nleft]] -= 1
                if freq[nums[nleft]] == 0:
                    uniqcnt -= 1
                nleft += 1
                fleft = nleft
            while freq[nums[nleft]] > 1:
                freq[nums[nleft]] -= 1
                nleft += 1
            if uniqcnt == k:
                ans += nleft - fleft + 1
        return ans
        