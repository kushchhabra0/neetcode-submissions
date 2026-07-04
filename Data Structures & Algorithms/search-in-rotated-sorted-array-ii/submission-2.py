class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = -1, len(nums)

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if nums[mid] == target:
                return True
            
            # CRITICAL DUPLICATE CHECK:
            # Agar left edge aur mid dono barabar hain, toh hum clear decision nahi le sakte.
            # Dono boundary elements ko ek-ek step andar squeeze karo aur search space chota karo.
            if nums[lo + 1] == nums[mid]:
                lo += 1

            
            # Case 1: Left half strictly sorted hai
            elif nums[lo + 1] < nums[mid]:
                if nums[lo + 1] <= target < nums[mid]:
                    hi = mid 
                else:
                    lo = mid
            
            # Case 2: Right half strictly sorted hai
            else:
                if nums[mid] < target <= nums[hi - 1]:
                    lo = mid
                else:
                    hi = mid
        
        # Agar loop khatam ho gaya aur target nahi mila, toh False return hoga
        return False