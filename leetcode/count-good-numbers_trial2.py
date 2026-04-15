class Solution:
    def binpow(self, a, n, m):
        a %= m
        res = 1
        while n > 0:
            if n & 1 == 1:
                res = (res * a) % m
            a = (a * a) % m
            n //= 2
        return res

    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        npow4 = self.binpow(4, n // 2, mod)
        npow5 = self.binpow(5, n // 2 + (n & 1), mod)
        return (npow4 * npow5) % mod