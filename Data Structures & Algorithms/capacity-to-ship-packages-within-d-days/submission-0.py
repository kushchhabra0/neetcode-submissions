class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Lower bound: max(weights) - 1 (Kyunki ship ko sabse bhaari item toh uthana hi padega)
        # Upper bound: sum(weights) (Saare items ek hi din me bhej do)
        lo = max(weights) - 1
        hi = sum(weights)
        
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            
            # Helper logic: Mid capacity ke sath kitne din lagenge?
            required_days = 1
            current_day_weight = 0
            
            for w in weights:
                if current_day_weight + w > mid:
                    required_days += 1       # Din badh gaya, naya ship mangwao
                    current_day_weight = w    # Naye din ka load is package se shuru
                else:
                    current_day_weight += w   # Same ship me adjust ho gaya
                
                # Agar kisi bhi point par required_days target days se bada ho gaya,
                # toh aage loop chalane ka koi fayda nahi. Yahin se bahar niklo!
                if required_days > days:
                    break
            
            # Minimization Invariant Control:
            # Agar required_days diye gaye days se kam ya barabar hain, toh mid valid capacity hai!
            if required_days <= days:
                hi = mid  # Safe zone me maintain rakho aur choti capacity dhoondo
            else:
                lo = mid
                
        return hi