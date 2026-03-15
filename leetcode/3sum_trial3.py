class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            num = nums[i]
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            left, right = i+1, len(nums) - 1
            while left < right:
                cursum = num + nums[left] + nums[right]
                if cursum < 0:
                    left += 1
                elif cursum > 0:
                    right -= 1
                else:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
        return ans
        