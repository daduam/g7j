class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse_range(nums, 0, len(nums)-1)
        self.reverse_range(nums, 0, k-1)
        self.reverse_range(nums, k, len(nums)-1)
        
    def reverse_range(self, nums, left, right):
        if not (0 <= left < len(nums) or 0 <= right < len(nums)):
            return
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1