class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))
        while left <= right:
            cursum = left ** 2 + right ** 2
            if cursum < c:
                left += 1
            elif cursum > c:
                right -= 1
            else:
                return True
        return False