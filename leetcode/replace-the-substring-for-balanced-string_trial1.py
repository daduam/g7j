class Solution:
    def balancedString(self, s: str) -> int:
        freq = Counter(s)
        ans, left, want = len(s), 0, len(s) / 4
        for right in range(len(s)):
            freq[s[right]] -= 1
            while left < len(s) and max(freq.values()) <= want:
                freq[s[left]] += 1
                ans = min(ans, right - left + 1)
                left += 1
        return ans
        