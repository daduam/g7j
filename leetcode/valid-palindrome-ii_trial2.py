class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                skipleft = s[left+1:right+1] == s[left+1:right+1][::-1]
                skipright = s[left:right] == s[left:right][::-1]
                return skipleft or skipright
            left += 1
            right -= 1
        return True