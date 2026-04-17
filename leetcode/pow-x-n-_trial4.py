class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binpow(x: float, n: int) -> float:
            ret = 1
            while n > 0:
                if n & 1:
                    ret *= x
                x *= x
                n //= 2
            return ret
        
        if n >= 0:
            return binpow(x, n)
            
        return 1 / binpow(x, -n)