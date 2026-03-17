class NumArray:

    def __init__(self, nums: List[int]):
        self.psum = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            self.psum[i] = self.psum[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.psum[right]
        return self.psum[right] - self.psum[left-1]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)