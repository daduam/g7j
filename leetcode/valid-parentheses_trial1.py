class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if len(stack) > 0 and open.get(ch, None) == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0