class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        sz = n + m - 1
        arr = [[] for _ in range(sz)]
        for i in range(n):
            for j in range(m):
                arr[i + j].append(mat[i][j])
        for i in range(0, sz, 2):
            arr[i].reverse()
        return [x for row in arr for x in row]
