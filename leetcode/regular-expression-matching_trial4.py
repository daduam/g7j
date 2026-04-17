class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sn, pn = len(s), len(p)
        cache = {}

        def helper(si: int, pi: int) -> bool:
            if (si, pi) in cache:
                return cache[(si, pi)]
            
            if pi >= pn:
                return si >= sn
            
            match1 = si < sn and p[pi] in {s[si], '.'}

            if pi + 1 < pn and p[pi+1] == '*':
                cache[(si, pi)] = helper(si, pi+2) or (match1 and helper(si+1, pi))
                return cache[(si, pi)]
            
            cache[(si, pi)] = match1 and helper(si+1, pi+1)
            return cache[(si, pi)]

        return helper(0, 0)