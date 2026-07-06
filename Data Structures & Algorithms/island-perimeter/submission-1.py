from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])
        
        # Pure grid ko linearly left-to-right aur top-to-bottom scan karo
        for i in range(rows):
            for j in range(cols):
                # Target Check: Agar current cell land (1) hai
                if grid[i][j] == 1:
                    # Shuruat mein maan lo is akele square ki 4 deewarein open hain
                    perimeter += 4
                    
                    # Comparison 1: Check karo ki kya iske just UPAR waala cell bhi land hai?
                    # Agar hai, toh dono ki 1-1 common deewar chup gayi, yani -2 perimeter kam karo
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                        
                    # Comparison 2: Check karo ki kya iske just LEFT waala cell bhi land hai?
                    # Agar hai, toh yahan bhi common wall ki wajah se -2 perimeter kam karo
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2
                        
        return perimeter

"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(i,j):
            if i >= len(grid) or j >= len(grid[0]) \
            or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            
            if (i,j) in visited:
                return 0
            
            visited.add((i,j))
            perim = dfs(i,j+1)
            perim += dfs(i,j-1)
            perim += dfs(i-1,j)
            perim += dfs(i+1,j)

            return perim

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)
"""
