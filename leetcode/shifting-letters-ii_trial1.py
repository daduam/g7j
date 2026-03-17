class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        psum = [0] * (len(s)+1)
        for start, end, direction in shifts:
            dt = 1 if direction == 1 else -1
            psum[start] += dt
            psum[end+1] -= dt
        ans = []
        rdt = 0
        for i in range(len(s)):
            rdt += psum[i]
            offset = (ord(s[i]) - ord('a') + rdt) % 26
            ans.append(chr(ord('a') + offset))
        return ''.join(ans)