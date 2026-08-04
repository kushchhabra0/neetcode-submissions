from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # Base Case 1: Out of bounds check
            # Base Case 2: Water cell ('0') or already visited cell
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
            
            # Mark current land cell as visited by sinking it to '0'
            grid[r][c] = "0"
            
            # Traverse all 4 cardinal directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # Grid scan
        for r in range(ROWS):
            for c in range(COLS):
                # Whenever an unvisited land cell ('1') is found
                if grid[r][c] == "1":
                    dfs(r, c)      # Connected land mass ko completely sink kar do
                    islands += 1   # Increment island count

        return islands