import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        res = []
        
        # Step 1: Har number ki frequency count karke map mein store karo
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
            
        heap = []    
        # Step 2: Min-Heap ka use karke top 'k' frequent elements maintain karo
        for num in mp.keys():
            # Heap mein (frequency, element) daal rahe hain taaki frequency ke basis pe sort ho
            heapq.heappush(heap, (mp[num], num))
            
            # Agar heap ka size k se bada ho jaye, toh sabse choti frequency wale ko uda do (pop)
            # Isse heap mein hamesha sirf top 'k' highest frequency wale elements hi bachenge
            if len(heap) > k:
                heapq.heappop(heap)
                
        # Step 3: Heap se bache hue k elements nikal kar result list mein daalo
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1]) # [1] kyunki hume sirf element chahiye, frequency nahi
            
        return res