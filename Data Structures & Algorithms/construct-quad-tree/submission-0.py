"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        # dfs(n, r, c) -> n: size of current sub-grid, r: row start, c: col start
        def dfs(n, r, c):
            allSame = True
            
            # 1. CHECK IF ALL ELEMENTS IN CURRENT SUB-GRID ARE SAME
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        allSame = False
                        break # Inner loop break hua
                if not allSame:
                    break # CRITICAL FIX: Outer loop ko bhi turant break karo taaki TLE na aaye!
            
            # 2. BASE CASE: Agar saare elements same hain, toh yeh ek Leaf Node hai
            if allSame:
                # Leaf node me val=grid[r][c], isLeaf=True aur baaki charo pointers None hote hain
                return Node(grid[r][c] == 1, True, None, None, None, None)
            
            # 3. DIVIDE AND CONQUER PHASE: Agar elements alag hain, toh 4 barabar tukdo me baanto
            n = n // 2
            
            # Har quadrant ka starting coordinate dhyan se pass karo
            topleft     = dfs(n, r, c)
            topright    = dfs(n, r, c + n)
            bottomleft  = dfs(n, r + n, c)
            bottomright = dfs(n, r + n, c + n)

            # Non-leaf node me value kuch bhi ho sakti hai (usually 1 ya 0), isLeaf=False, aur charo bacche attach honge
            return Node(True, False, topleft, topright, bottomleft, bottomright)
        
        return dfs(len(grid), 0, 0)