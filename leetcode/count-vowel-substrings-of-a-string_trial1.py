class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        windows = set()
        for start in range(len(word)):
            for end in range(len(word)):
                chars = set()
                for ch in word[start:end+1]:
                    chars.add(ch)
                if chars == set('aeiou'):
                    windows.add((start, end))
        return len(windows)
        