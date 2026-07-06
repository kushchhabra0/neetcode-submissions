class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        # Helper function: Kya hum array ko aise chunks me tod sakte hain 
        # jahan kisi bhi chunk ka sum 'largest' se bada na ho?
        def canSplit(largest):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                # Jaise hi current chunk ka sum limit cross karega...
                if curSum > largest:
                    subarray += 1  # Purana chunk yahin khatam (close)
                    curSum = n     # Naye chunk ki shuruat is element se
            
            # subarray + 1 isliye kyunki aakhiri bacha hua chunk loop ke baad count hota hai
            return subarray + 1 <= k
            
        # Invariant Bounds Setup:
        # lo = max(nums) - 1 -> Impossible lower bound (kam se kam sabse bada element toh jhelna hi padega)
        # hi = sum(nums) + 1 -> Hamesha valid upper bound (poora array ek hi chunk me daal do)
        lo, hi = max(nums) - 1, sum(nums) + 1
        
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            
            # Minimization Invariant Boundary Control:
            # Agar mid capacity ke sath chunks k se kam ya barabar hain, toh yeh safe zone hai!
            if canSplit(mid):
                hi = mid  # Safe zone me maintain rakho aur chota sum dhoondo
            else:
                lo = mid  # Sum bohot chota hai, bounds badhao
        
        # Invariant Rule: Loop termination par 'hi' hi absolute minimum valid largest sum hoga
        return hi