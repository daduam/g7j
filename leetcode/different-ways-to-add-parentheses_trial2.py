class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        memo = [[None] * n for _ in range(n)]

        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
        }

        def helper(left, right):
            ret = []
            for i in range(left, right+1):
                if expression[i] in ops:
                    lnums = memo[left][i-1] if memo[left][i-1] is not None else helper(left, i - 1)
                    rnums = memo[i+1][right] if memo[i+1][right] is not None else helper(i + 1, right)
                    for a in lnums:
                        for b in rnums:
                            ret.append(ops[expression[i]](a, b))
            if not ret:
                ret.append(int(expression[left:right+1]))
            return ret
        
        return helper(0, len(expression)-1)