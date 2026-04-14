class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex+1):
            currow = [1]
            for j in range(i-1):
                currow.append(row[j] + row[j+1])
            currow.append(1)
            row = currow.copy()
        return row