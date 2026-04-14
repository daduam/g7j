class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverseStringHelper(s, 0, len(s)-1)

    def reverseStringHelper(self, s: List[str], left: int, right: int) -> None:
        if left >= right:
            return
        s[left], s[right] = s[right], s[left]
        return self.reverseStringHelper(s, left + 1, right - 1)