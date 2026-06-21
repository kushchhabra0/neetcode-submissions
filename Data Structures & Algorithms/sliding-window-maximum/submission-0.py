from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        res = []
        q = deque()  # Isme hum elements ke INDICES store karenge

        while r < len(nums):
            # 1. MONOTONIC CLEANUP:
            # Jab tak queue me baithe purane elements naye incoming 'nums[r]' se chote hain,
            # unhe piche se pop() karke uda do. Kyunki wo ab kabhi max nahi ban sakte.
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # 2. OUT OF BOUNDS CLEANUP:
            # Agar deque ka front element (sabse bada element) hamari current window 
            # ke left bound 'l' se peeche chhoot gaya hai, toh use aage se popleft() kar do.
            if l > q[0]:
                q.popleft()
            
            # 3. CONSTRUCT RESULT:
            # Jaise hi window pehli baar size 'k' par pahunchti hai (yaani r + 1 >= k),
            # hum res me max element add karte hain aur left pointer 'l' ko shift karte hain.
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
                
            r += 1  # Window ka right edge aage badhao
        
        return res