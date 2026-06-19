import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Step 1: Pehle 'k' elements ka ek sub-array banao
        heap = nums[:k]
        
        # Is sub-array ko in-place Min-Heap me convert karo.
        # Min-Heap ka rule: Sabse choti (minimum) value humesha top par (heap[0]) hogi.
        heapq.heapify(heap)

        # Step 2: Baki bache hue elements par loop chalao
        for num in nums[k:]:
            # Agar current number heap ke sabse chote element (heap[0]) se bada hai,
            # toh iska matlab heap[0] hamara Kth largest element nahi ho sakta.
            
            if num > heap[0]:
                # Ek hi jhatke me purana bahar aur naya andar!
                heapq.heappushpop(heap, num)
                """
                heapq.heappop(heap)          # Sabse chote ko bahar nikalo
                heapq.heappush(heap, num)    # Is naye bade number ko andar dalo
                """
        # Step 3: Loop khatam hone ke baad, heap me sirf top 'k' largest elements bachenge.
        # Aur un 'k' largest elements me se jo sabse chota hoga (yaani heap[0]), 
        # wahi hamara poori array ka Kth largest element ban jayega!
        return heap[0]