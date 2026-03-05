class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        holder = 0
        seeker = 0
        while seeker < len(nums):
            if nums[seeker] != nums[holder]:
                nums[holder + 1] = nums[seeker]
                holder += 1
            seeker += 1
        return holder + 1 
        