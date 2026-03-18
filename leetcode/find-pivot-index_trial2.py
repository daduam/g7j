class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        psum = [0] * (n+1)
        for i in range(n):
            psum[i+1] = psum[i] + nums[i]
        for i in range(n):
            if psum[i] == psum[n] - psum[i+1]:
                return i
        return -1
        