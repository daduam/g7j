class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        st = []
        for i in range(n):
            if not st or nums[st[-1]] > nums[i]:
                st.append(i)
        for i in range(n-1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                ans = max(ans, i - st.pop())     
        return ans