class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # 1. MINIMIZATION PROBLEM (First Occurrence Dhoondna)
        def firstOccurence(nums, target):
            lo, hi = -1, len(nums)
            while lo + 1 < hi:
                mid = (lo + hi) // 2
                # Agar element target ke barabar ya usse bada hai, toh hum 'hi' ko mid par late hain.
                # Isse 'hi' hamesha pehle 'target' ya usse bade element ko point karega.
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid
            
            # Loop ke baad agar 'hi' array ke bahar nikal gaya, ya us index par target nahi hai,
            # iska matlab target array me hai hi nahi.
            if hi == len(nums) or nums[hi] != target:
                return -1
            return hi

        # 2. MAXIMIZATION PROBLEM (Last Occurrence Dhoondna)
        def lastOccurence(nums, target):
            lo, hi = -1, len(nums)
            while lo + 1 < hi:
                mid = (lo + hi) // 2
                # Agar element target ke barabar ya usse chota hai, toh hum 'lo' ko mid par late hain.
                # Isse 'lo' hamesha aakhiri 'target' ya usse chote element ko point karega.
                if nums[mid] <= target:
                    lo = mid
                else:
                    hi = mid

            # Loop ke baad agar 'lo' -1 reh gaya, ya us index par target nahi hai,
            # iska matlab target mila hi nahi.
            if lo == -1 or nums[lo] != target:
                return -1
            return lo
        
        # Dono functions ko call karo aur result list me daal do
        return [firstOccurence(nums, target), lastOccurence(nums, target)]