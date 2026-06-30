class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Fixed array of 9 empty sets setup karein (Memory pre-allocation)
        # Hamesha comprehension use karein taaki har set unique memory reference ho
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Khaali cells ko seedhe skip maaro
                if val == ".":
                    continue
                
                # Integer Formula to map 3x3 grids to 1D index (0 to 8)
                square_idx = (r // 3) * 3 + (c // 3)
                
                # Duplicate Check Validation:
                # Agar aaj ka character rows, cols ya squares ke pre-existing set mein milta hai
                # toh rule broke, seedhe False return maaro!
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[square_idx]):
                    return False
                
                # Direct insertion in pre-allocated sets
                rows[r].add(val)
                cols[c].add(val)
                squares[square_idx].add(val)
                
        return True
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) # hash set of pair (r//3,c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3),(c//3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3),(c//3)].add(board[r][c])
        
        return True
"""