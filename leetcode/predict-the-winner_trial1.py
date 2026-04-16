class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        return self.predictTheWinnerHelper(nums, 0, len(nums) - 1) >= 0

    def predictTheWinnerHelper(self, nums, left, right) -> int:
        if left == right:
            return nums[left]
        pickleft = nums[left] - self.predictTheWinnerHelper(nums, left + 1, right)
        pickright = nums[right] - self.predictTheWinnerHelper(nums, left, right - 1)
        return max(pickleft, pickright)