class Solution:
    def decodeString(self, s: str) -> str:
        chstack = []
        kstack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                k = []
                while s[i].isdigit():
                    k.append(s[i])
                    i += 1
                i -= 1
                kstack.append(int(''.join(k)))
            elif s[i] == ']':
                enc = []
                while chstack and chstack[-1] != '[':
                    enc.append(chstack.pop())
                chstack.pop()
                k = kstack.pop()
                chstack += enc[::-1] * k
            else:
                chstack.append(s[i])
            i += 1
        return ''.join(chstack)