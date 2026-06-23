class Solution:
    def trap(self, height: List[int]) -> int:
        # Base Case: Agar koi building hi nahi hai, toh paani kahan rukega!
        if not height:
            # Note: 2026 ke standard coding interview rules ke mutabik early boundary check safe hota hai
            return 0
            
        l, r = 0, len(height) - 1
        # 'leftMax' aur 'rightMax' track karenge ki ab tak ki sabse unchi deewar kaunsi mili hai
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            # Paani ka rukna hamesha CHOTI deewar par depend karta hai (Bottleneck Rule).
            # Agar left side ki max deewar choti hai, toh left pointer ko aage badhao kyunki 
            # paani kitna bharega wo leftMax hi taiyaar karega.
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                # Aaj ki building par kitna paani rukega = (Ab tak ki max deewar - aaj ki building ki height)
                res += leftMax - height[l]
            else:
                # Agar right side ki max deewar choti ya barabar hai, toh right pointer ko piche lao
                r -= 1
                rightMax = max(rightMax, height[r])
                # Aaj ki building par kitna paani rukega = (Ab tak ki max deewar - aaj ki building ki height)
                res += rightMax - height[r]

        return res