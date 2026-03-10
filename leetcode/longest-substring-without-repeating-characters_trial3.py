class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char2idx = dict()
        left, ans = 0, 0
        for right in range(len(s)):
            ch = s[right]
            idx = char2idx.get(ch, -1)
            if idx >= left:
                left = idx + 1
            char2idx[ch] = right
            ans = max(ans, right - left + 1)
        return ans
        