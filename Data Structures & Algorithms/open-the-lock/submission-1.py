from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Edge Case 1: Agar starting state "0000" hi deadend mein hai, 
        # toh aage badhna impossible hai
        if "0000" in deadends:
            return -1
        
        # Helper function: Lock position se saare 8 possible next combinations generate karta hai
        # (Har 4 wheels ko 1 step forward +1 ya 1 step backward -1 turn karke)
        def children(lock):
            res = []
            for i in range(4):
                # Forward turn (+1) with modulo 10 for '9' -> '0' wrap-around
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])

                # Backward turn (-1) with modulo 10 for '0' -> '9' wrap-around
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])

            return res
        
        # BFS Initialization
        q = deque()
        q.append(["0000", 0])  # Queue stores pairs of [current_lock_state, turns]
        
        # Deadends set mein store karke unko pre-visited mark kar do 
        # taaki search space un par kabhi expansion na kare
        visited = set(deadends)
        visited.add("0000")    # Starting state ko visit mark kar do

        # BFS Traversal (Guarantees shortest path/turns)
        while q:
            lock, turns = q.popleft()
            
            # Target match hote hi turns return kar do
            if lock == target:
                return turns
            
            # Neighbor combinations generate karke check karo
            for child in children(lock):
                if child not in visited:
                    visited.add(child)            # Mark visited immediately to prevent duplicates
                    q.append([child, turns + 1])  # Push to queue with incremented turn count
        
        # Agar queue khali ho jaye aur target na mile
        return -1