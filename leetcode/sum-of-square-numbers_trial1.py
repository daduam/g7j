class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrts = set()
        for i in range(int(sqrt(c)) + 1):
            sqrts.add(i * i)
        a = 0
        while a * a <= c:
            bsquared = c - a * a
            if bsquared in sqrts:
                return True
            a += 1
        return False