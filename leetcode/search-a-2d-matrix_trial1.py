class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        lo, hi = 0, len(matrix)-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target < matrix[mid][0]:
                hi = mid - 1
            elif matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            else:
                lo = mid + 1
        
        if row == -1:
            return False

        lo, hi = 0, len(matrix[0])-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False