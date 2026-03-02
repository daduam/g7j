class Solution:
    def frequencySort(self, s: str) -> str:
        sarr = list(s)
        freq = Counter(sarr)
        return ''.join(sorted(sarr, key=lambda x: (-freq[x], ord(x))))
 