class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem2idx = dict([(0, -1)])
        runsum = 0
        for i in range(len(nums)):
            runsum += nums[i]
            currem = runsum % k
            if currem not in rem2idx:
                rem2idx[currem] = i
            elif i - rem2idx[currem] >= 2:
                return True
        return False