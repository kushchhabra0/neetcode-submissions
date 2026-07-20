from typing import List

class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []  # '(' ke indices store karega
        star = []  # '*' ke indices store karega
        
        # Step 1: Forward Pass
        for i, ch in enumerate(s):
            if ch == '(':
                left.append(i)
            elif ch == '*':
                star.append(i)
            else: # ch == ')'
                if not left and not star:
                    return False  # Extra closing bracket mila bina match ke
                
                # Pehle '(' ko match karne ki priority do
                if left:
                    left.pop()
                else:
                    star.pop()
        
        # Step 2: Cleanup Leftover '(' using '*'
        # Stack ke top par rakhe indices ko compare karo
        while left and star:
            # Agar sabse aakhri '(' kisi '*' ke bhi BAAD aaya hai,
            # toh star us '(' ko close nahi kar sakta! (e.g., "*( ")
            if left[-1] > star[-1]:
                return False
            
            # Agar order sahi hai ( '(' pehle aaya hai '*' se ), toh dono ko pair kar do
            left.pop()
            star.pop()
        
        # Agar saare '(' clear ho gaye, toh string valid hai
        return len(left) == 0