import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python mein Max-Heap nahi hota, isliye elements ko negative karke push karenge
        stones = [-s for s in stones]
        heapq.heapify(stones)

        # Jab tak heap mein kam se kam 2 stones hain, ladai chalti rahegi!
        while len(stones) > 1:
            first = heapq.heappop(stones)   # Sabse bhaari stone (Sabse choti negative value)
            second = heapq.heappop(stones)  # Doosra sabse bhaari stone
            
            # Agar dono barabar hain (e.g. -8 aur -8), toh dono poore toot gaye, kuch push nahi hoga.
            # Agar barabar nahi hain, toh difference push karna padega.
            if first != second:
                # Formula: first - second 
                # Example: -8 - (-7) = -1 (Jo ki original 1 ka negative hai)
                heapq.heappush(stones, first - second)
        
        # Brahmastra Edge Case Fix: Agar saare stones toot gaye toh heap khali hoga.
        # Khali heap ke case mein 0 return karo, nahi toh bacha hua stone!
        return abs(stones[0]) if stones else 0