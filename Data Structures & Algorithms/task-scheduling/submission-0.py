from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # -------------------------------------------------------------
        # STEP 1: Frequencies Count Karo Aur Max-Heap Taiyar Karo
        # -------------------------------------------------------------
        # Counter hume har character ka count dega. E.g., {'A': 3, 'B': 1}
        count = Counter(tasks)
        
        # Python mein default Min-Heap hota hai. Max-Heap simulate karne ke liye 
        # hum saare counts ko NEGATIVE kar dete hain. 
        # E.g., count 3 ban jayega -3, jo heap mein sabse pehle pop hoga.
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # -------------------------------------------------------------
        # STEP 2: Time Tracker Aur Cool-down Queue Setup
        # -------------------------------------------------------------
        time = 0
        
        # Queue mein hum un tasks ko dalenge jo abhi "Cool-down" (idle) state mein hain.
        # Format: pairs of [remaining_count, next_available_time]
        q = deque()  

        # -------------------------------------------------------------
        # STEP 3: Simulation Loop (Jab tak tasks bache hain)
        # -------------------------------------------------------------
        # Loop tab tak chalega jab tak heap mein ready tasks hain YA queue mein cool-down ho rahe hain
        while maxHeap or q:
            time += 1  # Clock ki ek tick aage badhi (1 unit of time consumed)

            # BRAHMASTRA OPTIMIZATION (The Idle Fast-Forward Trap Fix):
            # Agar maxHeap khali hai, matlab abhi chalane ke liye koi ready task nahi hai.
            # Saare bache hue tasks queue mein cool-down ka wait kar rahe hain.
            # Toh har ek tick par loop chalane ke bajaye, hum direct clock ko fast-forward
            # karke queue ke sabse pehle element ke release time par le jayenge!
            if not maxHeap:
                time = q[0][1]  # Direct jump to the time when the next task becomes available
            else:
                # Agar heap mein tasks hain, toh sabse high frequency wale task ko pop karo.
                # Kyunki value negative thi, isme +1 karne ka matlab hai frequency ko 1 se KAM karna.
                # E.g., 1 + (-3) = -2 (Yaani original count 3 se ghatkar 2 ho gaya)
                cnt = 1 + heapq.heappop(maxHeap)
                
                # Agar us task ke abhi bhi aur rounds bache hain (cnt != 0)
                if cnt:
                    # Use cool-down ke liye queue mein daal do.
                    # Wo task ab strictly kab ready hoga? current time + cooling period (n)
                    q.append([cnt, time + n])
            
            # -------------------------------------------------------------
            # STEP 4: Queue Se Re-entry Check (Cool-down Khatam)
            # -------------------------------------------------------------
            # Har tick par check karo: Kya queue ke front wale task ka cool-down poora ho gaya?
            # Agar queue ka target release time hamare current time ke barabar ho gaya hai...
            if q and q[0][1] == time:
                # ...toh use queue se nikal kar (popleft) wapas ready pool (maxHeap) mein daal do!
                heapq.heappush(maxHeap, q.popleft()[0])
                
        # Jab saare tasks khatam aur queue khali, toh total time return kar do
        return time