class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[holder] = nums[holder], nums[i]        
                holder += 1
