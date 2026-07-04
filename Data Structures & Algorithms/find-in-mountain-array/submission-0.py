class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # STEP 1: Find the Peak Index (Minimization/Slope detection)
        # Hamesha slopes check karne ke liye lo=0 aur hi=n-1 safe hain
        l, r = 0, n - 1
        while l + 1 < r:
            m = (l + r) // 2
            # Strictly ONLY 2 API calls taaki 100 calls ki limit cross na ho!
            mid_val = mountainArr.get(m)
            right_val = mountainArr.get(m + 1)

            if mid_val < right_val:
                l = m      # Upward slope: Peak right side me hai
            else:
                r = m      # Downward slope: Peak m par hai ya left side me hai
        
        # Loop termination par 'r' hi hamara absolute peak index hoga
        peak = r

        # STEP 2: Search in Left Increasing Portion
        l, r = -1, peak + 1
        while l + 1 < r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)

            if val < target:
                l = mid
            elif val > target:
                r = mid
            else:
                return mid  # Target mil gaya!

        # STEP 3: Search in Right Decreasing Portion
        # Note: Right side me slope ulti hai, toh condition reverse ho jayegi
        l, r = peak - 1, n
        while l + 1 < r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)

            if val > target:
                l = mid    # Decreasing slope me bada element left me hota hai
            elif val < target:
                r = mid
            else:
                return mid  # Target mil gaya!
            
        return -1