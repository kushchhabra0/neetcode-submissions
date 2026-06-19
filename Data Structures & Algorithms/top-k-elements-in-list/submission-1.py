class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        res = []
        for num in nums:
            mp[num] = mp.get(num,0) +1
        heap = []    
        for num in mp.keys():
            heapq.heappush(heap,(mp[num],num))
            if len(heap) >k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res            