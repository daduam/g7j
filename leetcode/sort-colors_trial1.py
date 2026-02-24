class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1):
            jmin = i
            for j in range(i+1, n):
                if nums[j] < nums[jmin]:
                    jmin = j
            if jmin != i:
                nums[i], nums[jmin] = nums[jmin], nums[i]
        