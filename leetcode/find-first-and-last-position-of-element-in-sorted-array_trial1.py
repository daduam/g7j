class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid - 1
                ans[0] = mid if nums[mid] == target else ans[0]
            else:
                lo = mid + 1

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] <= target:
                lo = mid + 1
                ans[1] = mid if nums[mid] == target else ans[1]
            else:
                hi = mid - 1

        return ans