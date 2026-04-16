class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        nbits = 2 ** (n-1)
        mid = nbits // 2
        if k <= mid:
            return self.kthGrammar(n-1, k)
        return (1 - self.kthGrammar(n-1, k - mid))