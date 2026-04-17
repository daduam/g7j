class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sn, pn = len(s), len(p)
        cache = {}

        def helper(si: int, pi: int) -> bool:
            if pi >= pn:
                return si >= sn
            
            if (si, pi) in cache:
                return cache[(si, pi)]
            
            match1 = si < sn and p[pi] in {s[si], '.'}

            if pi + 1 < pn and p[pi+1] == '*':
                if (si, pi+2) not in cache:
                    cache[(si, pi+2)] = helper(si, pi+2)
                    
                return cache[(si, pi+2)] or (match1 and helper(si+1, pi))
            
            if (si+1, pi+1) not in cache:
                cache[(si+1, pi+1)] = helper(si+1, pi+1)
                
            return match1 and cache[(si+1, pi+1)]

        return helper(0, 0)