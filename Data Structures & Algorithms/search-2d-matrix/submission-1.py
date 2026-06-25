class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row_lo,row_hi = -1,m
        while row_lo+1 < row_hi:
            mid = (row_lo + row_hi) // 2
            if matrix[mid][n-1] >= target:
                row_hi = mid
            else:
                row_lo = mid
        
        row = row_hi
        if row >= m:
            return False
        col_lo,col_hi = -1,n
        while col_lo + 1 < col_hi:
            mid = (col_lo + col_hi)//2
            if matrix[row][mid] >= target:
                col_hi = mid
            else:
                col_lo = mid
        
        col = col_hi

        if col < n:
            return matrix[row][col] == target
            
        return False
            
        