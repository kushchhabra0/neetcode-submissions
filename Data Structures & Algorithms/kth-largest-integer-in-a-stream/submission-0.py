import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        
        # Step 1: Poori array ko heapify karo
        heapq.heapify(self.minHeap)
        
        # CRITICAL FIX (TLE Avoidance): Heap ko shuruat me hi trim karke sirf top 'k' elements tak lao.
        # Jab tak heap ka size 'k' se bada hai, faltu chote elements ko pop karke nikal do.
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Step 2: Naye element ko push karo
        heapq.heappush(self.minHeap, val)
        
        # Step 3: Agar size 'k' se bada ho gaya, toh sabse chote element (top) ko nikal do
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # Heap ka top (minHeap[0]) humesha dynamic stream ka Kth largest element hoga
        return self.minHeap[0]