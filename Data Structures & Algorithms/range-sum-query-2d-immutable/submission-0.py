from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Matrix ki dimensions extract karo
        ROWS, COLS = len(matrix), len(matrix[0])

        # Step 1: Initialize 2D Prefix Sum Matrix with size (ROWS + 1) x (COLS + 1)
        # Extra 0-row aur 0-column boundary edge cases (row1=0, col1=0) ko effortlessly handle karta hai
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # Precompute 2D Prefix Sums
        for r in range(ROWS):
            prefix = 0  # Row-wise running prefix sum
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]  # Pichli saari rows ka cumulative sum
                # Current 2D cell sum = current row prefix sum + above rows sum
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Step 2: Convert 0-indexed query coordinates to 1-indexed (for sumMat)
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        # 2D Inclusion-Exclusion Formula:
        bottomRight = self.sumMat[r2][c2]    # Full rectangle from (0,0) to (r2,c2)
        above = self.sumMat[r1 - 1][c2]       # Top unwanted rectangle
        left = self.sumMat[r2][c1 - 1]        # Left unwanted rectangle
        topLeft = self.sumMat[r1 - 1][c1 - 1] # Over-subtracted corner region (Add back!)

        # Result in O(1) Constant Time!
        return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)