class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Sliding window ke andar ke elements ko O(1) me check karne ke liye Set banaya
        window = set()
        l = 0  # Left pointer (window ki shuruat)

        # Right pointer array ke har element par aage badhega
        for r in range(len(nums)):
            # Agar window ka size 'k' se bada ho gaya (index difference > k)
            # Toh left side se purana element remove karo aur left pointer aage badhao
            if r - l > k:
                window.remove(nums[l])
                l += 1
                
            # Agar current element pehle se hi window (set) me maujood hai,
            # matlab hume k distance ke andar duplicate mil gaya!
            if nums[r] in window:
                return True
                
            # Current element ko window me add karo
            window.add(nums[r])
            
        return False