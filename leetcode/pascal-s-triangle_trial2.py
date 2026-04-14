class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(1, numRows):
            row = [1]
            prev = triangle[-1]
            for j in range(i-1):
                row.append(prev[j] + prev[j+1])
            row.append(1)
            triangle.append(row)
        return triangle