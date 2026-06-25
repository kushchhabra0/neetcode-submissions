from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)
        n = len(matrix[0])
        
        # Virtual 1D array boundaries
        # lo zone: element < target
        # hi zone: element >= target
        lo, hi = -1, m * n
        
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            
            # Magic Formula: 1D index se 2D row aur col nikalna
            row = mid // n
            col = mid % n
            
            if matrix[row][col] >= target:
                hi = mid  # Shrink towards left, capturing potential match at hi
            else:
                lo = mid  # Move right
                
        # Loop ke baad, hi khada hoga pehle element par jo >= target hai
        # Check karo ki kya 'hi' valid array bound mein hai aur element target ke barabar hai
        if hi < m * n:
            return matrix[hi // n][hi % n] == target
            
        return False