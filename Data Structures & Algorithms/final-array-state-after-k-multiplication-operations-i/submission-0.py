import heapq
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Original array ko modify hone se bachane ke liye copy banao
        res = nums[:]

        # Step 1: Min-Heap initialize karo pairs (value, index) ke saath
        # Python tuple comparison (value, index) automatic tie-breaking handle karti hai:
        # Same value hone par chota index pehle pop hoga.
        minheap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(minheap)

        # Step 2: 'k' operations perform karo
        for _ in range(k):
            # Sabse choti value aur uska index heap se pop karo
            num, i = heapq.heappop(minheap)

            # Result array mein element ko multiplier se multiply karo
            res[i] *= multiplier
            
            # Updated element aur uske index ko back heap mein push karo
            heapq.heappush(minheap, (res[i], i))
        
        return res