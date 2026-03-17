class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        psum = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            psum[i] = psum[i-1] + nums[i]
        return psum
        