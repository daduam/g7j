class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans, runcnt, n = 0, 0, len(nums)
        podd = [0] * (n + 1)
        podd[0] = 1
        for num in nums:
            runcnt += num & 1
            if runcnt - k >= 0:
                ans += podd[runcnt - k]
            podd[runcnt] += 1
        return ans
        