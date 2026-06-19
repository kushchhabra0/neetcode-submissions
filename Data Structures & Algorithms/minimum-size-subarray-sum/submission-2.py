class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, total = 0, 0, 0
        res = float("inf") # Sabse choti length track karne ke liye initial value Infinity rakhi
        n = len(nums)
        
        while r < n:
            # Right side se naya element window me add karo
            total += nums[r]
            
            # Jab tak window ka total sum target se bada ya barabar hai (Valid Window)
            while total >= target:
                # Minimum length ko update karo (r - l + 1)
                res = min(r - l + 1, res)
                
                # Left side se element ko total se nikalo aur window ko chota karo
                total -= nums[l]
                l += 1
                
            # Right pointer ko aage badhao
            r += 1
        
        # Agar res abhi bhi Infinity hai, matlab aisa koi subarray nahi mila jiska sum >= target ho
        if res == float("inf"):
            return 0    
        return res