class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        snums = sorted(set(nums), reverse=True)
        return snums[2] if len(snums) >= 3 else snums[0]
        