class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Hum virtual boundaries -1 aur len(nums) se shuru karte hain.
        # Isse out-of-bounds ka koi risk nahi rehta aur insertion extreme ends par bhi safe hota hai.
        lo, hi = -1, len(nums)

        # AAPKA EXCELLENT PATTERN: Loop tab tak chalega jab tak lo aur hi ke beech 
        # kam se kam ek index ka gap ho.
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            
            if nums[mid] > target:
                # Agar mid bada hai, toh target left side me hoga, 'hi' ko mid par le aao
                hi = mid
            elif nums[mid] < target:
                # Agar mid chota hai, toh target right side me hoga, 'lo' ko mid par le aao
                lo = mid
            else:
                # Agar element exact match ho gaya, toh wahi sahi position hai!
                return mid
        
        # MAGIC STATE: Jab loop rukega, tab target ke na milne par 'hi' exactly 
        # us position par hoga jahan target ko sabse pehle insert hona chahiye taaki array sorted rahe.
        return hi