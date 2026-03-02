class Solution:
    def smallestNumber(self, num: int) -> int:
        digits = sorted(str(abs(num)))
        if num > 0:
            i = 0
            while digits[i] == '0':
                i += 1
            digits[0], digits[i] = digits[i], digits[0]
            return int(''.join(digits))
        else:
            return -1 * int(''.join(digits[::-1]))
  