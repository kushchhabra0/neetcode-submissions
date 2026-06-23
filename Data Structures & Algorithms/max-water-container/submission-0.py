class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        # Shuruat me do pointers lelo: ek ekdam extreme left par aur ek extreme right par
        # Is tarah se hume sabse badi possible width (width = right - left) shuruat me hi mil jaati hai
        left, right = 0, len(heights) - 1

        while left < right:
            # Area ka formula: Width * Height
            # Height hamesha dono vertical lines me se CHOTI wali se decide hoti hai (kyunki paani overflow ho jayega)
            current_width = right - left
            current_height = min(heights[left], heights[right])
            current_area = current_width * current_height
            
            # Global maximum area ko update karo
            max_area = max(max_area, current_area)

            # GREEDY SHIFTING LOGIC:
            # Jo line choti hai, use aage badhao! 
            # Kyunki width toh har step par 1 unit kam ho hi rahi hai (right - left),
            # toh agar hum badi line ko chhedenge, toh area kabhi badh hi nahi payega.
            # Area badhane ka ek hi mauka hai—choti line ko chhodkar kisi badi line ko dhoondna!
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area