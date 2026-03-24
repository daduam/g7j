class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        ans, left, uniqcnt = 0, 0, 0
        for right in range(len(fruits)):
            curfruit = fruits[right]
            if freq[curfruit] == 0:
                uniqcnt += 1
            freq[curfruit] += 1
            while uniqcnt > 2:
                candidate = fruits[left]
                if freq[candidate] == 1:
                    uniqcnt -= 1
                freq[candidate] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
        