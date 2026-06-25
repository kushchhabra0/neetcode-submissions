class Solution:
    def mySqrt(self, x: int) -> int:
        # Boundaries set karo: 0 se lekar x + 1 tak (Safe for x = 0 and x = 1)
        # lo zone represents: mid * mid <= x
        # hi zone represents: mid * mid > x
        lo, hi = 0, x + 1

        while lo + 1 < hi:
            mid = (lo + hi) // 2
            
            # Agar mid * mid bada hai x se, toh yeh pakka unsafe zone hai
            if mid * mid > x:
                hi = mid
            else:
                # Agar mid * mid <= x hai, toh yeh safe zone hai. 
                # Hum lo ko mid par le aayenge taaki maximize kar sakein.
                lo = mid

        # Loop ke baad, lo + 1 == hi hoga.
        # lo khada hoga maximum possible value par jiska square <= x hai.
        return lo