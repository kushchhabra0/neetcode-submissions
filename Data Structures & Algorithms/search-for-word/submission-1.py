class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COL = len(board), len(board[0])
        path = set() # Current DFS path me visited cells ko track karne ke liye (Avoids reusing same cell)

        def dfs(r, c, i):
            # Base Case 1: Agar 'i' word ki length tak pahunch gaya, matlab pura word mil gaya!
            if i == len(word):
                return True

            # Base Case 2: Out of bounds check YA galat character YA cell pehle se visited hai
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COL or
                word[i] != board[r][c] or 
                (r, c) in path):
                return False

            # 1. Action: Current cell ko path me daalo (Mark Visited)
            path.add((r, c))
            
            # 2. Explore: Charo directions (Down, Up, Right, Left) me next character dhoondo
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1)) 
                   
            # 3. Backtrack: Wapas aate waqt cell ko path se hatao (Mark Unvisited)
            path.remove((r, c))

            return res

        # Matrix ke har ek cell ko starting point bana kar check karo
        for r in range(ROWS):
            for c in range(COL):
                if dfs(r, c, 0):
                    return True # Agar kahi se bhi word mil jaye, toh True return kar do
        return False