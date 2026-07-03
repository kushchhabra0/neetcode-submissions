import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # lo = 0 (impossible speed), hi = max(piles) + 1 (hamesha valid speed zone)
        lo = 0
        hi = max(piles) + 1
        
        while lo + 1 < hi:
            mid = (lo + hi) // 2

            totalTime = 0
            for p in piles:
                # Math.ceil handle karega partial hours ko safely
                totalTime += math.ceil(p / mid)
                
            # Minimization Invariant Boundary Control:
            # Agar mid speed se time target h ke barabar ya chota hai, toh yeh valid hai!
            # 'hi = mid' karke hum ise safe zone me maintain rakhte hain aur choti speed dhoondte hain
            if totalTime <= h:
                hi = mid
            else:
                lo = mid
        
        # Invariant Rule: Loop termination par 'hi' hi absolute minimum valid speed hogi
        return hi