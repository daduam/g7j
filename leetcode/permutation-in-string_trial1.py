class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1freq = Counter(s1)
        s2freq = Counter(s2[:n-1])
        left, right, ans = 0, n-1, False
        while right < len(s2):
            s2freq[s2[right]] += 1
            ans = ans or s1freq == s2freq
            s2freq[s2[left]] -= 1
            right += 1
            left += 1
        return ans
        