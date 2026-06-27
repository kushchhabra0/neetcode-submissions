import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        
        for x, y in points:
            # Distance formula: x^2 + y^2 (sqrt lene ki zaroorat nahi hai comparison ke liye)
            # Max-Heap simulate karne ke liye dist ko negative kiya
            dist = -(x**2 + y**2)
            
            # Heap mein push karo tuple: (negative_distance, x, y)
            heapq.heappush(maxHeap, (dist, x, y))
            
            # Brahmastra Move: Agar size K se bada hua, toh jo sabse door (max distance) 
            # wala element hai, usko pop karke bahar pheko!
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
                
        # Ab heap mein strictly sirf K closest elements bache hain
        # Unhe nikal kar format karo aur return kar do
        return [[x, y] for dist, x, y in maxHeap]