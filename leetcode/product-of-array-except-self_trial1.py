class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pmul = [1] * n
        for i in  range(1, n):
            pmul[i] = pmul[i-1] * nums[i-1]
        smul = [1] * n
        for i in range(n-2, -1, -1):
            smul[i] = smul[i+1] * nums[i+1]
        ans = [0] * n
        for i in range(n):
            ans[i] = pmul[i] * smul[i]
        return ans