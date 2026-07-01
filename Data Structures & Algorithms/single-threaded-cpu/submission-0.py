import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # indicies ko bhi task me dallo to track the index after sorting
        for i, t in enumerate(tasks): # [1,4,0],[3,3,1]
            t.append(i)
        
        tasks.sort(key = lambda t: t[0]) # sort on enque time

        res, minHeap = [], []
        # Optimization: Time ko 0 se start karo, dynamic fast-forward handle kar lega
        i, time = 0, 0 

        while minHeap or i < len(tasks):
            # append the task to heap if CPU kan procees it 
            while i < len(tasks) and time >= tasks[i][0]:
                # we only need processing time and index of tasks
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1

            if not minHeap:
                # Check lagaya taaki 'i' bounds se bahar hone par crash na ho
                # skip the idle waiting time if t = 2 nd enq = 7, skip to 7 directly
                if i < len(tasks):
                    time = tasks[i][0]
            else:
                procTime, index = heapq.heappop(minHeap)
                time += procTime
                res.append(index)
        
        return res