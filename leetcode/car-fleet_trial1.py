class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pairs)[::-1]:
            tt = (target - p) / s
            if not stack or tt > stack[-1]:
                stack.append(tt)
        return len(stack)