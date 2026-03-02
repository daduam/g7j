class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        for row in image:
            ans.append([x ^ 1 for x in row[::-1]])
        return ans
 