class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # PREDICATE FUNCTION:
        # Yeh function check karta hai ki kya hum rotated array ke RIGHT SORTED portion me hain?
        # Agar nums[mid] <= nums[-1] hai, iska matlab mid ke aage se lekar aakhir tak sab sorted hai,
        # aur hamara minimum element ya toh khud 'mid' hai ya uske left side me chupa hai.
        def PivotOnRight(mid):
            return nums[mid] <= nums[len(nums) - 1]

        # Invariant Boundaries: 
        # lo = -1 (Virtual boundary jo hamesha peak/left sorted side me rahegi)
        # hi = len(nums) - 1 (Hamesha right sorted portion ke kisi element ko hold karega)
        lo, hi = -1, len(nums) - 1

        while lo + 1 < hi:
            mid = (lo + hi) // 2
            
            if PivotOnRight(mid):
                # Agar mid right sorted portion me hai, toh minimum ya toh mid hai ya uske piche hai.
                # Isliye 'hi' ko mid par le aao (taaki 'hi' hamesha valid zone me rahe)
                hi = mid
            else:
                # Agar mid left portion me hai (badi values wale zone me), toh minimum strictly iske aage hoga.
                # Isliye 'lo' ko mid par le aao
                lo = mid
        
        # LOOP TERMINATION MAGIC:
        # Jab loop rukega, tab 'lo' aur 'hi' padosi ban chuke honge (lo + 1 == hi).
        # 'lo' khada hoga left portion ke sabse aakhiri (bade) element par, 
        # aur 'hi' thik uske agle index yaani right portion ke SABSE PEHLE (SABSE CHOTE) element par!
        return nums[hi]